""""This will be used to run the main functionality of the program"""

from navigate import Nav

import os


def main():
    userIn = input("Which directory would you like to open? \n"
                   "For assistance, type \"help\" \n"
                   "For a list of possible directories, type \"list\" \n")
    _nav = Nav(userIn)
    #we are doing this assuming that the user doesn't input and invalid directory
    while _nav.chosenDir == "help" or _nav.chosenDir == "list":
        if _nav.chosenDir == "help":
            _nav.infoMessages(help = True)
            _nav.chosenDir = input("")
        if _nav.chosenDir == "list":
            _nav.infoMessages(list = True)
            _nav.chosenDir = input("")
    os.chdir("C:\\Users\\aekic\\Desktop\\" + _nav.chosenDir)