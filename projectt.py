import json
import random
import string
from pathlib import Path


class Bank:
    database = "data.json"
    data = []

    # Load data from file
    if Path(database).exists():
        try:
            with open(database, "r") as fs:
                data = json.load(fs)
        except Exception as e:
            print("Error loading data:", e)
    else:
        data = []

    @classmethod
    def __update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%^&*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)

    # ---------------- CREATE ACCOUNT ----------------
    def Createaccount(self):
        try:
            info = {
                "name": input("Tell your name: "),
                "age": int(input("Tell your age: ")),
                "email": input("Tell your email: "),
                "pin": int(input("Tell your 4-digit pin: ")),
                "accountNo.": Bank.__accountgenerate(),
                "balance": 0,
            }
        except:
            print("❌ Invalid input")
            return

        if info["age"] < 18 or len(str(info["pin"])) != 4:
            print("❌ Account creation failed (age < 18 or pin invalid)")
            return

        Bank.data.append(info)
        Bank.__update()

        print("\n✅ Account created successfully")
        for k, v in info.items():
            print(f"{k}: {v}")
        print("⚠ Please save your account number")

    # ---------------- DEPOSIT ----------------
    def depositmoney(self):
        accnumber = input("Account number: ")
        pin = int(input("PIN: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if not userdata:
            print("❌ Account not found")
            return

        amount = int(input("Enter amount to deposit: "))

        if amount <= 0 or amount > 10000:
            print("❌ Invalid amount")
            return

        userdata[0]["balance"] += amount
        Bank.__update()
        print("✅ Amount deposited successfully")

    # ---------------- WITHDRAW ----------------
    def withdrawmoney(self):
        accnumber = input("Account number: ")
        pin = int(input("PIN: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if not userdata:
            print("❌ Account not found")
            return

        amount = int(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("❌ Invalid amount")
            return

        if userdata[0]["balance"] < amount:
            print("❌ Insufficient balance")
            return

        userdata[0]["balance"] -= amount
        Bank.__update()
        print("✅ Amount withdrawn successfully")

    # ---------------- SHOW DETAILS ----------------
    def showdetails(self):
        accnumber = input("Account number: ")
        pin = int(input("PIN: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if not userdata:
            print("❌ Account not found")
            return

        print("\n📄 Account Details\n")
        for k, v in userdata[0].items():
            print(f"{k}: {v}")

    # ---------------- UPDATE DETAILS ----------------
    def updatedetails(self):
        accnumber = input("Account number: ")
        pin = int(input("PIN: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if not userdata:
            print("❌ Account not found")
            return

        user = userdata[0]
        print("⚠ Age, account number & balance cannot be changed")

        name = input("New name (enter to skip): ")
        email = input("New email (enter to skip): ")
        newpin = input("New pin (enter to skip): ")

        if name:
            user["name"] = name
        if email:
            user["email"] = email
        if newpin:
            if len(newpin) == 4 and newpin.isdigit():
                user["pin"] = int(newpin)
            else:
                print("❌ Invalid PIN")

        Bank.__update()
        print("✅ Details updated successfully")

    # ---------------- DELETE ACCOUNT ----------------
    def Delete(self):
        accnumber = input("Account number: ")
        pin = int(input("PIN: "))

        userdata = [i for i in Bank.data if i["accountNo."] == accnumber and i["pin"] == pin]

        if not userdata:
            print("❌ Account not found")
            return

        confirm = input("Press Y to confirm delete: ")

        if confirm.lower() == "y":
            Bank.data.remove(userdata[0])
            Bank.__update()
            print("✅ Account deleted successfully")
        else:
            print("❌ Delete cancelled")


# ---------------- MAIN MENU ----------------
user = Bank()

print("\n1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Show Details")
print("5. Update Details")
print("6. Delete Account")

try:
    choice = int(input("Enter choice: "))
except:
    print("❌ Invalid choice")
    exit()

if choice == 1:
    user.Createaccount()
elif choice == 2:
    user.depositmoney()
elif choice == 3:
    user.withdrawmoney()
elif choice == 4:
    user.showdetails()
elif choice == 5:
    user.updatedetails()
elif choice == 6:
    user.Delete()
else:
    print("❌ Invalid option")
