"""
Code below was sourced from Code Institutes "Love Sandwiches Walkthrough
Project", "Getting Set Up" course videos
"""

# Import gspread library in order to access and update data on spreadsheet.
import gspread

# Import Credentials class for authentication.
from google.oauth2.service_account import Credentials

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

# Code taken from https://lycaeum.dev/en/questions/287871, credited in README.
CRED = '\033[91m'
CGREEN = '\33[32m'
CYELLOW = '\33[33m'
CBOLD = '\33[1m'
CEND = '\033[0m'


def capture_survey_data():
    """
    This will instruct and capture user input
    and return validated survey ratings.
    """
    while True:
        # Instructions to user for required input.
        print("Please enter survey ratings below, as per the following"
              " instructions:\n")
        print("Only one rating of between 0 and 10 for each of the four"
              " catergories,\n")
        print("In the following order of catergories - \n(Ease of use),"
              "(Design),(Features),(Overall Satisfaction).\n")
        print("Each seperated by a comma and without any spaces in"
              "between. i.e. 6,7,5,8\n")

        # Get user input as a string.
        survey_result_manual_input_str = input("Please enter ratings here: \n")

        # Change user input string to a list.
        extracted_survey_results = survey_result_manual_input_str.split(",")

        # Confirm to user that input was correct and break while loop.
        if data_validator(extracted_survey_results):
            print(CGREEN + "Valid entry accepted!\n" + CEND)
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
                raise ValueError("One or more of your inputs was greater than"
                                 " 10 or less than 0, only values between 0"
                                 "and 10 will be accepted")

        # Check that excatly 4 values are provided
        if len(user_values) != 4:
            raise ValueError(
                "4 values are required, you only provided"
                f" {len(user_values)}"
            )
    except ValueError as e:
        print(CRED + f"\nInvalid ratings supplied, {e}, \n"
              "Please try again.\n" + CEND)
        return False

    return True


def allocate_survey_capture_number():
    """
    This will extract the last captured survey registry number and allocate
    the next consecutive number to the captured results
    """
    print(CYELLOW + "Allocating survey registry number....\n" + CEND)
    survey_register = SHEET.worksheet("Survey_Results").get_all_values()
    last_captured_rating = survey_register[-1][4]
    new_survey_capture_number = int(last_captured_rating) + 1
    return new_survey_capture_number


def update_survey_worksheet(survey_data):
    """
    Update survey worksheet by adding a new row to the worksheet
    with the validated data list inputed by the user.
    """
    print(CYELLOW + "Updating survey data to worksheet.....\n" + CEND)
    survey_worksheet = SHEET.worksheet("Survey_Results")
    survey_worksheet.append_row(survey_data)
    print(CGREEN + "Survey data captured successfully.\n" + CEND)


def survey_summary_generator():
    """
    This will extract all the ratings captured by question and
    filter through them in order to generate a summary of
    customer satisfaction.
    """
    # Store sheet in a variable
    summary_sheet = SHEET.worksheet("Survey_Results")

    # Get all data from captured surveys
    all_survey_data = summary_sheet.get_all_values()

    # Get total number of surveys captured
    total_surveys = int(all_survey_data[-1][-1])

    print(total_surveys)
    print(all_survey_data)

    # Get ratings captured for each question in the survey
    for x in range(1, 5):
        question_data = summary_sheet.col_values(x)
        question = question_data.pop(0)
        ratings = question_data
        print(f"{question} :\n")

        # Parse ratings and filter results for summary
        poor = 0
        average = 0
        excellent = 0
        for rating in ratings:
            if int(rating) >= 0 and int(rating) <= 3:
                poor += 1
            elif int(rating) >= 4 and int(rating) <= 7:
                average += 1
            else:
                excellent += 1
        print(f"Poor = {int((poor / total_surveys) * 100)}%\n"
              f"Average = {int((average / total_surveys) * 100)}%\n"
              f"Excellent = {int((excellent / total_surveys) * 100)}%\n")



def main():
    """
    Run all program functions
    """
    verified_user_data = capture_survey_data()
    survey_data = [int(score) for score in verified_user_data]
    survey_data.append(allocate_survey_capture_number())
    update_survey_worksheet(survey_data)


# print(CBOLD + "\nWelcome to Survey Data processor\n" + CEND)
# main()
survey_summary_generator()
