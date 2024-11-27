from tkinter import *

#window
window = Tk()
window.title("BMI")
window.minsize(width=400, height=300)

#başlık
label = Label(text="BMI CALCULATOR")
label.config(bg="black")
label.config(fg=("white"))
label.config(padx=10,pady=10)

label.pack()
def button_clicked():
    height = label_üç.get()
    weight = label_iki.get()
    if weight == "" or height =="":
        result_label.config(text="Enter both weight and height!")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")

#kilogram
label_2 = Label(text="Enter your kilogram")
label_2.config(fg="blue")
label_iki = Entry(width=10)

label_2.pack()
label_iki.pack()

#boy
label_3 = Label(text="enter your height")
label_3.config(fg="blue")
label_üç = Entry(width=10)

label_3.pack()
label_üç.pack()

#button

button = Button(text="calculate", command=button_clicked)
button.config(padx=10, pady=10)
button.pack()

result_label = Label()
result_label.pack()
def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 2)}. You are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese class 1"
    elif 35 < bmi <= 40:
        result_string += "obese class 2"
    else:
        result_string += "obese class 3"
    return result_string
window.mainloop()