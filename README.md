# Income and Expense Tracker

## Overview

The **Income and Expense Tracker** is a web application developed using Streamlit to help users manage and visualize their personal finances. This application allows you to record your income and expenses, and provides interactive charts to analyze financial data.

## Features

- **Data Entry:** Input income and expenses for various categories.
- **Data Visualization:** View financial data through interactive charts.
- **Period Selection:** Choose different periods to analyze your financial data.
- **Responsive Footer:** Contact information and app creator details at the footer.
- **Professional Sidebar:** Contains app information and contact details with social media links.

## Technologies Used

- **Streamlit:** For building the interactive web application.
- **Pandas:** For data manipulation.
- **Plotly:** For data visualization.
- **MongoDB Atlas:** For cloud-based database storage.

## Setup and Installation

### Prerequisites

- Python 3.7 or later
- MongoDB Atlas account
- Necessary Python packages (listed in `requirements.txt`)

### Installation Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AkramUllahKhan/income-expense-tracker-streamlit.git
   cd income-expense-tracker-streamlit
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Required Packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Database Connection:**

   Update the `database.py` file with your MongoDB Atlas connection string and credentials.

5. **Run the Application:**

   ```bash
   streamlit run app.py
   ```

6. **Access the Application:**

   Open your web browser and navigate to `http://localhost:8501`.

## Usage

- **Data Entry:** Navigate to the "Data Entry" section to input your income and expenses.
- **Data Visualization:** Navigate to the "Data Visualization" section to select a period and view the data.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. For any major changes, please open an issue first to discuss what you would like to change.

## Contact

For any inquiries, contact me at [akramullahkhan05@gmail.com](mailto:akramullahkhan05@gmail.com) or connect with me on [GitHub](https://github.com/AkramUllahKhan) and [LinkedIn](https://www.linkedin.com/in/akram-ullah-97122014b/).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```