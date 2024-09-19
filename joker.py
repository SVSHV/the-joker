import tkinter as tk
import pyjokes

root = tk.Tk()
root.title("The Joker")
label = tk.Label(root, text= pyjokes.get_joke())
label.pack()


def next_button():
	joke = pyjokes.get_joke()
	label.config(text = joke)


#for (text, row, column) in button:
button = tk.Button(root, text='HaHa! Next',command=next_button)
button2 = tk.Button(root, text='Exit',command=root.destroy)
button.pack()
button2.pack()

root.mainloop()

