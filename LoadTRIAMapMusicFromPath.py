import os, shutil

success = "done, enjoy playing whatever map you are about to play! :D"
rootDir = "C:\Program Files (x86)\Roblox\Versions"

print("this thing only works in windows D:")
print("if roblox updates on the next play then you might want to run this tool again")

soundPath = input("enter the path to the sound file (or drag and drop the music file into this window): ")
soundPath = soundPath.replace("\"","")
while not os.path.exists(soundPath):
    soundPath = input("invalid path, re-enter the path to the sound file: ")
mother, son = os.path.split(soundPath)

for subdir, dirs, files in os.walk(rootDir):
    for file in files:
        filename = os.fsdecode(file)
        if filename == "RobloxPlayerBeta.exe":
            print(subdir+"\\content\\sounds\\MapMusic\\"+son)
            if not os.path.exists(subdir+"\\content\\sounds\\MapMusic"):
                os.mkdir(subdir+"\\content\\sounds\\MapMusic")
                shutil.copy2(soundPath, subdir+"\\content\\sounds\\MapMusic")
                print(success)
            else:
                if os.path.exists(subdir+"\\content\\sounds\\MapMusic\\"+son):
                    print("given sound file is already present in MapMusic folder, go play the map already >:]")
                else:
                    shutil.copy2(soundPath, subdir+"\\content\\sounds\\MapMusic")
                    print(success)