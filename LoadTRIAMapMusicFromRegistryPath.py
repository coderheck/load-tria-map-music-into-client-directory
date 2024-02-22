import os, shutil, winreg

success = "done, enjoy playing whatever map you are about to play! :D"
robloxPath = None

print("this thing only works in windows D:")
print("if roblox updates on the next play then you might want to run this tool again")

soundPath = input("enter the path to the sound file (or drag and drop the music file into this window): ")
soundPath = soundPath.replace("\"","")
while not os.path.exists(soundPath):
    soundPath = input("invalid path, re-enter the path to the sound file: ")
soundFilename = os.path.split(soundPath)[1]

robloxShellKey = r'HKEY_CLASSES_ROOT\\roblox-player\\shell\\open\\command'
hkcr = winreg.HKEY_CLASSES_ROOT
robloxRegistry = winreg.OpenKeyEx(hkcr, r'roblox-player\shell\\open\\command')
if robloxRegistry:
    robloxPath = winreg.QueryValueEx(robloxRegistry, "")[0]
robloxPath = robloxPath.replace("\"","")
robloxPath = robloxPath.replace("%1","")
robloxPath = os.path.split(robloxPath)[0]
if not os.path.exists(robloxPath+"\\content\\sounds\\MapMusic"):
    os.mkdir(robloxPath+"\\content\\sounds\\MapMusic")
    shutil.copy2(soundPath, robloxPath+"\\content\\sounds\\MapMusic")
    print(success)
else:
    if os.path.exists(robloxPath+"\\content\\sounds\\MapMusic\\"+soundFilename):
        print("given sound file is already present in MapMusic folder, go play the map already >:]")
    else:
        shutil.copy2(soundPath, robloxPath+"\\content\\sounds\\MapMusic")
        print(success)