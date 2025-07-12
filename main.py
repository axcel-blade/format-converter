from tkinter import *

class FormatConverter():
    def __init__(self, root):
        BACKGROUND_COLOR = "#2a2a2a"
        TEXT_COLOR = "#ffffff"
        BUTTON_COLOR = "#6a6a6a"
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
        self.videoConverterButton = Button(self.converterButtonsFrame, text="Video Converter", font=("Arial", 12))
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

        # Developer frame
        self.developerFrame = Frame(root)
        self.developerFrame.pack(side=BOTTOM, fill=X)
        self.developerFrame.config(bg=BACKGROUND_COLOR)

        # Developer label
        self.developerLabel = Label(self.developerFrame, text="Developed by: Joseph Fernando", font=("Arial", 12))
        self.developerLabel.pack(side=BOTTOM, fill=X, pady=10)
        self.developerLabel.config(fg=TEXT_COLOR, bg=BACKGROUND_COLOR)

if __name__ == "__main__":
    root = Tk()
    converter = FormatConverter(root)
    root.mainloop()