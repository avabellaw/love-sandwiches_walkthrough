import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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
    
    while True:
        print("Please enter the number of sales for every sandwich.")
        print("Input each of the 6 numbers, seperated by commas.\nExample: 10, 20, 30, 40, 50, 60\n")
        
        figures_str = input("Enter the figures:")
        
        sales_data = figures_str.split(",")
        if validate_sales_data(sales_data):
            print("[Data is valid]\n")
            return sales_data
    
def validate_sales_data(values):
    """ 
    Checks list of values can be converted to integers, within a try,
    and that the number of values is 6
    """
    
    try:
        if(len(values) != 6):
            [int(value) for value in values]
            raise ValueError(
                f"Exactly 6 sales figures are required, you provided: {len(values)}"
                )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False
        
    return True
        
def update_sales_worksheet(sales_data):
    """
    Add inputted sales figure as a new row in sales worksheet.
    """
    print("Updating sales worksheet...\n")
    
    sales_wksht = SHEET.worksheet("sales")
    sales_wksht.append_row(sales_data)
    
    print("Sales figures added to worksheet successfully!\n")
   
def update_surplus_worksheet(surplus_data):
    """
    Add the calculated surplus into the surplus worksheet
    """
    print("Updating surplus worksheet...")
    
    surplus_wksht = SHEET.worksheet("surplus")
    surplus_wksht.append_row(surplus_data)
    print("Surplus worksheet updated successfully!")
     
def calculate_surplus(sales_data):
    """Calculate the difference between the stock and the sales"""
    print("Getting stock...")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    
    surplus = [int(stock_items) - sales_items for stock_items, sales_items in zip(stock_row, sales_data)]
    return surplus
    
def main():
    """
    Runs the programs functions
    """
    sales_data_str = get_sales_data()

    sales_data = [int(data) for data in sales_data_str]

    update_sales_worksheet(sales_data)
    surplus = calculate_surplus(sales_data)
    update_surplus_worksheet(surplus)
    
welcome_message = "Welcome to Love Sandwich's sales data automation system\n"
for i in range(len(welcome_message)):
    welcome_message += "-"
    
print(welcome_message)
    
main()