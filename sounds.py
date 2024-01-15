from tkinter import * 
import pygame 

root = Tk()
root.title("LF sound")
root.geometry("500x400")

pygame.mixer.init()

def play():
    pygame.mixer.music.load("music/Recording.mp3")
    pygame.mixer.music.play(loops=0)
    


my_button = Button(root, text="Play Song", font=("Helvetica", 24), command=play)
my_button.pack(pady=20)

root.mainloop()