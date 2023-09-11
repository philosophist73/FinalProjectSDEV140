import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def conversions():
    mile_input = entry_int.get()
    kilometer_output = mile_input * 1.61
    return f'{output_string.set(round(kilometer_output, 2))} Kilometers'
    
def conversions1():
    celsius_input = entry_int.get()
    fahrenheit_output = (celsius_input * 1.8) + 32
    output_string1.set(round(fahrenheit_output, 2))
    
def conversions2():
    day_input = entry_int.get()
    seconds_output = day_input*86400
    output_string2.set(round(seconds_output, 2))

attempts = 6
secretNumber = random.randint(1, 20)

def guessFunc():
    global text, attempts
    secretNumber = random.randint(1, 20)
    
    guess = int(entry.get())
    
    attempts -= 1
    
    if guess == secretNumber:
        text.set("Congrats! You guessed it!")
        button.pack_forget()
    elif attempts == 0:
        text.set("You ran out of guesses")
        button.pack_forget()
    elif guess < secretNumber:
        text.set(f'Incorrect! You now have {attempts} guesses remaining. Guess a higher number!!')
    elif guess > secretNumber:
        text.set(f'Incorrect! You now have {attempts} guesses remaining. Guess a lower number!!')
    
    return
    
def MileConverter():
    global frame, entry, label, entry_int, button, output_label, output_string
    window2 = tk.Toplevel()
    window2.geometry('300x300')
    window2.title('Converting Kilometers and Miles')
    
    label = Label(window2, text='Converting Miles to Kilometers', font=('Times New Roman Bold', 15))
    label.pack()
    
    frame = Frame(window2)
    frame.pack()
    
    entry_int = tk.IntVar()
    entry = Entry(frame, textvariable= entry_int)
    button = Button(frame, text='Convert', command=conversions)
    button_quit = Button(frame, text='Exit Program', command=quit)
    output_string = tk.StringVar()
    output_label = Label(window2, text='Output', font=('Times New Roman Bold', 12), textvariable= output_string, bg='blue', fg='yellow')
    entry.pack(pady=5)
    button.pack(pady=5)
    output_label.pack(pady=5)
    button_quit.pack(pady=5)
    
    
def CelsiusConverter():
    global frame, entry, label, entry_int, button, output_label, output_string1
    window3 = tk.Toplevel()
    window3.geometry('500x250')
    window3.title('Converting Temperatures')
    
    label = Label(window3, text='Converting Celsius to Fahrenheit', font=('Times New Roman Italic', 20))
    label.pack(side=TOP, pady=10)
    
    frame = Frame(window3)
    frame.pack()
    
    entry_int = tk.IntVar()
    entry = Entry(frame, textvariable= entry_int)
    button = Button(frame, text='Convert', pady= 5, command=conversions1)
    button_quit = Button(frame, text='Exit Program', command=quit)
    entry.pack(side=TOP, pady=5)
    button.pack(side=TOP, pady=5)
    button_quit.pack(side=TOP, pady=5)
    
    output_string1 = tk.StringVar()
    output_label = Label(window3, text='Output', font=('Times New Roman Bold', 12), textvariable= output_string1)
    output_label.pack()

def SecondsConverter():
    global frame, entry, label, entry_int, button, output_label, output_string2, button_quit, window1
    window4 = tk.Toplevel()
    window4.geometry('500x250')
    window4.title('Days to Seconds')
    
    label = Label(window4, text='Days to Seconds', font=('Times New Roman Italic', 20))
    label.pack(side=TOP, pady=10)
    
    frame = Frame(window4)
    frame.pack()
    
    entry_int = tk.IntVar()
    entry = Entry(frame, textvariable= entry_int)
    button = Button(frame, text='Convert', pady= 5, command=conversions2)
    button_quit = Button(frame, text='Exit Program', command=quit)
    entry.pack(side=TOP, pady=5)
    button.pack(side=TOP, pady=5)
    button_quit.pack(side=TOP, pady=5)
    
    output_string2 = tk.StringVar()
    output_label = Label(window4, text='Output', font=('Times New Roman Bold', 12), textvariable= output_string2)
    output_label.pack()


