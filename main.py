from tkinter import *
from PIL import Image, ImageTk 
import pygame

pygame.mixer.init()

window = Tk()
window.title("Эщкерембус")
window.geometry("500x300")
window.configure(bg="light gray")
window.iconbitmap("dota2.ico")

count = 0 
light_on = False  

image1 = Image.open("1.jpg")  
image1 = image1.resize((300, 134))  
image1 = ImageTk.PhotoImage(image1)  

image2 = Image.open("2.png")  
image2 = image2.resize((300, 134))  
image2 = ImageTk.PhotoImage(image2)  

image_label = Label(window, image=image1)
image_label.pack(pady=10)  

def on_button_click():
    global count
    count += 1
    if count % 2 == 1:
        window.configure(bg="light gray")  
        lab1.config(text="0")
        pygame.mixer.music.load("u1.mp3")
        pygame.mixer.music.play() 
        image_label.config(image=image1) 
        image_label.pack(pady=10)  
    else:
        window.configure(bg="white")  
        lab1.config(text="1")
        pygame.mixer.music.load("1488.mp3")
        pygame.mixer.music.play() 
        image_label.config(image=image2)  
        image_label.pack(pady=10)  

button = Button(window, text="нет", command=on_button_click, bg='lightgray')
button.pack(pady=10)

lab1 = Label(window, text="0", bg="black", fg="white")
lab1.pack(pady=10)

window.mainloop()