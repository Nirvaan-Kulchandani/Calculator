from tkinter import *

calc = Tk()
calc.config(bg="cyan")

calc.geometry("254x368")
calc.resizable(False, False)
calc.title("Nirvaan Calculator")

text = None
def press_btn_text(x):
    global text
    if x == btn1:
        text = x.cget("text")
    if x == btn2:
        text = x.cget("text")
    if x == btn3:
        text = x.cget("text")
    if x == btn4:
        text = x.cget("text")
    if x == btn5:
        text = x.cget("text")
    if x == btn6:
        text = x.cget("text")
    if x == btn7:
        text = x.cget("text")
    if x == btn8:
        text = x.cget("text")
    if x == btn9:
        text = x.cget("text")
    if x == btn0:
        text = x.cget("text")
    if x == btn_add:
        text = x.cget("text")
    if x == btn_minus:
        text = x.cget("text")
    if x == btn_multiply:
        text = x.cget("text")
    if x == btn_divide:
        text = x.cget("text")
    output.configure(text=(output.cget("text")) + text)
    if x == btn_clear:
        output.config(text="")    
    

def evaluate():
    values = str(output.cget("text"))
    result = str(eval(values))
    output.config(text=result)

output = Label(calc, font=("comicansms 20 bold"), bg="grey94", relief="flat", bd=10, width=13)

output.grid(row=0, column=0, columnspan=4)

font_num = "Algerian 30 bold italic"

# buttons = [
#     ("1",2,0),
#     ("2",2,1),
#     ("3",2,2),
#     ("4",3,0),
#     ("5",3,0),
#     ("6",3,0),
#     ("7",4,0),
#     ("8",4,0),
#     ("9",4,0),
#     ("0",5,0),
#     ("=",2,0),
#     ("+",2,0),
#     ("-",2,0),
#     ("÷",2,0),
#     ("×",2,0),
#     ("C",2,0),
# ]

btn1 = Button(calc, text="1", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn1))
btn1.grid(row=2, column=0)

btn2 = Button(calc, text="2", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn2))
btn2.grid(row=2, column=1)

btn3 = Button(calc, text="3", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn3))
btn3.grid(row=2, column=2)

btn4 = Button(calc, text="4", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn4))
btn4.grid(row=3, column=0)

btn5 = Button(calc, text="5", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn5))
btn5.grid(row=3, column=1)

btn6 = Button(calc, text="6", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn6))
btn6.grid(row=3, column=2)

btn7 = Button(calc, text="7", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn7))
btn7.grid(row=4, column=0)

btn8 = Button(calc, text="8", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn8))
btn8.grid(row=4, column=1)

btn9 = Button(calc, text="9", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn9))
btn9.grid(row=4, column=2)

btn0 = Button(calc, text="0", font="algerian 29 bold italic", fg="aquamarine4", bg="antiquewhite", padx=2, command=lambda: press_btn_text(btn0))
btn0.grid(row=5, column=1)

btn_equal = Button(calc, text="=", font=font_num, fg="aquamarine4", bg="antiquewhite", command=evaluate)
btn_equal.grid(row=2, column=3)

btn_add = Button(calc, text="+", font=font_num, fg="aquamarine4", bg="antiquewhite", command=lambda: press_btn_text(btn_add))
btn_add.grid(row=3, column=3)

btn_minus = Button(calc, text="-", font=font_num, fg="aquamarine4", bg="antiquewhite", padx=6, command=lambda: press_btn_text(btn_minus))
btn_minus.grid(row=4, column=3)

btn_multiply = Button(calc, text="*", font="algerian 29 bold italic", fg="aquamarine4", bg="antiquewhite", padx=6, command=lambda: press_btn_text(btn_multiply))
btn_multiply.grid(row=5, column=3)

btn_divide = Button(calc, text="/", font="algerian 29 bold italic", fg="aquamarine4", bg="antiquewhite", padx=4, command=lambda: press_btn_text(btn_divide))
btn_divide.grid(row=5, column=2)

btn_clear = Button(calc, text="C", font="algerian 29 bold italic", fg="aquamarine4", bg="antiquewhite", padx=2, command=lambda: press_btn_text(btn_clear))
btn_clear.grid(row=5, column=0)



calc.mainloop()