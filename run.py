import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")

SCOPED_CREDS = CREDS.with_scopes(SCOPE)

GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():
    """
    Get sales data from the user
    """
    print("Please enter the number of sales for every sandwich.")
    print("Input each of the 6 numbers, seperated by commas.\nExample: 10, 20, 30, 40, 50, 60\n")
    
    figures_str = input("Enter the figures:")
    print(f"Figures received: {figures_str}")

get_sales_data()