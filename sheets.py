import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import time 
import sys

 
def upload(users, urls, image_names, votes, winner_idx):
        dirname = time.strftime('%d-%m-%Y') 

        # use creds to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret_sheets.json', scope)
        client = gspread.authorize(creds)
 
        # Find a workbook by name and open the first sheet
        # Make sure you use the right name here.
        sheet = client.open("SAG-weekly-challenges")
	homesheet = sheet.sheet1
	row  = homesheet.find(dirname).row
	week = homesheet.cell(row, 1).value
	challenge = homesheet.cell(row, 4).value

	weeksheet = sheet.add_worksheet('Week {} Entries'.format(week), len(users)+3, 3)
	weeksheet.update_cell(1, 1, 'Week {}: {}'.format(week, challenge))
	weeksheet.update_cell(2, 1, 'User')
	weeksheet.update_cell(2, 2, 'Entry')
	weeksheet.update_cell(2, 3, 'Votes')

	for i in range(len(urls)):
		weeksheet.update_cell(i+3, 1, users[i].name)
		for j in range(len(image_names)):
			if users[i].name.startswith(image_names[j]):
				weeksheet.update_cell(i+3, 2, urls[j])
				break
		weeksheet.update_cell(i+3, 3, votes[i])

	weeksheet.update_cell(len(users)+3, 2, 'Total:')
	weeksheet.update_cell(len(users)+3, 3, sum(votes))

	homesheet.update_cell(row, 6, len(users))
	homesheet.update_cell(row, 7, sum(votes))
	homesheet.update_cell(row, 8, users[winner_idx].name)
	for j in range(len(image_names)):
		if users[winner_idx].name.startswith(image_names[j]):
			homesheet.update_cell(row, 9, urls[j])
			break
