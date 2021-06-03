""""This will be used to find the relevant directory we wish to launch our apps from"""

import os


class Nav():

    def __init__(self,chosenDir):
        self.chosenDir = chosenDir

    def infoMessages(self, help = False, list = False):
        if help:
            print("Choose a folder in the Desktop directory to look into. \n"
                  "Type \"list\" to see all the directories in the Desktop.")
        if list:
            print("The list of directories to choose from is as follows: \n")
            directories = os.listdir("C:\\Users\\aekic\\Desktop")
            for x in range(len(directories)):
                if "." in directories[x]:
                    continue
                else:
                    print(directories[x])