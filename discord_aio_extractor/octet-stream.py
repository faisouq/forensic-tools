from fileinput import filename
from importlib.metadata import files
import magic
import os
import shutil

pathToDir = input("Paste the discord cache directory: ")
directory = os.fsencode(pathToDir)

newDir = os.fsdecode(directory) + r"\! octet-stream"            
if os.path.exists(newDir):
    pass
else:
    os.makedirs(newDir)            

for file in os.listdir(directory):
    fileName = os.fsdecode(file)
    try:
        fileSignature = magic.from_file(f"{pathToDir}\\{fileName}", mime=True)
        # print(f"{pathToDir}\{fileName}: {fileSignature}")

        if fileSignature == 'application/octet-stream':
            print(f"{pathToDir}\{fileName}: {fileSignature}")
            shutil.copyfile(f'{pathToDir}\\{fileName}', f"{newDir}\\{fileName}.doc")

        # def fileSign():
        #     match fileSignature:
        #         case 'image/png':
        #             shutil.copyfile(f'{pathToDir}\\{fileName}', f"{newDir}\\{fileName}.png")
        #         case 'image/jpeg':
        #             shutil.copyfile(f'{pathToDir}\\{fileName}', f"{newDir}\\{fileName}.jpg")
        #         case 'video/mp4':
        #             shutil.copyfile(f'{pathToDir}\\{fileName}', f"{newDir}\\{fileName}.mp4")                    
        #         case 'image/webp':
        #             shutil.copyfile(f'{pathToDir}\\{fileName}', f"{newDir}\\{fileName}.webp")                    
        #         case 'image/gif':
        #             shutil.copyfile(f'{pathToDir}\\{fileName}', f"{newDir}\\{fileName}.gif") 
        # fileSign()                   
    except PermissionError:
        pass
