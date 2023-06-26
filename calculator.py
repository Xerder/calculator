import tkinter,math

class Calculator():
    def __init__(self):
        self.window = tkinter.Tk()
        self.window.resizable(0,0)
        self.window.geometry("270x607")
        self.window.title("Калькулятор")
        self.digits={7:(1,1),8:(1,2),9:(1,3),
                     4:(2,1),5:(2,2),6:(2,3),
                     1:(3,1),2:(3,2),3:(3,3),
                     0:(4,2)}
        self.oper_digits={"+":(2,4),"-":(1,4),"*":(4,4),":":(3,4),
                          "=":(4,3),".":(4,1),
                          "%":(5,1),"C":(5,2),"<-":(5,3)}
        self.current_text = ""

    def run(self):
        self.window.mainloop()

    

    def create_buttons_frame(self):
        self.but_frame = tkinter.Frame(self.window,height=400,width=375)
        self.but_frame.place(x=0,y=201,width=375,height=467)



    def create_buttons(self):
        for digit,position in self.digits.items():
            button = tkinter.Button(self.but_frame,text=digit,command=lambda x=digit:self.button_handler(str(x)))
            button.grid(row=position[0],column = position[1],sticky=tkinter.NSEW)
            


    def create_operator_buttons(self):
        i = 0
        for oper_digit,position in self.oper_digits.items():
            button = tkinter.Button(self.but_frame,text=oper_digit,command=lambda x=oper_digit:self.button_handler(str(x)))
            button.grid(row=position[0],column = position[1],sticky=tkinter.NSEW)
            self.but_frame.rowconfigure(i,weight=1)
            self.but_frame.columnconfigure(i,weight=1)
            i +=1
       

    def create_display_frame(self):
        self.display_frame = tkinter.Frame(self.window,height=100,width = 100,background="lightgray")
        self.display_frame.place(x = 0,y=0,height=200,width=270)
        



    def display_create(self):
        self.label = tkinter.Label(self.display_frame, anchor= tkinter.E,text=self.current_text,background="lightgray",foreground="black")
        self.label.pack(side="right")
        
    def button_handler(self,text):
        if text == "=":
            self.current_text = eval(self.current_text)
        elif text =="C":
            self.current_text = ""
        elif text =="<-":
            self.current_text = self.current_text[:-1]
        else:
            self.current_text += text
        self.label.configure(text=self.current_text)





def main():
    calc = Calculator()
    calc.create_display_frame()
    calc.display_create()
    calc.create_buttons_frame()
    calc.create_buttons()
    calc.create_operator_buttons()
    calc.run()


if __name__ =="__main__":
    main()