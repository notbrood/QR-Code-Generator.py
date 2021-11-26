import pyqrcode
import tkinter
import png


root = tkinter.Tk()
root.title('QR Code Generator by Brood')
data = tkinter.Entry(root)
root.configure(bg = "#1974D2")
def gen_qr():
    s = data.get()
    url = pyqrcode.create(s)
    url.png("qr\qrcode.png", scale = 6)
    test = url.xbm(scale=5)
    global xbm_image
    xbm_image = tkinter.BitmapImage(data=test, foreground="black")
    image_view.config(image=xbm_image)
    statement.config(text="This is a QR Code for : " + str(data.get()))


heading = tkinter.Label(root, text="QR Code Generator", font="Helvetica 40 bold", background= "#2554C7", foreground="white")
subheading = tkinter.Label(root, text="by @notbrood", font="Helvetica 15", background="#1974D2", foreground="white")
subtitle = tkinter.Label(root, text="Enter the data ", font="Arial 20 bold", background="#1974D2")
make_button = tkinter.Button(root, text=" Make QR", font="Arial 20", background="#2554C7", foreground="white", command=gen_qr)
image_view = tkinter.Label(root)
statement = tkinter.Label(root, background="#1974D2")


heading.grid(row=0, column=0, columnspan=2)
subheading.grid(row=1, column=0, columnspan=2)
subtitle.grid(row=2, column=0)
data.grid(row=2, column=1)
make_button.grid(row=3, column=0, columnspan=2)
image_view.grid(row=4, column=0, columnspan=2)
statement.grid(row=5, column=0, columnspan=2)


root.mainloop()