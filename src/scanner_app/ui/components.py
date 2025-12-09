# scanner_app/src/scanner_app/ui/components.py
import tkinter as tk
from PIL import ImageTk

class ImageThumbnail(tk.Label):
    def __init__(self, parent, image, idx):
        self.image = image.resize((100, 100))  # Thumbnail size
        self.photo = ImageTk.PhotoImage(self.image)
        
        super().__init__(parent, image=self.photo)
        self.image = self.photo  # Keep reference
        self.bind("<Button-1>", lambda e: self.show_full_image(idx))

    def show_full_image(self, idx):
        # For now, just print; could open a new window
        print(f"Showing full image {idx}")