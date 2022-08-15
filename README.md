# GOOGLE DRIVE API WRAPPER

This adds a little functionality to ease the process of doing ```File Uploads, Folder Uploads, Get Data, Traverse Drive File System```. This can also be a backup system to the Google Drive, if you want to backup some files easily to the Google Drive. This can also help future projects about using Google Drive API since it's a wrapper.

<br></br>

# EXAMPLES

## Upload Folder Example:
```py 
# Can be found here: 
# https://drive.google.com/drive/u/0/folders/<ID>

folderID = <yourFolderID>
directory = parseDirectory(r"path/to/upload")
drive = GoogleDriveWrapper()
drive.uploadFolder(directory, folderID)
```


## Upload File Example:
```py 
# Can be found here: 
# https://drive.google.com/drive/u/0/folders/<ID>

folderID = <yourFolderID>
directory = parseDirectory(r"path/to/upload")
drive = GoogleDriveWrapper()
drive.uploadFile(folderID, directory)
```

<br></br>

# INSTALLATIONS (WIP)

1. Clone this Repository to your workspace.


<br></br>


# README (WIP)

<br></br>

# More Info

### [Requirements](./requirements.txt)
### [License](./license.md)