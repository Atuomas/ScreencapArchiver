from datetime import datetime
import os
import shutil

day = datetime.now()

#Check if there are any files in the specified location
def scChecker():
    path = '/Users/Tuomas/Desktop'
    extension = 'png'
    if any(file.endswith(extension) for file in os.listdir(path)):
        return True
    else:
        return False

#Checks if the folder with the same name (same day) has already been created
def folderExists():
    path = '/Users/Tuomas/Documents/Screenshots/' + day.strftime('%Y%m%d')
    exists = os.path.exists(path)
    return exists

#Creates folder with todays date as its name
def createFolder():
    path = '/Users/Tuomas/Documents/Screenshots/' + day.strftime('%Y%m%d')
    os.mkdir(path)

#Moves files to the specified directory/folder
def scMover():
    src = '/Users/Tuomas/Desktop'
    dest = '/Users/Tuomas/Documents/Screenshots/' + day.strftime('%Y%m%d')
    for file in os.listdir(src):
        if file.endswith('.png'):
            shutil.move(src + '/' + file, dest)
            continue
        else:
            pass
def main():
    if scChecker():
        if not folderExists():
            createFolder()
            scMover()
        else:
            scMover()
    else:
        pass

if __name__== "__main__":
    main()
