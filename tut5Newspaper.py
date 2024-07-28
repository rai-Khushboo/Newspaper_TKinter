from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("1200x700")  # Increased window size to accommodate multiple images
root.title("Newspaper")

label = Label(text = "Tech & Terra Times",fg="green",font="comicsansms 19 bold" ,relief=SUNKEN)
label.pack()

# Function to create a frame with an image and text
def create_img_frame(parent, image_path, text):
    frame = Frame(parent)
    frame.pack(side=LEFT, padx=90, pady=20)  # Pack frames side-by-side with padding

    # Load and resize image
    image = Image.open(image_path)
    image = image.resize((300, 200), Image.Resampling.LANCZOS)  # Updated resampling method
    photo = ImageTk.PhotoImage(image)

    # Add image to the frame
    img_label = Label(frame, image=photo)
    img_label.image = photo  # Keep a reference to avoid garbage collection
    img_label.pack()

    # Add text to the frame
    text_label = Label(frame, text=text, wraplength=300, justify=LEFT, font=("Helvetica", 10))
    text_label.pack()  # Ensure this is packed to show the text

    return frame

# Paths to images and their descriptions
images = [
    ("C:/Users/Dell/Desktop/Python/Tkinter_course/nature.jpg", "This captivating image showcases the serene beauty of nature. The lush greenery and tranquil surroundings offer a peaceful escape, reminding us of the calm and restorative power of the natural world."),
    ("C:/Users/Dell/Desktop/Python/Tkinter_course/choice.jpg", "A compelling visual depicting two individuals contemplating different paths. This image symbolizes the myriad choices we face in life and the journeys that await us, each with its own set of possibilities and adventures."),
    ("C:/Users/Dell/Desktop/Python/Tkinter_course/thought.jpg", "This inspiring image captures a profound motivational thought: it's not just about the destination, but the journey itself. It serves as a reminder to embrace each step along the way, finding meaning and growth in the process of striving toward our goals."),
    ("C:/Users/Dell/Desktop/Python/Tkinter_course/calcii.jpg", "An insightful depiction of a calculator crafted with Python's Tkinter. This image illustrates the intricate design and functionality of the tool, showcasing the power of programming in creating practical and innovative solutions.")
]

# Create frames and arrange in rows
for i in range(0, len(images), 2):  # Loop over images in steps of 2
    row_frame = Frame(root)
    row_frame.pack()  # Pack new row frame

    # Create and pack each image frame in the current row
    for j in range(i, min(i+2, len(images))):
        img_path, description = images[j]
        create_img_frame(row_frame, img_path, description)

root.mainloop()
