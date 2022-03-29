import os

pathToDir = input("Paste the discord cache directory: ")


os.system(
    f'.\ChromeCacheView.exe -folder {pathToDir} /copycache "" "application/json" /CopyFilesFolder "! Cache Output" /UseWebSiteDirStructure 1'
)
# os.system(f'.\ChromeCacheView.exe -folder {pathToDir} /copycache "" "image/gif" /CopyFilesFolder "! Cache Output Images 3" /UseWebSiteDirStructure 1')

# -folder {directory} /stext c:\output.txt
