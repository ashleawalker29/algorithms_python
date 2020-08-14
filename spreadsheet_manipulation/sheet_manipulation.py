import gspread
from google.oauth2.service_account import Credentials

SCOPES = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
CREDENTIALS = Credentials.from_service_account_file('superuser_secret.json', scopes=SCOPES)
CLIENT = gspread.authorize(CREDENTIALS)

SHEET_NAME = 'AC Amiibo Cards Trading'
SHEET = CLIENT.open(SHEET_NAME)


def get_worksheet_names():
    return [worksheet.title for worksheet in SHEET.worksheets()]
