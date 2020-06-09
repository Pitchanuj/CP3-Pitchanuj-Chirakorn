from tkinter import *
import math

def leftClickButton(event):
    BMI = float(textBoxWeight.get())/ math.pow(float(textBoxHeight.get())/100,2)
    labelBMI.configure(text = BMI)
    if BMI >= 30:
        labelResult.configure(text = "อ้วนมาก",fg = "red")
    elif BMI >= 25:
        labelResult.configure(text = "อ้วน",fg = "red")
    elif BMI >= 23:
        labelResult.configure(text = "น้ำหนักเกิน",fg = "red")
    elif BMI >= 18.6:
        labelResult.configure(text = "น้ำหนักปกติ เหมาะสม",fg = "green")
    else:
        labelResult.configure(text = "ผอมเกินไป",fg = "red")
    print(BMI)



MainWindow = Tk()
labelHeight = Label(MainWindow,text = "ส่วนสูง (cm.)")
labelHeight.grid(row = 0,column = 0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row = 0 , column = 1)
labelWeight = Label(MainWindow,text = "น้ำหนัก (Kg.)")
labelWeight.grid(row = 1,column = 0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row = 1 , column = 1)
calculateButton = Button(MainWindow, text = "คำนวน")
calculateButton.grid(row = 2, column = 0)
calculateButton.bind('<Button-1>',leftClickButton)
labelBMI = Label(MainWindow,text = "ผลลัพธ์")
labelBMI.grid(row = 2,column = 1)
labelResult = Label(MainWindow,text = "",font =("Angsana New",14))
labelResult.grid(row = 3,column = 1)

MainWindow.mainloop()

