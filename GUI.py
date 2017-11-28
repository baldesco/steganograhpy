import tkinter as tk
from PIL import ImageTk, Image
import Decoder as dco
from tkinter.filedialog import askopenfilename, asksaveasfilename
import tkinter.messagebox

#Carga el path de la imagen que se quiere abrir, y lo escribe en el campo entry_1.
def search_path_in():
        fname = askopenfilename(filetypes=(("Image files", "*.jpg;*.gif;*.png;*.bmp"),
                                           ("All files", "*.*") ))
        var_1.set(fname)

def search_path_out():
        fname = asksaveasfilename(filetypes=(("Image files", "*.png"),
                                           ("All files", "*.*") ))
        var_2.set(fname)

def load_image():
        picsize = 400, 400
        image = Image.open(var_1.get())
        image.thumbnail(picsize,Image.ANTIALIAS)
        im = ImageTk.PhotoImage(image)
        panel.configure(image=im)
        panel.image = im

def decode_image_command():
    img = dco.decode_image(var_1.get())
    picsize = 400, 400
    img.thumbnail(picsize,Image.ANTIALIAS)
    im = ImageTk.PhotoImage(img)
    panel.configure(image=im)
    panel.image = im

def encode_image_command():
    texto = text_1.get('1.0','end-1c')
    nombre_imagen = var_2.get()
    template_image = var_1.get()
    dco.encode_image(texto,nombre_imagen,template_image)
    tkinter.messagebox.showinfo('Info', 'Image saved!')

root = tk.Tk()
root.resizable(width=False, height=False)
root.wm_title('Steganographer')
root.iconbitmap(default='favicon.ico')


label_1 = tk.Label(root,text='Select\nimage:')
label_1.grid(row=0, column=0, rowspan=2)
label_4 = tk.Label(root,text='Type the message that you want to hide:',justify='left')
label_4.grid(row=4, column=0, columnspan=2)
label_5 = tk.Label(root,text='Select\ndestination:')
label_5.grid(row=13, column=0, rowspan=2)
label_6 = tk.Label(root,text='Show hidden message:        ',font='Arial 10 bold',justify='left')
label_6.grid(row=2, column=0,columnspan=2)
label_6 = tk.Label(root,text='Hide message inside image:',font='Arial 10 bold',justify='left')
label_6.grid(row=3, column=0,columnspan=2)
label_3 = tk.Label(root,text='      ')   #Para Crear espacios en la interfaz
label_3.grid(row=3, column=4)
label_7 = tk.Label(root,text='')   #Para Crear espacios en la interfaz
label_7.grid(row=14, column=4)


var_1 = tk.StringVar()
var_2 = tk.StringVar()

entry_1 = tk.Entry(root,width=30, textvariable=var_1)
entry_1.grid(row=0, column=1, columnspan=5,sticky='E'+'W')
entry_2 = tk.Entry(root,width=30, textvariable=var_2)
entry_2.grid(row=13, column=1, columnspan=5,sticky='E'+'W')

text_1 = tk.Text(root, height=15, width=40)
text_1.grid(row=5, column=1,columnspan=2,rowspan=5,sticky='E'+'W'+'N'+'S')


boton_1 = tk.Button(root, text="Browse", command=search_path_in, width=10, bg = "white")
boton_1.grid(row=0, column=6)
boton_2 = tk.Button(root, text="Load image", command=load_image, width=10, bg = "yellow")
boton_2.grid(row=0, column=8)
boton_3 = tk.Button(root, text="Decode image", command=decode_image_command, width=13, bg = "red")
boton_3.grid(row=2, column=3)
boton_4 = tk.Button(root, text="Encode\nimage", command=encode_image_command, width=10, bg = "red")
boton_4.grid(row=13, column=8,rowspan=2)
boton_5 = tk.Button(root, text="Browse", command=search_path_out, width=10, bg = "white")
boton_5.grid(row=13, column=6)

img = Image.open('mystery.jpg')
picsize = 400, 400
img.thumbnail(picsize,Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
panel = tk.Label(root, image = img, width=400, height=400,borderwidth=2, relief="groove")
panel.grid(row=2,column=5,columnspan=4,rowspan=10)


root.mainloop()
