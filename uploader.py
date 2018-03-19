import pprint as pp
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from os import listdir
import time

def upload():
	gauth = GoogleAuth()
	gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.

	drive = GoogleDrive(gauth)

	images_ID = '1IK4vQNnh7cA6Xnin1WRrzIOhGsAOk-4q' # ID for "root" folder
	weekly_folder_name  = time.strftime('%d-%m-%Y') 

	folder = drive.CreateFile({'title': weekly_folder_name, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [{'id': images_ID}]}) # create a folder named 'dd-mm-YYYY' in /images/ 
	folder.Upload()

	weekly_folder_dir = './images/'+weekly_folder_name+'/' # look for all local files in /images/dd-mm-YYYY
	for f in listdir(weekly_folder_dir):
		temp = drive.CreateFile({'title': str(f), 'parents': [{'id': folder['id']}]}) # upload each image in the newly created folder 
		temp.SetContentFile(weekly_folder_dir+str(f)) 
		temp.Upload()
	
	return folder['alternateLink']
