import gspread
import pprint
from oauth2client.service_account import ServiceAccountCredentials

pp = pprint.PrettyPrinter()

# use creds to create a client to interact with API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# find a workbook by name and open the first sheet
sheet = client.open('SAG-weekly-challenges').sheet1

# extract and print values
list_of_hashes = sheet.get_all_records()
pp.pprint(list_of_hashes)

