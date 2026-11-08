import tkinter as tk

root = tk.Tk()
menu = tk.Menu(root, tearoff=0)

# 1. Checkbutton: the ✓ goes IN the left column
checked = tk.BooleanVar(value=True)
menu.add_checkbutton(label="Checkbutton (✓ in the gap)", variable=checked)

# 2. Symbol inside the text: it goes AFTER the gap
menu.add_command(label="🖥 RDP (symbol in text)")
menu.add_command(label="📁 WinSCP")

# Reference: normal item
menu.add_command(label="Normal item")

root.bind("<Button-3>", lambda e: menu.tk_popup(e.x_root, e.y_root))
root.mainloop()