""" All code below up until line *** was sourced from Code Institutes "Love Sandwiches Walkthrough Project",
"Getting Set Up" course videos"""

# Import gspread library in order to access and update data on spreadsheet
import gspread

# Import Credentials class from google-auth library, service account function in order to set up authentication needed to access Google Cloud
from google.oauth2.service_account import Credentials

# Write your code to expect a terminal of 80 characters wide and 24 rows high

# Scope constant for IAM
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('survey_data_capture_sheet')

survey = SHEET.worksheet('Survey_Results')

data = survey.get_all_values()

print(data)

