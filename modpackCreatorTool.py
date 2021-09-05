import time, sys, subprocess
print("MMM is now loading...")
time.sleep(1)

def modpackMaker():
    print("Before you can make your modpack, you need to answer a few questions...")
    forgeInstalled = input("This is a modpack creator for Minecraft 1.16.5 running the Forge client. Do you have Minecraft Forge 1.16.5 installed on this device? ")
    if forgeInstalled != "yes":
        print("You need Minecraft Forge to use this tool! Come back once you have it")
        time.sleep(2)
        sys.exit()
    modsReady = input("Do you have all your mods in the Minecraft mods folder ready to be put in your modpack? ")
    if modsReady != "yes":
        print("You need to place all the mods you want to use in your mods folder! Come back once you've done that")
        time.sleep(2)
        sys.exit()
    print("\n\nPlease wait... Creating modpack...")
    time.sleep(0.5)
    print("Copying mods folder to MODPACK directory...")
    subprocess.call('copyFiles.bat')

print("Welcome to MMM (Minecraft Modpack Maker) This program will guide you through making your own modpack!")
yesOrNo = input("Would you like to make a modpack today? (type yes or no) ")
if yesOrNo == "yes":
    proceed = True
    modpackMaker()
if yesOrNo == "no":
    proceed = False
    print("Come back soon to make your own modpack!")
    time.sleep(1)