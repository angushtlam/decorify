#!/usr/bin/python
import os
import sys
from PIL import ImageTk
import tkinter as tk

# Append library files the system path so this file can import those files.
src_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(src_dir)

from decorify import decorify


# Create a new Tkinter window.
window = tk.Tk()

# Load the image.
assets_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'assets')
image = decorify.get_image()

# Create a `PhotoImage` object from the image.
photo_image = ImageTk.PhotoImage(image)

# Create a `Label` widget and set its `image` property to the `PhotoImage` object.
label = tk.Label(window, image=photo_image)
label.image = photo_image
label.pack()

# Start the Tkinter main loop.
window.mainloop()
