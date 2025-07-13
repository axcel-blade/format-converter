from tkinter import *
from FormatConverter import *
import os
from pathlib import Path

class VideoConverter():
    def __init__(self, BACKGROUND_COLOR, TEXT_COLOR, BUTTON_COLOR, root, mainMenu):
        self.BACKGROUND_COLOR = BACKGROUND_COLOR
        self.TEXT_COLOR = TEXT_COLOR        
        self.BUTTON_COLOR = BUTTON_COLOR
        self.DEFAULT_FILE_PATH = Path(f"C:\\Users\\{os.getlogin()}\\Downloads\\")
        self.mainMenu = mainMenu

        # Video converter frame
        self.videoConverterFrame = Frame(root)
        self.videoConverterFrame.pack(side=TOP, fill=X)
        self.videoConverterFrame.config(bg=BACKGROUND_COLOR)

        self.fileLocationFrame = Frame(self.videoConverterFrame)
        self.fileLocationFrame.pack(side=TOP, fill=X)
        self.fileLocationFrame.config(bg=BACKGROUND_COLOR)

        # File name label
        self.fileNameLabel = Label(self.fileLocationFrame, text="File path: ", font=("Arial", 12))
        self.fileNameLabel.pack(side=LEFT, fill=X, padx=10, pady=10)
        self.fileNameLabel.config(bg=BACKGROUND_COLOR, fg=TEXT_COLOR)

        # File location label
        self.fileLocationLabel = Label(self.fileLocationFrame, text=self.DEFAULT_FILE_PATH, font=("Arial", 12))
        self.fileLocationLabel.pack(side=LEFT, fill=X, padx=10, pady=10)
        self.fileLocationLabel.config(bg=BACKGROUND_COLOR, fg=TEXT_COLOR)

        # Select file button
        self.SelectFileButton = Button(self.fileLocationFrame, text="Select File", font=("Arial", 12), command=self.openFile)
        self.SelectFileButton.pack(side=LEFT, fill=X, padx=10, pady=10)
        self.SelectFileButton.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

        # self.convertTypeFrame = Frame(self.videoConverterFrame)
        # self.convertTypeFrame.pack(side=TOP, fill=X, padx=10, pady=10)
        # self.convertTypeFrame.config(bg=BACKGROUND_COLOR)

        # Convert type option menu    
        self.convertionTypes = ["MP4", "AVI"]
        self.defaultOption = StringVar(value=self.convertionTypes[0])
        
        # Convert type option menu
        self.convertTypeOptionMenu = OptionMenu(self.videoConverterFrame, self.defaultOption, *self.convertionTypes)
        self.convertTypeOptionMenu.pack(side=TOP, fill=X, padx=10, pady=10)
        self.convertTypeOptionMenu.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

        # Convert button
        self.convertButton = Button(self.videoConverterFrame, text="Convert", font=("Arial", 12), command=self.convertToVideoType)
        self.convertButton.pack(side=TOP, fill=X, padx=10, pady=10)
        self.convertButton.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

        # Back button
        self.backButton = Button(self.videoConverterFrame, text="Back", font=("Arial", 12), command=self.goBack)
        self.backButton.pack(side=TOP, fill=X, padx=10, pady=10)
        self.backButton.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

    # Go back to main menu
    def goBack(self):
        self.videoConverterFrame.pack_forget()
        self.mainMenu.showMainMenu()

    def openFile(self):
        pass

    def convertToVideoType(self):
        pass