def checkifwon():
    global winner
    winner = False 
    
#Winning Combinations for X
    
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
    if b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
    if b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
    if b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
    if b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
    if b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
    if b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
    if b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! X won!!")
        
# Winning Combinations for O
        
    if b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")
    if b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")
    if b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")
    if b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")
    if b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")
    if b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")
    if b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")
    if b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations! O won!!")

clicked = True
count = 0

def button_clicked(b):
    global clicked, count
    
    if b['text'] == " " and clicked == True:
        b['text'] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b['text'] == " " and clicked == False:
        b['text'] = "O"
        clicked = True
        count += 1 
        checkifwon()
    else:
        messagebox.showerror('Tic Tac Toe', 'This box is already marked! Please make another selection')
    

def TicTacToe():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, leave
    ticTacToe = tk.Toplevel()
    ticTacToe.geometry('300x345')
    ticTacToe.title('TIC TAC TOE')
    b1 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b1))
    b2 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b2))
    b3 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b3))

    b4 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b4))
    b5 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b5))
    b6 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b6))
    
    b7 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b7))
    b8 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b8))
    b9 = Button(ticTacToe, text= " ", font=('Times New Roman', 20), height=3, width=6, bg='SystemButtonFace', command=lambda: button_clicked(b9))
    
    # setting up our grid
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


def mathCalcs():
    math = tk.Toplevel()
    math.geometry('600x250')
    math.title('Math Calculations')

    label = Label(math, text='Please select a Math calculation you would like to compute!')

    math1 = Button(math, text='Miles to Kilometers', command= MileConverter)
    math2 = Button(math, text='Converting Temperature', command= CelsiusConverter)
    math3 = Button(math, text='Converting Speed', command= SecondsConverter)
    label.pack()
    math1.pack(pady=5)
    math2.pack(pady=5)
    math3.pack(pady=5)


def GuessTheNumber():
    global frame, entry, label, entry_int, button, output_label, text
    window3 = tk.Toplevel()
    window3.geometry('500x250')
    window3.title('Converting Temperatures')
    
    label = Label(window3, text='Guess a number between 1 and 20', font=('Times New Roman Italic', 20))
    label.pack(side=TOP, pady=10)
    
    frame = Frame(window3)
    frame.pack()
    
    entry_int = tk.IntVar()
    entry = Entry(frame, textvariable= entry_int)
    button = Button(frame, text='Check', pady= 5, command=guessFunc)
    button_quit = Button(frame, text='Exit Program', command=quit)
    entry.pack(side=TOP, pady=5)
    button.pack(side=TOP, pady=5)
    button_quit.pack(side=TOP, pady=5)
    
    text = tk.StringVar()
    text.set("You have 6 attempts remaining! Good Luck!")
    output_label = Label(window3, text='Output', font=('Times New Roman Bold', 12), textvariable= text)
    output_label.pack()

# First Window
window1 = tk.Tk()
window1.geometry('600x250')
window1.title('Welcome to my Final Project')


ticTacToe_img = Image.open("TicTacToe.png")
resized = ticTacToe_img.resize((50,50), Image.ANTIALIAS)
ticTacToe_img_resized = ImageTk.PhotoImage(resized)

math_img = Image.open("MathCalculations.png")
math_resized = math_img.resize((50,50), Image.ANTIALIAS)
math_img_resized = ImageTk.PhotoImage(math_resized)

guess_img = Image.open("GuessTheNumber.png")
guess_resized = guess_img.resize((50,50), Image.ANTIALIAS)
guess_img_resized = ImageTk.PhotoImage(guess_resized)

label = Label(window1, text='Please select a program to run', font=('Times New Roman Bold', 15))
label.pack(pady=5) 
# Window Orientation
math_btn = Button(window1, command= mathCalcs, image=math_img_resized)
ticTacToe_btn = Button(window1, command=TicTacToe, image=ticTacToe_img_resized)
guess_btn = Button(window1, command=GuessTheNumber, image=guess_img_resized)
math_btn.pack(pady=5)
ticTacToe_btn.pack(pady=5)
guess_btn.pack(pady=5)



window1.mainloop()
