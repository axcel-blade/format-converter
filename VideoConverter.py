from tkinter import *
from FormatConverter import FormatConverter

class VideoConverter():
    def __init__(self, BACKGROUND_COLOR, TEXT_COLOR, BUTTON_COLOR, root):
        self.BACKGROUND_COLOR = BACKGROUND_COLOR
        self.TEXT_COLOR = TEXT_COLOR        
        self.BUTTON_COLOR = BUTTON_COLOR

        # Video converter frame
        self.videoConverterFrame = Frame(root)
        self.videoConverterFrame.pack(side=TOP, fill=X)
        self.videoConverterFrame.config(bg=BACKGROUND_COLOR)

        # Convert to MP4 button
        self.convertToMP4Button = Button(self.videoConverterFrame, text="Convert to MP4", font=("Arial", 12))
        self.convertToMP4Button.pack(side=TOP, fill=X, padx=10, pady=10)
        self.convertToMP4Button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

        # Back button
        self.backButton = Button(self.videoConverterFrame, text="Back", font=("Arial", 12), command=self.goBack)
        self.backButton.pack(side=TOP, fill=X, padx=10, pady=10)
        self.backButton.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

    def goBack(self):
        self.videoConverterFrame.pack_forget()
        self.FormatConverter = FormatConverter()
        self.FormatConverter.showMainMenu()