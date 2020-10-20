import os
from pathlib import Path

"""
Runs a script that sorts files by their file types. Puts them into either a Documents, Audio, Videos,
Images, or a MISC folder. 
"""

SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf','.rtf','.txt'],
    "AUDIO": ['.m4a','.m4b','.mp3'],
    "VIDEOS": ['.mov','.avi','.mp4'],
    "IMAGES": ['.jpg','.jpeg','.png']
}

"""
Returns a category based on the file suffix (eg: .pdf will return DOCUMENTS)
.mov will return VIDEOS
"""
def pickDirectory(value):
    #Loop through all items in the dictionary.
    #.items() returns a list of tuples containing all key-value pairs in the dict.
    for category, suffixes in SUBDIRECTORIES.items():
        
        #Loop through file suffixes, found in the second element of each tuple.
        for suffix in suffixes:
            
            #If a suffix matches the passed value, return the category of that suffix.
            if suffix == value:
                return category

    #If no suffixes get matched, return MISC.
    #This means that when no 
    return "MISC"
#Test:
#print(pickDirectory(".pdf"))

"""
Loop through every file in the working directory.
"""
def organizeDir():
    
    #Loop through all items returned by .scandir(), which gives us the path names of all files.
    for items in os.scandir():

        #Skip if items is a directory.
        if items.is_dir():
            continue

        #Find the directory path of each item using pathlib
        filePath = Path(items)

        #Find the file's suffix using .suffix()
        fileSuffix = filePath.suffix.lower()

        #Use pickDirectory funcion to determine directory name.
        directory = pickDirectory(fileSuffix)

        #Cast directory to path type.
        directoryPath = Path(directory)

        #If the directrroy path does not exist, make a new dir.
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        
        #Move the file to its respective directory.
        #Done by renaming the filepath to include new folder.
        #For more info: https://docs.python.org/3/library/pathlib.html 
        filePath.rename(directoryPath.joinpath(filePath))

#Call funciton to organize the dir.
organizeDir()

