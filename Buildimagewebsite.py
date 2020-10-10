from tkinter import *
from PIL import ImageTk,Image
root = Tk()
root.iconbitmap("D:/Icon Photo/Itzikgur-My-Seven-Pictures-Canon.ico")
root.geometry("400x400")



my_image = ImageTk.PhotoImage(Image.open("D:/Icon Photo/download (2).png"))
my_image1 = ImageTk.PhotoImage(Image.open("D:/Icon Photo/download2.jfif"))


def next():




Title = Label(root, text = "Image Gallery", font="Algerian 20 bold")
Title.grid(row=0, column=1)

label1 = Label(image = my_image1, width=400)
label1.grid(row=1, columnspan=3,column=0)

b1 = Button(root,text=">>>", command = next)
b1.grid(row=1, column = 2, columnspan = 1)

b1 = Button(root,text="<<<")
b1.grid(row=1, column = 0)

exit_p = Button(root, text= "Exit Programme", command=root.quit)
exit_p.grid(row = 2, column=1)

root.mainloop()