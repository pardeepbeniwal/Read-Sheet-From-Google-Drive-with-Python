import gspread
from oauth2client.service_account import ServiceAccountCredentials

SCOPES = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
SPREADSHEET_URL = 'file_url_here'
CREDENTIAL_JSON = 'json file provided by google while create project'

creds = ServiceAccountCredentials.from_json_keyfile_name(
                CREDENTIAL_JSON, SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_url(SPREADSHEET_URL).sheet1
list_of_hashes = sheet.get_all_records()
