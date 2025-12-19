import streamlit as st
from projectt import Bank

# MUST be first Streamlit command
st.set_page_config(page_title="Bank Management System", layout="wide")

bank = Bank()

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "View Account",
        "Update Account",
        "Delete Account",
    ],
)

# ---------------- CREATE ACCOUNT ----------------
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Customer Name")
    age = st.number_input("Age", min_value=1, step=1)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create Account"):
        if not name or not email or not pin:
            st.error("All fields are required")
        elif len(pin) != 4 or not pin.isdigit():
            st.error("PIN must be 4 digits")
        elif age < 18:
            st.error("Age must be 18+")
        else:
            info = {
                "name": name,
                "age": age,
                "email": email,
                "pin": int(pin),
                "accountNo.": Bank._Bank__accountgenerate(),
                "balance": 0,
            }
            Bank.data.append(info)
            Bank._Bank__update()

            st.success("Account created successfully")
            st.info(f"Account Number: {info['accountNo.']}")

# ---------------- DEPOSIT MONEY ----------------
elif menu == "Deposit Money":
    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, step=1)

    if st.button("Deposit"):
        if not acc or not pin:
            st.error("Account number and PIN required")
        else:
            userdata = [
                i for i in Bank.data
                if i["accountNo."] == acc and i["pin"] == int(pin)
            ]

            if not userdata:
                st.error("Account not found")
            elif amount > 10000:
                st.error("Maximum deposit limit is 10,000")
            else:
                userdata[0]["balance"] += amount
                Bank._Bank__update()
                st.success("Amount deposited successfully")

# ---------------- WITHDRAW MONEY ----------------
elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, step=1)

    if st.button("Withdraw"):
        userdata = [
            i for i in Bank.data
            if i["accountNo."] == acc and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")
        elif userdata[0]["balance"] < amount:
            st.error("Insufficient balance")
        else:
            userdata[0]["balance"] -= amount
            Bank._Bank__update()
            st.success("Amount withdrawn successfully")

# ---------------- VIEW ACCOUNT ----------------
elif menu == "View Account":
    st.subheader("View Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View"):
        userdata = [
            i for i in Bank.data
            if i["accountNo."] == acc and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")
        else:
            st.json(userdata[0])

# ---------------- UPDATE ACCOUNT ----------------
elif menu == "Update Account":
    st.subheader("Update Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    new_name = st.text_input("New Name (optional)")
    new_email = st.text_input("New Email (optional)")
    new_pin = st.text_input("New PIN (optional)", type="password")

    if st.button("Update"):
        userdata = [
            i for i in Bank.data
            if i["accountNo."] == acc and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")
        else:
            user = userdata[0]

            if new_name:
                user["name"] = new_name
            if new_email:
                user["email"] = new_email
            if new_pin:
                if len(new_pin) == 4 and new_pin.isdigit():
                    user["pin"] = int(new_pin)
                else:
                    st.error("PIN must be 4 digits")
                    st.stop()

            Bank._Bank__update()
            st.success("Details updated successfully")

# ---------------- DELETE ACCOUNT ----------------
elif menu == "Delete Account":
    st.subheader("Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        userdata = [
            i for i in Bank.data
            if i["accountNo."] == acc and i["pin"] == int(pin)
        ]

        if not userdata:
            st.error("Account not found")
        else:
            Bank.data.remove(userdata[0])
            Bank._Bank__update()
            st.success("Account deleted successfully")
