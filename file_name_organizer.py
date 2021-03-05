import os
from pathlib import Path

"""
Runs a script that puts screenshots into the "Screenshots" folder. Maybe implement date sorting?
"""

SUBDIRECTORIES = {
    "SPREADSHEETS": ['.xlsx']

}

#For checking what suffix a file item has and returning the correct Category that type of suffix belongs to. 
#Useful if I want to move many types of file extensions to one type of folder.
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
        #Find the directory path of each item using pathlib
        filePath = Path(items)
        
        #For debugging:
        print(filePath.name)

        #Skip if items is a directory.
        if items.is_dir():
            continue

        #Skip if the file for this script is found
        if filePath.name == "file_name_organizer.py":
            continue

        #Find the file's suffix using .suffix()
        #Useful if you want to sort via file extension.
        fileSuffix = filePath.suffix.lower()
        
        #Make new directory paths:
        cleanDirectory = Path("CLEAN SLIDES")
        spreadsheetDirectory = Path("SPREADSHEETS")

        if cleanDirectory.is_dir() != True:
            cleanDirectory.mkdir()

        if spreadsheetDirectory.is_dir() != True:
            spreadsheetDirectory.mkdir()

        #Moving the files
        #put all files with "clean" in their names in the cleanDirectory filepath.
        if "clean" in filePath.name:
            filePath.rename(cleanDirectory.joinpath(filePath))

        #Put all files with suffix .xlsx into the SPREADSHEETS folder
        if ".xlsx" == fileSuffix:
            filePath.rename(spreadsheetDirectory.joinpath(filePath))

#Call funciton to organize the dir.
organizeDir()

