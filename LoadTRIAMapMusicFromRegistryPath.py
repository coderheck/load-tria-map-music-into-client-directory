import os, shutil, winreg

success = "done, enjoy playing whatever map you are about to play! :D"
robloxPath = None

print("this thing only works in windows D:")
print("if roblox updates on the next play then you might want to run this tool again")

robloxShellKey = r'HKEY_CLASSES_ROOT\\roblox-player\\shell\\open\\command'
hkcr = winreg.HKEY_CLASSES_ROOT
robloxRegistry = winreg.OpenKeyEx(hkcr, r'roblox-player\shell\\open\\command')
if robloxRegistry:
	robloxPath = winreg.QueryValueEx(robloxRegistry, "")[0]
robloxPath = robloxPath.replace("\"","")
robloxPath = robloxPath.replace("%1","")
robloxPath = os.path.split(robloxPath)[0]

choice = input("pick loading option ('1' for singular audio file, '2' for sound folder): ")
while choice != "1" and choice != "2":
	choice = input("i hereby implore you to pick a valid loading option ('1' for singular audio file, '2' for sound folder): ")

if choice == "1":

	soundPath = input("enter the path to the sound file (or drag and drop the music file into this window): ")
	soundPath = soundPath.replace("\"","")
	while not os.path.exists(soundPath):
		soundPath = input("invalid path, re-enter the path to the sound file: ")
	soundFilename = os.path.split(soundPath)[1]

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
	
elif choice == "2":

	soundFolder = input("enter the path to the sounds folder (or drag and drop the folder into this window): ")
	soundFolder = soundFolder.replace("\"","")
	while not os.path.exists(soundFolder):
		soundFolder = input("invalid path, re-enter the path to the sound file: ")
	
	mergeOption = input("pick folder merging option ('3' to overwrite, '4' to merge folders): ")
	while mergeOption != "3" and mergeOption != "4":
		mergeOption = input("i hereby implore you to pick a valid folder merging option ('3' to overwrite, '4' to merge folders): ")
	
	if mergeOption == "3":
		if not os.path.exists(robloxPath+"\\content\\sounds\\MapMusic"):
			os.mkdir(robloxPath+"\\content\\sounds\\MapMusic")
		shutil.copytree(soundFolder, robloxPath+"\\content\\sounds\\MapMusic",False,None)
		print(success)
	elif mergeOption == "4":
		if os.path.exists(robloxPath+"\\content\\sounds\\MapMusic\\"+soundFolder):
			print("given sound file is already present in MapMusic folder, go play the map already >:]")
		else:
			shutil.copytree(soundFolder, robloxPath+"\\content\\sounds\\MapMusic",False,None)
			print(success)