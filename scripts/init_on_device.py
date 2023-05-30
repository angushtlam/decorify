#!/usr/bin/python
import os
import sys
import time
import tkinter as tk

from PIL import ImageTk

# Append library files the system path so this file can import those files.
src_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(src_dir)

from decorify import Decorify


# Create a Decorify state machine
decorify_obj = Decorify()

# Create a new Tkinter window.
window = tk.Tk()

print("Ctrl+C to kill process.")

while True:
    # Load the image
    image = decorify_obj.get_image()

    # Create a `PhotoImage` object from the image.
    photo_image = ImageTk.PhotoImage(image)

    # Create a `Label` widget and set its `image` property to the `PhotoImage` object.
    label = tk.Label(window, image=photo_image)
    label.image = photo_image
    label.pack()

    # Render to the display
    window.update()

    # Take a break
    time.sleep(10)

    # Destroy the current image
    label.destroy()

    # Display the next image
    decorify_obj.next_image()
