from tkinter import *
import numpy as np
import cv2
from matplotlib import pyplot as plt
pencere = Tk()
pencere.geometry("270x150")
pencere.title("Photo Master")
pencere.iconbitmap(default='Photo_Master-removebg-preview.ico')

def sign_in():
    sifre=entry.get()
    img = cv2.imread(sifre, 1)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.show()




label=Label(pencere)
label.config(text="Fotoğraf Klasörü",font=("Arial",20))
label.place(x=20,y=20)

entry=Entry(pencere)
entry.place(x=20,y=70)

buton=Button(pencere)
buton.config(text="Tamamla",bg="black",fg="white",command=sign_in)
buton.place(x=20,y=100)

mainloop()