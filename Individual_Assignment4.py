import tkinter as tk
main_window = tk.Tk()
main_window.geometry('250x150')
#Add button 1
button1 = tk.Button(text="left")
#pack button 1
button1.pack(side = 'left')
#Add button 2
button2 = tk.Button(text="top")
#pack button 2
button2.pack(side = 'top')
#Add button 3
button3 = tk.Button(text="right")
#pack button 3
button3.pack(side = 'right')
#Add button 4
button4 = tk.Button(text="bottom")
#pack button 4
button4.pack(side = "bottom")
main_window.mainloop()
