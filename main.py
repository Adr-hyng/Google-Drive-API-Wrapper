from wrapper import GoogleDriveWrapper
from utility import parseDirectory

if __name__ == "__main__":
    folderID = YOUR_FOLDER_ID
    directory = parseDirectory(r"PATH/TO/UPLOAD")
    drive = GoogleDriveWrapper()
    drive.uploadFolder(directory, folderID)