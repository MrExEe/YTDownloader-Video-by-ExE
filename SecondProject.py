from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox

#Second Project

def action():
    enlace=videos.get()
    video = YouTube(enlace)
    descargas = video.streams.get_highest_resolution()
    descargas.download()

root = Tk()
root.config(bd=15)
root.title("YTDownloader Video by ExE")

imagen = PhotoImage(file="youtube.png")
Photo = Label(root, image=imagen, bd=0)
Photo.grid(row=0, column=0)

instrucciones = Label(root, text="Programa creado para descargar videos de YT")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

button = Button(root, text="Descargar video", command=action)
button.grid(row=2, column=1)

root.mainloop()


