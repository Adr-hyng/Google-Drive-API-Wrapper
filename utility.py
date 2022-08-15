from msilib.schema import Directory


def parseDirectory(directory):
    return "{pathDir}".format(pathDir = directory).replace("\\","/")