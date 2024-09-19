import calendar
from datetime import datetime
import streamlit as st
from streamlit_option_menu import option_menu
import database as db
from create_sankey_chart import create_sankey_chart

# -------------- SETTINGS --------------
incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car", "Other Expenses", "Saving"]
currency = "USD"
page_title = "Income and Expense Tracker"
page_icon = ":money_with_wings:"
layout = "centered"
# --------------------------------------

st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(page_title + " " + page_icon)


# --- SIDEBAR SECTION ---
st.sidebar.title("App Information")
st.sidebar.info("""
**Income and Expense Tracker** helps you keep track of your finances by recording your income and expenses. You can easily visualize the data for better financial planning.
""")


st.sidebar.title("Usage Instructions")
st.sidebar.write("""
1. **Data Entry**: Select the 'Data Entry' option to input your monthly income and expenses.
2. **Data Visualization**: Use the 'Data Visualization' option to see a graphical breakdown of your income and expenses for the selected period.
""")

st.sidebar.markdown("### Contact Me")
st.sidebar.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/AkramUllahKhan)")
st.sidebar.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:akramullahkhan05@gmail.com)")
st.sidebar.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/akram-ullah-97122014b/)")



# --- DROP DOWN VALUES FOR SELECTING THE PERIOD ---
years = [datetime.today().year, datetime.today().year + 1]
months = list(calendar.month_name[1:])

def get_all_periods():
    """Fetch all periods and return a list of unique periods"""
    items = db.fetch_all_periods()
    return items


# --- HIDE STREAMLIT STYLE ---
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- NAVIGATION MENU ---
selected = option_menu(
    menu_title=None,
    options=["Data Entry", "Data Visualization"],
    icons=["pencil-fill", "bar-chart-fill"],
    orientation="horizontal",
)

# --- INPUT & SAVE PERIODS ---
if selected == "Data Entry":
    st.header(f"Data Entry in {currency}")
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        month = col1.selectbox("Select Month:", months, key="month")
        year = col2.selectbox("Select Year:", years, key="year")

        "---"
        with st.expander("Income"):
            for income in incomes:
                st.number_input(f"{income}:", min_value=0, format="%i", step=10, key=income)
        with st.expander("Expenses"):
            for expense in expenses:
                st.number_input(f"{expense}:", min_value=0, format="%i", step=10, key=expense)
        with st.expander("Comment"):
            comment = st.text_area("", placeholder="Enter a comment here ...")

        "---"
        submitted = st.form_submit_button("Save Data")
        if submitted:
            period = f"{year}_{month}"
            incomes_dict = {income: st.session_state[income] for income in incomes}
            expenses_dict = {expense: st.session_state[expense] for expense in expenses}
            db.insert_period(period, incomes_dict, expenses_dict, comment)
            st.success("Data saved!")

# --- PLOT PERIODS ---
if selected == "Data Visualization":
    st.header("Data Visualization")
    with st.form("saved_periods"):
        period = st.selectbox("Select Period:", get_all_periods())
        submitted = st.form_submit_button("Plot Period")
        if submitted:
            # Get data from database
            period_data = db.get_period(period)
            if period_data:
                comment = period_data.get("comment", "")
                expenses_data = period_data.get("expenses", {})
                incomes_data = period_data.get("incomes", {})

                # Create metrics
                total_income = sum(incomes_data.values())
                total_expense = sum(expenses_data.values())
                remaining_budget = total_income - total_expense
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Income", f"{total_income} {currency}")
                col2.metric("Total Expense", f"{total_expense} {currency}")
                col3.metric("Remaining Budget", f"{remaining_budget} {currency}")
                st.text(f"Comment: {comment}")

                # Create Sankey chart
                fig = create_sankey_chart(incomes_data, expenses_data)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.error("No data found for the selected period.")

# --- FOOTER ---
st.markdown("""
    <footer style="
        text-align: center; 
        padding: 20px; 
        font-size: 14px; 
        color: #FAFAFA; /* Matches the textColor in config.toml */
        background-color: #0E1117; /* Matches the backgroundColor in config.toml */
        border-top: 1px solid #262730; /* Matches the secondaryBackgroundColor in config.toml */
        margin-top: 30px; 
        position: relative; 
        bottom: 0; 
        width: 100%;
    ">
        <p style="margin: 0; font-family: 'sans-serif';">Made with ❤️ by <strong>Akram Ullah</strong></p>
        <p style="margin: 5px 0 0; font-size: 12px; color: #FAFAFA; font-family: 'sans-serif';">
            For any inquiries, contact me at <a href="mailto:akramullahkhan05@gmail.com" style="color: #FC4BFF;">akramullahkhan05@gmail.com</a>
        </p>
    </footer>
    """, unsafe_allow_html=True)
