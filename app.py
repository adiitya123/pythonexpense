import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state for expenses
if "expenses" not in st.session_state:
    st.session_state.expenses = []

# Streamlit App Title
st.title("💰 Personal Finance Tracker")

# Sidebar Input Section
st.sidebar.header("➕ Add a New Expense")
date = st.sidebar.date_input("📅 Select Date")
category = st.sidebar.selectbox("📂 Select Category", ["Food", "Rent", "Bills", "Entertainment", "Others"])
amount = st.sidebar.number_input("💲 Enter Amount", min_value=0.01, format="%.2f")

# Add Button
if st.sidebar.button("Add Expense"):
    st.session_state.expenses.append({"Date": date, "Category": category, "Amount": amount})
    st.sidebar.success("✅ Expense Added!")

# Display Expenses as DataFrame
st.header("📋 Expense History")
if st.session_state.expenses:
    df = pd.DataFrame(st.session_state.expenses)
    st.write(df)

    # Expense Summary
    st.subheader("📊 Expense Distribution")
    fig, ax = plt.subplots()
    df.groupby("Category")["Amount"].sum().plot(kind="pie", autopct="%1.1f%%", ax=ax)
    st.pyplot(fig)
else:
    st.info("No expenses recorded yet. Add your first expense in the sidebar!")

# Reset Button
if st.button("🔄 Reset Data"):
    st.session_state.expenses = []
    st.warning("All expenses cleared!")

