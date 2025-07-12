from tkinter import *

class FormatConverter():
    def __init__(self, root):
        self.root = root
        self.root.title("Format Converter")
        self.root.geometry("400x300")
        self.root.resizable(False, False)
    
        # Title frame
        self.titleFrame = Frame(root)
        self.titleFrame.pack(side=TOP, fill=X)

        # Title
        self.titleLabel = Label(self.titleFrame, text="Format Converter", font=("Arial", 18, "bold")).pack(side=TOP, fill=X)

        # Converter buttons and progress bar frame
        self.converterFrame = Frame(root)
        self.converterFrame.pack(side=TOP, fill=X)

        # Converter buttons
        self.converterButtonsFrame = Frame(self.converterFrame)
        self.converterButtonsFrame.pack(side=TOP, fill=X)

        # Video converter
        self.videoConverterButton = Button(self.converterButtonsFrame, text="Video Converter", font=("Arial", 12)).pack(side=TOP, fill=X, padx=10, pady=10)

        # Audio converter
        self.audioConverterButton = Button(self.converterButtonsFrame, text="Audio Converter", font=("Arial", 12)).pack(side=TOP, fill=X, padx=10, pady=10)

        # Progress bar frame
        self.progressBarFrame = Frame(self.converterFrame)
        self.progressBarFrame.pack(side=TOP, fill=X)

        # Progress bar
        self.progressBarLabel = Label(self.progressBarFrame, text="Progress: 0%", font=("Arial", 12)).pack(side=TOP, fill=X)

        # Developer frame
        self.developerFrame = Frame(root)
        self.developerFrame.pack(side=BOTTOM, fill=X)

        # Developer label
        self.developerLabel = Label(self.developerFrame, text="Developed by: Joseph Fernando", font=("Arial", 12)).pack(side=BOTTOM, fill=X, pady=10)

if __name__ == "__main__":
    root = Tk()
    converter = FormatConverter(root)
    root.mainloop()