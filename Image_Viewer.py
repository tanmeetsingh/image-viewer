from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.geometry("580x620")

root.resizable(0, 0)
root.title('Image Viewer by Suraj')
root.iconbitmap('images\icon.ico')
frame = LabelFrame(root, padx=3, pady=3, highlightbackground="red")
frame.grid(row=0, column=0, columnspan=3, padx=3, pady=3, ipadx=3)
global current
current = 0

images = ["images\Darren.jpg", "images\harry.jpg", "images\jenny.jpg", "images\john.jpg", "images\Misty.jpg",
          "images\panda.jpg"]

lst = []
for image in images:
    lst.append(ImageTk.PhotoImage(Image.open(image)))
global image_len
image_len = str(len(lst))
global label
label = Label(frame, image=lst[current], width=540, height=540)
label.grid(row=0, columnspan=3)
global status_bar
status_bar = Label(root, text="Image 1 of 6 ", relief=SUNKEN)
status_bar.grid(row=2, column=2, columnspan=3, sticky=E)


def left():
    global label
    label.grid_forget()
    global current
    current = current - 1
    if (current == -1):
        current = 5
    label = Label(frame, image=lst[current], width=540, height=540)
    label.grid(row=0, columnspan=3)
    image_pos = str(current + 1)
    global status_bar
    status_bar.grid_forget()
    status_bar = Label(root, text="Image " + image_pos + " of " + image_len, relief=SUNKEN)
    status_bar.grid(row=2, columnspan=3, sticky=E)


def right():
    global label
    label.grid_forget()
    global current
    current = current + 1
    if (current == 6):
        current = 0
    label = Label(frame, image=lst[current], width=540, height=540)
    label.grid(row=0, columnspan=3)
    image_pos = str(current + 1)
    global status_bar
    status_bar.grid_forget()
    status_bar = Label(root, text="Image " + image_pos + " of " + image_len, relief=SUNKEN)
    status_bar.grid(row=2, sticky=E, columnspan=3)


b = Button(root, text='Quit', command=root.quit).grid(row=1, column=1, sticky=N + S + E + W)
b_left = Button(root, text='<<', command=left).grid(row=1, column=0, sticky=N + S + E + W)
b_right = Button(root, text='>>', command=right).grid(row=1, column=2, sticky=N + S + E + W)

root.mainloop()
