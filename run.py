"""
Imported in order to allow clear screen and sleep functionality
Sourced from https://www.geeksforgeeks.org/clear-screen-python/
"""
from os import system, name
from time import sleep

# Code below was sourced from Code Institutes "Love Sandwiches Walkthrough
# Project", "Getting Set Up" course videos

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


def clear():
    """
    This is a function sourced from
    https://www.geeksforgeeks.org/clear-screen-python/ for clearing the
    terminal window.
    """
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def capture_survey_data():
    """
    This will instruct and capture user input
    and return validated survey ratings.
    """
    while True:
        # Instructions to user for required input.
        print("\n Please enter survey ratings below, as per the following"
              " instructions:\n")
        print(" Only 1 rating of between 0 - 10 for each of the four"
              " catergories,\n")
        print(" In the following order:\n\n         (Ease of use),"
              "(Design),(Features),(Overall Satisfaction)\n")
        print(" Each seperated by a comma and without any open spaces in-"
              "between. i.e. 6,7,5,8\n")

        # Get user input as a string.
        survey_result_manual_input_str = input("Please enter ratings here"
                                               " then press enter: \n")

        # Change user input string to a list.
        extracted_survey_results = survey_result_manual_input_str.split(",")

        # Confirm to user that input was correct and break while loop.
        if data_validator(extracted_survey_results, True):
            print(CGREEN + "\n Valid entry accepted!\n" + CEND)
            break

    return extracted_survey_results


def data_validator(user_values, capture_survey):
    """
    This will try to convert all string values into integers, check that all
    integers are betweeen 0 and 10 and also check if exactly 4 values were
    supplied. If any of these conditions are not met then specific
    ValueError's will be raised.
    """
    if capture_survey:
        min_value = 0
        max_value = 10
        amount_of_values = 4
    else:
        min_value = 1
        max_value = 2
        amount_of_values = 1
    try:
        for user_value in user_values:

            # Check that all values provided are between 0 and 10.
            if int(user_value) >= min_value and int(user_value) <= max_value:
                continue
            else:
                raise ValueError("One or more of your inputs was greater than"
                                 f" {max_value} or less\n than"
                                 f" {min_value}, only"
                                 f" values between {min_value}"
                                 f" and {max_value} will be accepted")

        # Check that correct amount of values are provided
        if len(user_values) != amount_of_values:
            raise ValueError(
                f"{amount_of_values} values are required, you provided"
                f" {len(user_values)}"
            )
    except ValueError as e:
        clear()
        print(CRED + f"\n Invalid value supplied, {e}, \n"
              " Please try again.\n" + CEND)
        return False

    return True


def allocate_survey_capture_number():
    """
    This will extract the last captured survey registry number and allocate
    the next consecutive number to the captured results
    """
    print(CYELLOW + " Allocating survey registry number....\n" + CEND)
    survey_register = SHEET.worksheet("Survey_Results").get_all_values()
    last_captured_rating = survey_register[-1][4]
    new_survey_capture_number = int(last_captured_rating) + 1
    return new_survey_capture_number


def update_survey_worksheet(survey_data):
    """
    Update survey worksheet by adding a new row to the worksheet
    with the validated data list inputed by the user.
    """
    print(CYELLOW + " Updating survey data to worksheet.....\n" + CEND)
    survey_worksheet = SHEET.worksheet("Survey_Results")
    survey_worksheet.append_row(survey_data)
    print(CGREEN + " Survey data captured successfully.\n" + CEND)
    print(" Returning to home screen.....")
    sleep(4)
    clear()
    main()


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

    clear()
    print(CBOLD + f"\n Out of {total_surveys} Surveys captured" + CEND)

    # Get ratings captured for each question in the survey
    for x in range(1, 5):
        question_data = summary_sheet.col_values(x)
        question = question_data.pop(0)
        ratings = question_data

        # Parse ratings and filter results for summary
        unsatisfied = 0
        satisfied = 0
        extremely_satisfied = 0
        for rating in ratings:
            if int(rating) >= 0 and int(rating) <= 3:
                unsatisfied += 1
            elif int(rating) >= 4 and int(rating) <= 7:
                satisfied += 1
            else:
                extremely_satisfied += 1

        print(CBOLD + f"\n {question}"
              ":\n" + CEND + f"\n {int((unsatisfied / total_surveys) * 100)}"
              "% Dissappointed (0 - 3) | "
              f"{int((satisfied / total_surveys) * 100)} % Pleased (4 - 7) | "
              f"{int((extremely_satisfied / total_surveys) * 100)}"
              "% Very Pleased (8 - 10)")

    input('\nPlease press the "Enter" key to return to home screen\n')
    clear()
    main()


def select_function():
    """
    ADD DOCSTRING
    """
    while True:
        print("\n Please select what you would like to do:\n"
              "\n 1) Capture a customer's survey\n"
              " 2) View a summary of survey results\n")
        user_selection = input("Please enter either 1 or 2, "
                               "then press enter: \n")
        if data_validator(user_selection, False):
            if user_selection == "1":
                clear()
                verified_user_data = capture_survey_data()
                survey_data = [int(score) for score in verified_user_data]
                survey_data.append(allocate_survey_capture_number())
                update_survey_worksheet(survey_data)
                break
            else:
                survey_summary_generator()
                break


def main():
    """
    Run all program functions
    """
    select_function()


print(CBOLD + "\n Welcome to Survey Data Processor\n" + CEND + "\n Please"
      " click on this terminal")
main()
