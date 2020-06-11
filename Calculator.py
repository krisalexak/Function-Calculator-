from tkinter import *
from math import *

class Calc():
    def __init__(self,master):
        self.v=IntVar()
        self.v.set(1)
        self.operator="0"
        self.operation=""
        self.text_Input=StringVar()
        self.text_Input.set("0")
        self.text_Operation=StringVar()
        self.text_Operation.set("")
        
        displayFrame=Frame(master,borderwidth=1,bg="blue")
        displayFrame.grid(column=0, row=0,sticky=W+E)
        displayFrame.columnconfigure(0, weight=1)
        buttonFrame=Frame(master)
        buttonFrame.grid(column=0, row=1,sticky=W+E)
        buttonFrame.columnconfigure(0, weight=1,uniform='a')
        buttonFrame.columnconfigure(1, weight=1,uniform='a')
        buttonFrame.columnconfigure(2, weight=1,uniform='a')
        
        operationEntry=Entry(displayFrame,textvariable=self.text_Operation,relief=SUNKEN,justify=RIGHT,bg="Lavender",borderwidth=1)
        operationEntry.grid(row=0,sticky=W+E,columnspan=3)

        displayEntry=Entry(displayFrame,textvariable=self.text_Input,relief=SUNKEN,justify=RIGHT,borderwidth=1)
        displayEntry.grid(row=1,sticky=W+E,columnspan=3) 

        sevenButton=Button(buttonFrame, text="7",command=lambda:calc.numberDisplay(7))
        sevenButton.grid(row=0,sticky=W+E,column=0)
        
        eightButton=Button(buttonFrame, text="8",command=lambda:calc.numberDisplay(8))
        eightButton.grid(row=0,sticky=W+E,column=1)

        nineButton=Button(buttonFrame, text="9",command=lambda:calc.numberDisplay(9))
        nineButton.grid(row=0,sticky=W+E,column=2)

        fourButton=Button(buttonFrame, text="4",command=lambda:calc.numberDisplay(4))
        fourButton.grid(row=1,sticky=W+E,column=0)

        fiveButton=Button(buttonFrame, text="5",command=lambda:calc.numberDisplay(5))
        fiveButton.grid(row=1,sticky=W+E,column=1)

        sixButton=Button(buttonFrame, text="6",command=lambda:calc.numberDisplay(6))
        sixButton.grid(row=1,sticky=W+E,column=2)

        oneButton=Button(buttonFrame, text="1",command=lambda:calc.numberDisplay(1))
        oneButton.grid(row=2,sticky=W+E,column=0)

        twoButton=Button(buttonFrame, text="2",command=lambda:calc.numberDisplay(2))
        twoButton.grid(row=2,sticky=W+E,column=1)

        threeButton=Button(buttonFrame, text="3",command=lambda:calc.numberDisplay(3))
        threeButton.grid(row=2,sticky=W+E,column=2)

        signButton=Button(buttonFrame, text="+/-",command=lambda:calc.inputSign())
        signButton.grid(row=3,sticky=W+E,column=0)

        zeroButton=Button(buttonFrame, text="0",command=lambda:calc.numberDisplay(0))
        zeroButton.grid(row=3,sticky=W+E,column=1)

        commaButton=Button(buttonFrame, text=".",command=lambda:calc.numberDisplay("."))
        commaButton.grid(row=3,sticky=W+E,column=2)
        
        equalsButton=Button(buttonFrame, text="=",command=lambda:calc.equals())
        equalsButton.grid(row=4,sticky=W+E,column=0)

        delButton=Button(buttonFrame, text="Del",command=lambda:calc.delLastInput())
        delButton.grid(row=4,sticky=W+E,column=1)

        clearButton=Button(buttonFrame, text="C",command=lambda:calc.clearDisplay())
        clearButton.grid(row=4,sticky=W+E,column=2)

        logButton=Button(buttonFrame, text="log10",command=lambda:calc.logDisplay())
        logButton.grid(row=5,sticky=W+E,column=0)

        powerButton=Button(buttonFrame, text="a^b",command=lambda:calc.powerDisplay())
        powerButton.grid(row=5,sticky=W+E,column=1)

        sqrButton=Button(buttonFrame, text="√",command=lambda:calc.sqrDisplay())
        sqrButton.grid(row=5,sticky=W+E,column=2)

        sinButton=Button(buttonFrame, text="sin",command=lambda:calc.sinDisplay())
        sinButton.grid(row=6,sticky=W+E,column=0)

        cosButton=Button(buttonFrame, text="cos",command=lambda:calc.cosDisplay())
        cosButton.grid(row=6,sticky=W+E,column=1)

        tanButton=Button(buttonFrame, text="tan",command=lambda:calc.tanDisplay())
        tanButton.grid(row=6,sticky=W+E,column=2)

        piButton=Button(buttonFrame, text="pi",command=lambda:calc.numberDisplay(pi))
        piButton.grid(row=7,sticky=W+E,column=2)

        radButton=Radiobutton(buttonFrame, text="rad", variable=self.v,value=1,command=lambda:calc.get_mode())
        radButton.grid(row=7,column=0,sticky=W+E)

        degButton=Radiobutton(buttonFrame, text="deg", variable=self.v,value=2,command=lambda:calc.get_mode())
        degButton.grid(row=7,column=1,sticky=W+E)
        
    def numberDisplay(self,x):
        if x==pi:                          
            self.operator=str(pi)                                   
            self.text_Input.set(self.operator)                      
            return 
        if self.operation!="":                                    
            if x!="." and "^" not in self.operation:                
                self.operator="0"                                   
                self.operation=""
                if  self.operator==str(0):                          
                    if x!=".":  
                         self.operator=str(x)
                    else:
                         self.operator= self.operator+str(x)
                else:
                    if x=="." and "." in  self.operator:
                        pass
                    else:
                         self.operator= self.operator+str(x)
                self.text_Operation.set("")
                self.text_Input.set( self.operator)
            elif "^" in  self.operation:
                if  self.operator=="":
                    self.operator=str(x)
                    self.text_Input.set(self.operator)
                else:
                    if  self.operator==str(0):
                        if x!=".":
                             self.operator=str(x)
                        else:
                             self.operator= self.operator+str(x)
                    else:
                        if x=="." and "." in  self.operator:
                            pass
                        else:
                             self.operator= self.operator+str(x)
                    self.text_Input.set( self.operator)
        else:
            if  self.operator==str(0):
                if x!=".":
                     self.operator=str(x)
                else:
                     self.operator= self.operator+str(x)
            else:
                if x=="." and "." in  self.operator:
                    pass
                else:
                     self.operator= self.operator+str(x)
            self.text_Input.set(self.operator)
            
    def inputSign(self):
        try:
            self.operator=str(float(self.operator)*-1) 
            self.text_Input.set(self.operator)
        except: ValueError

    def delLastInput(self): 
        if self.text_Operation.get()=="" or "^" in self.operation:
            if self.text_Input.get()!="0":
                self.operator=self.operator[:-1]
                self.text_Input.set(self.operator)

    def powerDisplay(self): 
        if "^" not in self.operation:
            self.operation=self.operator+"^"
            self.text_Operation.set(self.operation)
            self.operator=""
            self.text_Input.set("")
   
    def equals(self): 
        if "^" in self.operation:
            try:
                self.operator=str(pow(float(self.text_Operation.get()[:-1]),float(self.text_Input.get())))
                self.text_Operation.set(self.operation+self.text_Input.get())
                self.text_Input.set(self.operator)
                self.operation=""
            except:ValueError
        
    def clearDisplay(self):
        self.operator="0"
        self.text_Input.set("0")
        self.operation=""
        self.text_Operation.set("")

    def sqrDisplay(self):
        try:
            if "^" not in self.operation:
                self.operation="√("+self.operator+")"
                self.operator=str(eval(str(sqrt(float(self.operator)))))
                self.text_Input.set(self.operator)
                self.text_Operation.set(self.operation)
            else:
                self.operator=str(pow(float(self.operation[:-1]),sqrt(float(self.operator))))
                self.operation=self.text_Operation.get()+"√("+self.text_Input.get()+")"
                self.text_Operation.set(self.operation)
                self.text_Input.set(self.operator)
                self.operation=""
        except:ValueError    

    def sinDisplay(self):
        try:
            if "^" not in self.operation:
                self.operation="sin("+self.operator+")"
                if self.v.get()==1:
                    self.operator=str(round(sin(float(self.operator)),15))
                elif self.v.get()==2:
                    self.operator=str(round(sin(float(self.operator)*pi/180),15))
                self.text_Input.set(self.operator)
                self.text_Operation.set(self.operation)
            else:
                if self.v.get()==1:
                    self.operator=str(pow(float(self.operation[:-1]),round(sin(float(self.operator)),15)))
                elif self.v.get()==2:
                    self.operator=str(pow(float(self.operation[:-1]),round(sin(float(self.operator)*pi/180),15)))
                self.operation=self.text_Operation.get()+"sin("+self.text_Input.get()+")"
                self.text_Operation.set(self.operation)
                self.text_Input.set(self.operator)
                self.operation=""
        except: ValueError
            


    def cosDisplay(self):
        try:
            if "^" not in self.operation:
                self.operation="cos("+self.operator+")"
                if self.v.get()==1:
                    self.operator=str(round(cos(float(self.operator)),15))
                elif self.v.get()==2:
                    self.operator=str(round(cos(float(self.operator)*pi/180),15))
                self.text_Input.set(self.operator)
                self.text_Operation.set(self.operation)
            else:
                if self.v.get()==1:
                    self.operator=str(pow(float(self.operation[:-1]),round(cos(float(self.operator)),15)))
                elif self.v.get()==2:
                    self.operator=str(pow(float(self.operation[:-1]),round(cos(float(self.operator)*pi/180),15)))
                self.operation=self.text_Operation.get()+"cos("+self.text_Input.get()+")"
                self.text_Operation.set(self.operation)
                self.text_Input.set(self.operator)
                self.operation=""
        except: ValueError
        
    def tanDisplay(self):
        try:
            if "^" not in self.operation:
                self.operation="tan("+self.operator+")"
                if self.v.get()==1:
                    self.operator=str(round(tan(float(self.operator)),15))
                elif self.v.get()==2:
                    self.operator=str(round(tan(float(self.operator)*pi/180),15))
                self.text_Input.set(self.operator)
                self.text_Operation.set(self.operation)
            else:
                if self.v.get()==1:
                    self.operator=str(pow(float(self.operation[:-1]),round(tan(float(self.operator)),15)))
                elif self.v.get()==2:
                    self.operator=str(pow(float(self.operation[:-1]),round(tan(float(self.operator)*pi/180),15)))
                self.operation=self.text_Operation.get()+"tan("+self.text_Input.get()+")"
                self.text_Operation.set(self.operation)
                self.text_Input.set(self.operator)
                self.operation=""
        except: ValueError


    def logDisplay(self):
        try:
            if "^" not in self.operation:
                self.operation="log10("+self.operator+")"
                self.operator=str(eval(self.operation))
                self.text_Input.set(self.operator)
                self.text_Operation.set(self.operation)
            else:
                self.operator=str(pow(float(self.operation[:-1]),log10(float(self.operator))))
                self.operation=self.text_Operation.get()+"log("+self.text_Input.get()+")"
                self.text_Operation.set(self.operation)
                self.text_Input.set(self.operator)
                self.operation=""
        except:ValueError

    def get_mode(self):
        if self.v.get()==1:
            mode="rad"
        elif self.v.get()==2:
            mode="degree"   
        return mode

root=Tk()
root.title('Calculator')
root.geometry("246x248")
root.columnconfigure(0, weight=1)
calc=Calc(root)

root.mainloop()

