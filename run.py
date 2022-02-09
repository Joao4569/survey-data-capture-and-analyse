"""
Code below was sourced from Code Institutes "Love Sandwiches Walkthrough Project",
"Getting Set Up" course videos
"""

# Import gspread library in order to access and update data on spreadsheet.
import gspread

""" Import Credentials class from google-auth library
service account function in order to set up authentication needed to access Google Cloud"""
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

"""
End of code taken from Code Institutes "Love Sandwiches Walkthrough Project",
"Getting Set Up" course videos
"""

def capture_survey_data():
    """
    Instruct the user how to input data and allow the user to confirm their input.
    """
    # Instructions to user for required input.
    print(f"Please enter survey results below,\n")
    print("Only one rating between 0 and 10 for each of the four catergories,")
    print("each seperated by a comma. i.e. 4,5,6,7\n")

    while True:
        # Get user input as a string.
        survey_result_manual_input_str = input("Please enter ratings here: ")

        # Change user input string to a list.
        extracted_survey_results = survey_result_manual_input_str.split(",")

        # Confirm to user that input was correct and break while loop.
        if data_validator(extracted_survey_results):
            print("Valid entry accepted!")
            break

    return extracted_survey_results


def data_validator(user_values):
    """
    This will try to convert all string values into integers, check that all integers
    are betweeen 0 and 10 and also check if exactly 4 values were supplied. If any of
    these conditions are not met then specific ValueError's will be raised.
    """
    try:
        for user_value in user_values:

            # Check that all values provided are between 0 and 10.
            if int(user_value) > 0 and int(user_value) < 10:
                continue
            else:
                raise ValueError("One or more of your inputs was greater than 10 or less than 0, only values between 0 and 10 will be accepted")

        # Check that excatly 4 values are provided
        if len(user_values) != 4:
            raise ValueError(
                f"Four values are required, you only provided {len(user_values)}"
            )
    except ValueError as e:
        print(f"\nInvalid results supplied, {e}, please re-enter your results.\n")
        return False
 
    return True


verified_user_data = capture_survey_data()
print(verified_user_data)
