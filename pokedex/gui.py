import tkinter as tk
from PIL import ImageTk, Image


def test_function():
    print("Button clicked!")

HEIGHT = 729
WIDTH = 410

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

img = Image.open("pokedex.jpg")
resized = img.resize((410, 729), Image.ANTIALIAS)
img = ImageTk.PhotoImage(resized)
canvas.create_image((0, 0), anchor=tk.NW, image=img)

# container for upperframe label
upper_frame = tk.Frame(root)
upper_frame.place(relx=0.45, rely=0.28, relwidth=0.53, relheight=0.21, anchor='n')

label = tk.Label(upper_frame, bg='#80c1ff')
label.place(relwidth=1, relheight=1)

mid_frame = tk.Frame(root)
mid_frame.place(relx=0.37, rely=0.685, relwidth=0.29, relheight=0.095, anchor='n')

entry = tk.Entry(mid_frame, font=40)
entry.place(relwidth=1, relheight=1)

lower_frame = tk.Frame(root)
lower_frame.place(relx=0.37, rely=0.80, relwidth=0.3, relheight=0.04, anchor='n')

button = tk.Button(lower_frame, text="Search", font=40, command=test_function)
button.place(relheight=1, relwidth=1)


# main container
root.mainloop()
