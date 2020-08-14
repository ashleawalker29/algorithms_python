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

def get_all_collection_cards():
    collection_worksheet_names = [worksheet_name for worksheet_name in get_worksheet_names()
                                  if 'Need' in worksheet_name]

    opened_collection_worksheets = [open_worksheet(collection_worksheet) for collection_worksheet
                                    in collection_worksheet_names]

    collection_data = [opened_collection_worksheet.get_all_records() for opened_collection_worksheet
                       in opened_collection_worksheets]

    card_data = []
    for data in collection_data:
        card_data.extend([row for row in data])

    return card_data
