""" All code below up until line 22 was sourced from Code Institutes "Love Sandwiches Walkthrough Project",
"Getting Set Up" course videos"""

# Import gspread library in order to access and update data on spreadsheet.
import gspread

# Import Credentials class from google-auth library, service account function in order to set up authentication needed to access Google Cloud.
from google.oauth2.service_account import Credentials

# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Scope constant for IAM.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('survey_data_capture_sheet')


def capture_survey_data():
    """
    Capture user inputed survey data from terminal input.
    """
    # Instructions to user for required input.
    print(f"Please enter survey results below,\n")
    print("Only one rating between 0 and 10 for each of the four catergories,")
    print("each seperated by a comma. i.e. 4,5,6,7\n")

    # Get user input as a string.
    survey_result_manual_input_str = input("Please enter ratings here: ")

    # Change user input string to a list.
    extracted_survey_results = survey_result_manual_input_str.split(",")

    print(survey_result_manual_input_str)

    # print(f"\nThe ratings provided were {survey_result_manual_input_str}\n")

    # confirm_result_manual_input_str = input("Are these correct? 'y' for Yes and 'n' for No:  ")
    # if confirm_result_manual_input_str.lower() == "y":
    #     print("yes")
    # else:
    #     capture_survey_data()


capture_survey_data()
