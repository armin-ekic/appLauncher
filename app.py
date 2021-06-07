""""This will be used to run the main functionality of the program"""

#used to navigate the file system and find the relevant directories, also to display relevant messages
from navigate import Nav

#used to list/change directories, and perform other functions directly on the file system
import os


#main function to take user input and launch applications
def main():
    while True:
        #take user input for desired directory and store it for Nav instance _nav
        userIn = input("Which directory would you like to open? \n"
                       "For assistance, type \"help\". \n"
                       "For a list of possible directories, type \"list\". \n")
        _nav = Nav(userIn)

        #we are doing this assuming that the user doesn't input and invalid directory
        #depending on user input, display a help message, if help isn't needed then skip
        while _nav.chosenDir == "help" or _nav.chosenDir == "list":
            if _nav.chosenDir == "help":
                _nav.infoMessages(help = True)
                _nav.chosenDir = input("")
            if _nav.chosenDir == "list":
                _nav.infoMessages(list = True)
                _nav.chosenDir = input("")

        #navigate the user to the desired directory
        os.chdir("C:\\Users\\aekic\\Desktop\\" + _nav.chosenDir)

        #take user input for the desired app to open and store it in Nav instance _app
        appLaunch = input("Which app would you like to open? \n"
                          "For a list of apps available, type \"app list\". \n")
        _app = Nav(appLaunch)

        #if more information is needed, display it
        while _app.chosenDir == "app list":
            _app.infoMessages(_nav.chosenDir, appList = True)
            _app.chosenDir = input("\n")

        #append the appropriate file type (assuming game shortcut) and launch
        _app.chosenDir = _app.chosenDir + ".lnk"
        os.startfile("C:\\Users\\aekic\\Desktop\\" + _nav.chosenDir + "\\" + _app.chosenDir)

        #end the script
        break