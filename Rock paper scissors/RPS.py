from tkinter import *;
from random import randint
from tkinter import ttk
from tkinter import font
from tkinter.font import Font


root = Tk()
root.title('Rock, Paper, Scissors')

root.geometry("550x600")

root.config(bg='white')

rock = PhotoImage(file= 'rock.png')
paper = PhotoImage(file='paper.png')
scissors = PhotoImage(file='scissors.png')

image_list=[rock, paper, scissors]

pick_random=randint(0,2)


display=Label(root, image=image_list[pick_random], border=0)
display.pack(pady=20, padx=20)

def spin():
    pick_random=randint(0,2)
    display.config(image=image_list[pick_random])

    if user_choice.get()== "Rock":
        user_choice_value=0
    elif user_choice.get()== "Paper":
        user_choice_value=1
    elif user_choice.get()== "Scissors":
        user_choice_value=2

    if user_choice_value==0:
        if pick_random==0:
            win_lose_label.config(text="It's a Tie! Spin Again...")
        elif pick_random==1:
            win_lose_label.config(text="Paper covers Rock. You LOSE!")
        elif pick_random==2:
            win_lose_label.config(text="Rock smashes Scissor. You WIN!")

    if user_choice_value==1:
        if pick_random==0:
            win_lose_label.config(text="Paper covers Rock. You WIN!")
        elif pick_random==1:
            win_lose_label.config(text="It's a Tie! Spin Again...")
        elif pick_random==2:
            win_lose_label.config(text="Scissor cuts Paper. You LOSE!")
    
    if user_choice_value==2:
        if pick_random==0:
            win_lose_label.config(text="Rock smashes Scissors. You LOSE!")
        elif pick_random==1:
            win_lose_label.config(text="Scissor cuts Paper. You WIN!")
        elif pick_random==2:
            win_lose_label.config(text="It's a Tie! Spin Again...")


spin_button=Button(root, text="Spin", command=spin)
spin_button.pack(pady=10)

user_choice= ttk.Combobox(root, value=("Rock", "Paper", "Scissors"))
user_choice.current(0)
user_choice.pack(pady=10)

win_lose_label= Label(root, text="", font=("Helvetica", 18), bg="white")
win_lose_label.pack()

root.mainloop()