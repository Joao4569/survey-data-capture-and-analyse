"""
Code below was sourced from Code Institutes "Love Sandwiches Walkthrough
Project", "Getting Set Up" course videos
"""

# Import gspread library in order to access and update data on spreadsheet.
import gspread

# Import Credentials class for authentication.
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
    This will instruct and capture user input
    and return validated survey ratings.
    """
    # Instructions to user for required input.
    print("Please enter survey results below, as per the following"\
        "instructions:\n")
    print("Only one rating of between 0 and 10 for each of the four"\
        "catergories,")
    print("In the following order of catergories - (Ease of use),"\
        "(Design),(Features),(Overall Satisfaction).\n")
    print("Each seperated by a comma and without any spaces in"\
        "between. i.e. 6,7,5,8\n")

    while True:
        # Get user input as a string.
        survey_result_manual_input_str = input("Please enter ratings here: "\
                                            "(Ease of use),(Design),(Features),"\
                                            "(Overall Satisfaction)\n")

        # Change user input string to a list.
        extracted_survey_results = survey_result_manual_input_str.split(",")

        # Confirm to user that input was correct and break while loop.
        if data_validator(extracted_survey_results):
            print("Valid entry accepted!")
            break

    return extracted_survey_results


def data_validator(user_values):
    """
    This will try to convert all string values into integers, check that all
    integers are betweeen 0 and 10 and also check if exactly 4 values were
    supplied. If any of these conditions are not met then specific
    ValueError's will be raised.
    """
    try:
        for user_value in user_values:

            # Check that all values provided are between 0 and 10.
            if int(user_value) >= 0 and int(user_value) <= 10:
                continue
            else:
                raise ValueError("""One or more of your inputs was greater than
                                10 or less than 0, only values between 0 and 10
                                will be accepted""")

        # Check that excatly 4 values are provided
        if len(user_values) != 4:
            raise ValueError(
                f"""Four values are required, you only provided {len(user_values
                )}"""
            )
    except ValueError as e:
        print(f"""\nInvalid results supplied, {e}, \nplease re-enter your
            results.\n""")
        return False

    return True


def allocate_survey_capture_number():
    """
    This will extract the last captured survey registry number and allocate
    the next consecutive number to the captured results
    """
    print("Allocating survey registry number....")
    survey_register = SHEET.worksheet("Survey_Results").get_all_values()
    last_captured_rating = survey_register[-1][4]
    new_survey_capture_number = int(last_captured_rating) + 1
    return new_survey_capture_number


def update_survey_worksheet(survey_data):
    """
    Update survey worksheet by adding a new row to the worksheet
    with the validated data list inputed by the user.
    """
    print("Updating survey data to worksheet.....\n")
    survey_worksheet = SHEET.worksheet("Survey_Results")
    survey_worksheet.append_row(survey_data)
    print("Survey data captured successfully.\n")


def main():
    """
    Run all program functions
    """
    verified_user_data = capture_survey_data()
    survey_data = [int(score) for score in verified_user_data]
    survey_data.append(allocate_survey_capture_number())
    update_survey_worksheet(survey_data)


print("Welcome to Survey Data processor")
main()
