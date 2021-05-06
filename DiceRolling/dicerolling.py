import tkinter
from PIL import Image, ImageTk
import random
from datetime import datetime

# toplevel widget which represents the main window of an application
# to create base GUI 
root = tkinter.Tk() 
root.geometry('800x600')
root.title('ST Dice Rolling Simulator')
totalc=0 #Count Match
totalr=0 #Count rolling_dice

# Adding label into the frame 
l0 = tkinter.Label(root, text="") #First label - L0
l0.pack() #Funtion for label location at top

# adding label with different font and formatting
l1 = tkinter.Label(root, text="Let's rock & roll!", fg = "light green", #Second label - L1
        bg = "dark blue", #fg=Font color, bg=background color
        font = "Arial 30 bold") #Helvetica italic
l1.pack() #Funtion for label default location at after Label0

l2a = tkinter.Label(root, text="Total Roll= 0", fg = "light blue",
        bg = "dark red",
        font = "Arial 20 bold")
l2a.pack(padx=25, pady=25, side=tkinter.TOP)#xxx

l2 = tkinter.Label(root, text="Total Match = 0", fg = "light blue",
        bg = "dark red",
        font = "Arial 30 bold")
l2.pack(fill=tkinter.X, padx=5, expand=True ) #fill=tkinter.X to fill 

# Image List, arrange in ascending , die0=question mark
dice = ['die0.png', 'die1.png', 'die2.png', 'die3.png', 'die4.png', 'die5.png', 'die6.png']
# simulating the dice with random numbers between 0 to 6 and generating image
image1 = ImageTk.PhotoImage(Image.open(dice[0])) #pillow class : grab image from file / rectangle
image2 = ImageTk.PhotoImage(Image.open(dice[0])) #pillow class :grab image from file / rectangle
# construct a label widget for image
label1 = tkinter.Label(root, image=image1) #tkinter/GUI class : to load image1 /rectangle
label2 = tkinter.Label(root, image=image2) #tkinter/GUI class : to load image2 /rectangle
label1.image = image1 #to display image1 /rectangle
label2.image = image2 #to display image2 /rectangle

# packing a widget in the parent widget 
label1.pack(padx=50, pady=20, side=tkinter.LEFT) #location of label 1 (image 1)
label2.pack(padx=50, pady=50, side=tkinter.LEFT) #location of label 2 (image 2)

# function to return now
def now():
    return datetime.now().strftime('%Y.%m.%d %H:%M:%S') #To store date time for dice rolling in file

# function activated by button
def rolling_dice():
    global totalc #to define variable name for total match counter
    global totalr #to define variable name for total rolling dice counter
    dice1=random.randint(1,6) #to generate random number for dice 1
    dice2=random.randint(1,6) #to generate random number for dice 2
    
    image1=ImageTk.PhotoImage(Image.open(dice[dice1])) #Pillow class: to grab image for dice 1
    image2=ImageTk.PhotoImage(Image.open(dice[dice2])) #Pillow class: to grab image for dice 2
    #image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    # update image
    label1.configure(image=image1) #to configure label 1 image / 
    label2.configure(image=image2) #to configure label 2 image
    # keep a reference
    label1.image = image1 #to connect label1 and display image 1
    label2.image = image2 #to connect label2 and display image 2
    totalr += 1 #to count total rolling dice
    l2a.config(text="Total Roll = " + str(totalr)) #to configure text of total roll
    l2a.update_idletasks() #to update the # of total roll
    if dice1 == dice2: 
        totalc += 1 
        l2.config(text="Total Match = " + str(totalc)) #to configure text of total match
        l2.update_idletasks() #to update the # of total match
    f= open("RollResult.csv", "a+") #to open the file, a+ = append
    f.write(now() + ";" + str(dice1) + ";" + str(dice2) + '\n') #to record rolling data (time and rolling result)
    f.close() #to close the filepython
        
        

# adding button, and command will use rolling_dice function
button = tkinter.Button(root, text='Roll the Dice', fg='blue', height=5, width=15, command=rolling_dice) #button design, to call rolling dice function

# pack a widget in the parent widget
button.pack( expand=True) #button position

# call the mainloop of Tk
# keeps window open
root.mainloop() #always keep GUI running 