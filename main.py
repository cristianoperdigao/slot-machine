#!/usr/bin/python

# This script is a simulator of slot machine
#
# Example usage:
#  python3 main.py
#
# Learn more: https://github.com/cristianoperdigao/slot-machine

from tkinter import *

from PIL import Image, ImageTk
import random
import time


class App:
    def __init__(self):
        # Create instance
        self.window = Tk()

        # Configs
        self.setConfigs()

        # Draw page
        self.drawUI()

    def setConfigs(self):
        # Set screen size
        self.w, self.h = self.window.winfo_screenwidth(), self.window.winfo_screenheight()

        # Bring it to the front and keep always
        self.window.title("SLOT MACHINE SIMULATOR")

        # self.window.attributes("-fullscreen", True)
        self.window.geometry("%dx%d" % (self.w, self.h))

    def drawUI(self):
        self.alive = True

        # Set valuable for each row or column
        self.window.columnconfigure(0, weight=1)
        self.window.columnconfigure(1, weight=1)
        self.window.columnconfigure(2, weight=1)
        self.window.rowconfigure(1, weight=2)

        headerText = Label(self.window, text="minimal unlimited experience about slots", bg="white", fg="grey", font=('Verdana', 24, 'bold'))
        headerText.grid(column=0, row=0, columnspan=3, ipadx=20, ipady=20, sticky="NSEW")

        # Set slots box
        canvasOne = Canvas(self.window, width=(self.w / 3.5), height=(self.h / 3), background="white", highlightthickness=1, highlightbackground="black")
        canvasTwo = Canvas(self.window, width=(self.w / 3.5), height=(self.h / 3), background="white",highlightthickness=1, highlightbackground="black")
        canvasThree = Canvas(self.window, width=(self.w / 3.5), height=(self.h / 3), background="white", highlightthickness=1, highlightbackground="black")

        # pack the canvas into a frame/form
        canvasOne.pack()
        canvasTwo.pack()
        canvasThree.pack()

        canvasOne.grid(column=0, row=1, padx=50, pady=4, sticky="NW")  # NSEW
        canvasTwo.grid(column=1, row=1, padx=50, pady=4, sticky="NW")  # NSEW
        canvasThree.grid(column=2, row=1, padx=50, pady=4, sticky="NW")  # NSEW

        # 1
        openMainImage = Image.open("slot_machine_symbols.png")

        # spin a few times through before stopping
        spinsTotal = 100

        # Resize the images
        resizeWidth = (int(self.w / 3.5) - 120)
        resizeHeigth = (int(self.h / 3))

        # Array image list
        imageCoordinates = [
            openMainImage.crop([0, 0, 300, 300]),  # Cherry
            openMainImage.crop([300, 0, 600, 300]),  # Diamond
            openMainImage.crop([600, 0, 900, 300]),  # Clevor
            openMainImage.crop([0, 300, 300, 600]),  # Grapes
            openMainImage.crop([300, 300, 600, 600]),  # Lemon
            openMainImage.crop([600, 300, 900, 600]),  # Seven
            openMainImage.crop([0, 600, 335, 900]),  # Melon
            openMainImage.crop([330, 600, 600, 900]),  # Horseshoe
            openMainImage.crop([600, 600, 900, 900]),  # Bell
        ]

        # Creating a photoimage object to use image
        openSpinImage = Image.open("spin.jpg")
        openSpinImage.resize((40, 50), Image.ANTIALIAS)
        btnSpinPhoto = ImageTk.PhotoImage(openSpinImage)

        self.spinText = Label(self.window, text="press <space> to spin", bg="white", fg="grey", font=('Verdana', 24, 'bold'))
        self.spinText.grid(column=0, row=2, columnspan=3, padx=0, pady=130, ipady=1, sticky=N)

        self.btnSpin = Label(self.window, image=btnSpinPhoto, bg="white", fg="grey", font=('Verdana', 24, 'bold'))
        self.btnSpin.grid(column=0, row=2, columnspan=3, padx=0, pady=0, ipady=1, sticky=N)

        # Start column One
        i = random.randint(0, len(imageCoordinates) - 1)
        imageCoordinates[i].resize((resizeWidth, resizeHeigth), Image.ANTIALIAS)
        tkImgSlotOne = ImageTk.PhotoImage(imageCoordinates[i])
        canvasOne.create_image(0, 0, anchor=NW, image=tkImgSlotOne)

        # Start column Two
        i = random.randint(0, len(imageCoordinates) - 1)
        imageCoordinates[i].resize((resizeWidth, resizeHeigth), Image.ANTIALIAS)
        tkImgSlotTwo = ImageTk.PhotoImage(imageCoordinates[i])
        canvasTwo.create_image(0, 0, anchor=NW, image=tkImgSlotTwo)

        # Start column Three
        i = random.randint(0, len(imageCoordinates) - 1)
        imageCoordinates[i].resize((resizeWidth, resizeHeigth), Image.ANTIALIAS)
        tkImgSlotThree = ImageTk.PhotoImage(imageCoordinates[i])
        canvasThree.create_image(0, 0, anchor=NW, image=tkImgSlotThree)

        self.window.bind('<space>', lambda event=None: self.spin(100, imageCoordinates, resizeWidth, resizeHeigth, [canvasOne, canvasTwo, canvasThree]))
        self.window.mainloop()

    def spin(self, spins, images, resizeWidth, resizeHeigth, canvas):
        print("spinning...")
        speedAmount = 0
        self.btnSpin["state"] = DISABLED
        self.spinText["state"] = DISABLED

        self.spinText.grid_remove()

        for spin in range(0, 20):
            slotOne = random.randint(0, len(images) - 1)
            slotTwo = random.randint(0, len(images) - 1)
            slotThree = random.randint(0, len(images) - 1)
            time.sleep((speedAmount * 2.4) / 1000)

            images[slotOne].resize((resizeWidth, resizeHeigth), Image.ANTIALIAS)
            images[slotTwo].resize((resizeWidth, resizeHeigth), Image.ANTIALIAS)
            images[slotThree].resize((resizeWidth, resizeHeigth), Image.ANTIALIAS)

            tkImgSlotOne = ImageTk.PhotoImage(images[slotOne])
            tkImgSlotTwo = ImageTk.PhotoImage(images[slotTwo])
            tkImgSlotThree = ImageTk.PhotoImage(images[slotThree])

            canvas[0].delete('all')
            canvas[0].create_image(50, 0, anchor=NW, image=tkImgSlotOne)
            canvas[0].update()

            canvas[1].delete('all')
            canvas[1].create_image(50, 0, anchor=NW, image=tkImgSlotTwo)
            canvas[1].update()

            canvas[2].delete('all')
            canvas[2].create_image(50, 0, anchor=NW, image=tkImgSlotThree)
            canvas[2].update()

            speedAmount += 5

        print("spinning finished.")
        self.spinText.grid()
        self.btnSpin["state"] = NORMAL

        self.window.mainloop()

if __name__ == '__main__':
    App()
