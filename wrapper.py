# Google OAuth 2.0 and OAuth consent screen

# authetication to google api services
# create oauth client secret file

# https://console.cloud.google.com/

# pip install pydrive

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import mimetypes

class GoogleDriveWrapper:
    def __init__(self):
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth
        self.drive = GoogleDrive(gauth)
        
    def createFolder(self, parentFolderID: str, dir_name: str) -> str:
        drive_folder = self.drive.CreateFile({
        'parents' : [{'id' : parentFolderID}],
        'title': dir_name,
        "mimeType": "application/vnd.google-apps.folder"
        })
        drive_folder.Upload()
        return drive_folder.get("id")
    
    def uploadFile(self, parentFolderID: str, fileDirectory: str):
        fileName = fileDirectory.split("/")[-1]
        _file = self.drive.CreateFile({'parents' : [{'id' : parentFolderID}], 'title' : fileName})
        _file.SetContentFile(fileDirectory)
        _file.Upload()
        
    def uploadFolder(self, rootDirectory: str, parentFolderID: str):
        dir_name = rootDirectory.split("/")[-1]
        directoryName = dir_name.split("\\")[-1]
        gdrive_folder = self.drive.CreateFile({
            'parents' : [{'id' : parentFolderID}],
            'title': directoryName,
            "mimeType": "application/vnd.google-apps.folder"
        })
        gdrive_folder.Upload()
        gdrive_folder_id = gdrive_folder['id']
        files = os.listdir(rootDirectory)
        for _file in files:
            full_name = os.path.join(rootDirectory, _file)
            print("Backing up {}".format(full_name))
            mime_type = mimetypes.guess_type(full_name)[0]
            if os.path.isfile(full_name):
                f = self.drive.CreateFile({ 
                    'title': _file, 
                    "parents": [{ "id": gdrive_folder_id }],
                    'mimeType': mime_type})
                f.SetContentFile(full_name)
                f.Upload()
            else:
                self.uploadFolder(full_name, gdrive_folder_id)
        print("Directory: {} backed up successfully".format(rootDirectory))
        
    def traverseDirectory(self, parentFolderID: str = "", parentName: str = "Root"):
        query = f"\'{parentFolderID}\' in parents and trashed=false"
        file_list = self.drive.ListFile({'q': query}).GetList()
        directoryName = ""
        parent = parentName
        for counter, file1 in enumerate(file_list):
            if file1['title'].endswith("."+file1['title'].split('.')[-1]):
                current = "file"
            elif file1['title'].endswith(file1['title'].split('.')[-1]):
                current = "folder"
                parent = file1['title']
                directoryName = parentName + '/' + parent
            p_type = parent if current == "file" else directoryName
            print('>> Gdrive/: %s' % (f"{p_type}{'/' + file1['title'] if current == 'file' else ''}"))
            self.traverseDirectory(file1['id'], directoryName)
    
    def getFolders(self, parentFolderID: str, maxResults: int = 30) -> list[dict]:
        folderData = []
        query = f"\'{parentFolderID}\' in parents and trashed=false"
        for file_list in self.drive.ListFile({'q': query, 'maxResults': maxResults}):
            print('Received %s files from Files.list()' % len(file_list)) # <= 10
            for file1 in file_list:
                folderData.append(file1)
                print('title: %s, id: %s' % (file1['title'], file1['id']))
        return folderData