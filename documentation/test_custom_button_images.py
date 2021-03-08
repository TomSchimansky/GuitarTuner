import tkinter
from tkinter_custom_button import TkinterCustomButton
from PIL import Image, ImageTk

app = tkinter.Tk()
app.geometry("300x200")
app.title("TkinterCustomButton")

def button_function():
    print("Button pressed")

play_image = ImageTk.PhotoImage(Image.open("button_test_images/play_button_image.png").resize((40, 40)))
skip_image = ImageTk.PhotoImage(Image.open("button_test_images/skip_button_image.png").resize((40, 40)))

button_1 = TkinterCustomButton(image=play_image, width=60, height=60, corner_radius=12, command=button_function)
button_1.place(relx=0.33, rely=0.5, anchor=tkinter.CENTER)

button_2 = TkinterCustomButton(image=skip_image, width=60, height=60, corner_radius=12, command=button_function)
button_2.place(relx=0.66, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()