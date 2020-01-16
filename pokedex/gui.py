import tkinter as tk

HEIGHT = 500
WIDTH = 600

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

button = tk.Button(root, text="Test Button")
button.pack()

label = tk.Label(frame, text="This is a label", bg='yellow')
label.pack()

entry = tk.Entry(frame, bg='green')
entry.pack()

# main container
root.mainloop()
