from tkinter import *
from VideoConverter import *

class FormatConverter():
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = "#2a2a2a"

    global TEXT_COLOR
    TEXT_COLOR = "#ffffff"

    global BUTTON_COLOR
    BUTTON_COLOR = "#6a6a6a"

    def __init__(self, root):
        self.root = root
        self.root.title("Format Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND_COLOR)

        # Title frame
        self.titleFrame = Frame(root)
        self.titleFrame.pack(side=TOP, fill=X)
        self.titleFrame.config(bg=BACKGROUND_COLOR)

        # Title
        self.titleLabel = Label(self.titleFrame, text="Format Converter", font=("Arial", 18, "bold"))
        self.titleLabel.pack(side=TOP, fill=X)
        self.titleLabel.config(fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        # Converter buttons and progress bar frame
        self.converterFrame = Frame(root)
        self.converterFrame.pack(side=TOP, fill=X)
        self.converterFrame.config(bg=BACKGROUND_COLOR)

        # Converter buttons
        self.converterButtonsFrame = Frame(self.converterFrame)
        self.converterButtonsFrame.pack(side=TOP, fill=X)
        self.converterButtonsFrame.config(bg=BACKGROUND_COLOR)

        # Video converter
        self.videoConverterButton = Button(self.converterButtonsFrame, text="Video Converter", font=("Arial", 12), command=self.showVideoConverterFrame)
        self.videoConverterButton.pack(side=TOP, fill=X, padx=10, pady=10)
        self.videoConverterButton.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

        # Audio converter
        self.audioConverterButton = Button(self.converterButtonsFrame, text="Audio Converter", font=("Arial", 12))
        self.audioConverterButton.pack(side=TOP, fill=X, padx=10, pady=10)
        self.audioConverterButton.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

        # Progress bar frame
        self.progressBarFrame = Frame(self.converterFrame)
        self.progressBarFrame.pack(side=TOP, fill=X)
        self.progressBarFrame.config(bg=BACKGROUND_COLOR)

        # Progress bar
        self.progressBarLabel = Label(self.progressBarFrame, text="Progress: 0%", font=("Arial", 12))
        self.progressBarLabel.pack(side=TOP, fill=X)
        self.progressBarLabel.config(fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

        # Video converter frame
        self.videoConverterFrame = Frame(self.root)
        # self.videoConverterFrame.pack(side=TOP, fill=X)
        self.videoConverterFrame.config(bg=BACKGROUND_COLOR)

        # Convert to MP4 button
        self.convertToMP4Button = Button(self.videoConverterFrame, text="Convert to MP4", font=("Arial", 12))
        self.convertToMP4Button.pack(side=TOP, fill=X, padx=10, pady=10)
        self.convertToMP4Button.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)
        
        # Back button
        self.backButton = Button(self.videoConverterFrame, text="Back", font=("Arial", 12))
        self.backButton.pack(side=TOP, fill=X, padx=10, pady=10)
        self.backButton.config(bg=BUTTON_COLOR, fg=TEXT_COLOR)

        # Developer frame
        self.developerFrame = Frame(root)
        self.developerFrame.pack(side=BOTTOM, fill=X)
        self.developerFrame.config(bg=BACKGROUND_COLOR)

        # Developer label
        self.developerLabel = Label(self.developerFrame, text="Developed by: Joseph Fernando", font=("Arial", 12))
        self.developerLabel.pack(side=BOTTOM, fill=X, pady=10)
        self.developerLabel.config(fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

    def showVideoConverterFrame(self):
        self.converterFrame.pack_forget()

        self.videoConverter = VideoConverter(BACKGROUND_COLOR, TEXT_COLOR, BUTTON_COLOR, self.root, self)
        self.videoConverter.videoConverterFrame.pack(side=TOP, fill=X)

    def showMainMenu(self):
        self.videoConverter.videoConverterFrame.pack_forget()
        self.converterFrame.pack(side=TOP, fill=X)

if __name__ == "__main__":
    root = Tk()
    converter = FormatConverter(root)
    root.mainloop()