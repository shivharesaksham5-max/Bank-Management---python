import streamlit as st
from projectt import Bank

bank = Bank()

st.set_page_config(page_title="Bank Management System")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Option",
    ["Create Account", "Deposit", "Withdraw", "View Account"]
)

# CREATE ACCOUNT
if menu == "Create Account":
    st.subheader("Create New Account")

    name = st.text_input("Customer Name")
    balance = st.number_input("Initial Balance", min_value=0)

    if st.button("Create Account"):
        acc_no = bank.create_account(name, balance)
        st.success(f"Account created successfully!")
        st.info(f"Account Number: {acc_no}")

# DEPOSIT
elif menu == "Deposit":
    st.subheader("Deposit Money")

    acc_no = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        if bank.deposit(acc_no, amount):
            st.success("Deposit successful")
        else:
            st.error("Account not found")

# WITHDRAW
elif menu == "Withdraw":
    st.subheader("Withdraw Money")

    acc_no = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        if bank.withdraw(acc_no, amount):
            st.success("Withdrawal successful")
        else:
            st.error("Insufficient balance or invalid account")

# VIEW ACCOUNT
elif menu == "View Account":
    st.subheader("Account Details")

    acc_no = st.text_input("Account Number")

    if st.button("View"):
        details = bank.get_details(acc_no)
        if details:
            st.json(details)
        else:
            st.error("Account not found")
