import streamlit as st

st.set_page_config(page_title="Bank Manager Demo", layout="centered")

st.title("🏦 Bank Manager Demo")

# Fake in-memory data
if "balance" not in st.session_state:
    st.session_state.balance = 0

menu = st.selectbox(
    "Choose an operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Delete Account"
    ]
)

if menu == "Create Account":
    name = st.text_input("Enter your name")
    if st.button("Create"):
        st.success(f"Account created for {name}")

elif menu == "Deposit Money":
    amount = st.number_input("Enter amount", min_value=0)
    if st.button("Deposit"):
        st.session_state.balance += amount
        st.success(f"Deposited ₹{amount}")

elif menu == "Withdraw Money":
    amount = st.number_input("Enter amount", min_value=0)
    if st.button("Withdraw"):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.success(f"Withdrawn ₹{amount}")
        else:
            st.error("Insufficient balance")

elif menu == "Show Details":
    st.info(f"Current Balance: ₹{st.session_state.balance}")

elif menu == "Delete Account":
    if st.button("Delete"):
        st.session_state.balance = 0
        st.warning("Account deleted")
