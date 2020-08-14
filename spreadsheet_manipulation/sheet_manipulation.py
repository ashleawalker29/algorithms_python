import gspread
from google.oauth2.service_account import Credentials

SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDENTIALS = Credentials.from_service_account_file('superuser_secret.json', scopes=SCOPES)
CLIENT = gspread.authorize(CREDENTIALS)

SHEET_NAME = 'AC Amiibo Cards Trading'
SHEET = CLIENT.open(SHEET_NAME)


def get_worksheet_names():
    return [worksheet.title for worksheet in SHEET.worksheets()]

def open_worksheet(worksheet_name):
    return SHEET.worksheet(worksheet_name)

def get_all_keys(worksheet):
    return worksheet.row_values(1)

def get_all_needed_cards(worksheet):
    worksheet_data = worksheet.get_all_records()

    return [data for data in [row for row in worksheet_data] if data['Need']]
