# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 13:28:50 2021

@author: Ballhow
"""
import tkinter as tk

class CalculatorCUI:
    def __init__(self, mainForm = tk.Tk()):
        self.mainForm = mainForm
        self.CreateComponents()
        self.mainForm.mainloop()
        self.equalButton
# ------------ Component Callback ------------
# All Clear Button Callback
    def ACButtonCallBack(self):
        self.hisLabel['text'] = ''
        self.nowLabel['text'] = '0'
# Sign Change Button Callback
    def SignButtonCallback(self):
        if self.nowLabel['text'][0] != '-':
            self.nowLabel['text'] = '-' + self.nowLabel['text']
        else:
            self.nowLabel['text'] = self.nowLabel['text'][1:]
# Back Button CallBack
    def BackButtonCallBack(self):
        if self.nowLabel['text'] != '0' and not self.nowLabelResetFlag:
            self.nowLabel['text'] = self.nowLabel['text'][:-1]
        if len(self.nowLabel['text'] ) == 0:
            self.nowLabel['text'] = '0'
# Arithmetic Button Callback
    def ArithmeticButtonCallBack(self, btnText):
        if not self.hisLabel['text'] or self.hisLabel['text'][-1] == '=':
            self.hisLabel['text'] = self.nowLabel['text'] + btnText
        elif self.nowLabelResetFlag:
            self.hisLabel['text'] = self.hisLabel['text'][:-1] + btnText
        else:
            equation = self.hisLabel['text'] + self.nowLabel['text']
            equation = equation.replace("÷","/")
            equation = equation.replace("×","*")
            value = eval(equation)
            self.nowLabel['text'] = str(value)
            self.hisLabel['text'] = self.nowLabel['text'] + btnText
        self.nowLabelResetFlag = True
# Equal Button Callback
    def EqualButtonCallback(self):
        if not self.hisLabel['text'] or self.hisLabel['text'][-1] == '=':
            self.hisLabel['text'] = self.nowLabel['text'] + '='
        else:
            self.hisLabel['text'] = self.hisLabel['text'] + self.nowLabel['text'] + '='
            equation = self.hisLabel['text'][:-1]
            equation = equation.replace("÷","/")
            equation = equation.replace("×","*")
            value = eval(equation)
            self.nowLabel['text'] = str(value)
        self.nowLabelResetFlag = True
# Number Button CallBack
    def NumberButtonCallBack(self, text):
        if text == '.':
            self.nowLabel['text'] = self.nowLabel['text'] + text
        elif self.nowLabel['text'] == '0' or self.nowLabelResetFlag:
            self.nowLabel['text'] = text
        else:
            self.nowLabel['text'] += text
        self.nowLabelResetFlag = False
# Key Board Press Monitor
    def KeyPressMonitor(self, event):
        if event.keycode == 27: # "ESC" key
            self.acButton.invoke()
        elif event.keycode == 8: # "BackSpace" key
            self.backButton.invoke()
        elif event.char == '=' or event.keycode == 13: # The "=" and "Enter" key
            self.equalButton.invoke()
        elif event.char == '/':
            self.devideButton.invoke()
        elif event.char == '*':
            self.multiplyButton.invoke()
        elif event.char == '-':
            self.minusButton.invoke()
        elif event.char == '+':
            self.plusButton.invoke()
        elif event.char.isnumeric():
            self.numButton[int(event.char)].invoke()
        elif event.char == '.':
            self.numButton[10].invoke()
            
# ------------ Create component of Form ------------
    def CreateComponents(self):
    # Parameters
        self.backgrondColor = '#272727' # Backgrond Color
        self.fontType = 'Calibri' # Font type
        self.fontColor = '#FFFFFF' # Font Color
        self.nowLabelResetFlag = False
    # Main Form
        self.mainForm.geometry('300x500')
        self.mainForm['bg'] = self.backgrondColor
        self.mainForm.title('Calculator')
        self.mainForm.bind("<Key>", self.KeyPressMonitor)
    # History Label
        self.hisLabel = tk.Label(self.mainForm)
        self.hisLabel['bg'] = self.backgrondColor
        self.hisLabel['fg'] = self.fontColor
        self.hisLabel['text'] = ''
        self.hisLabel['font'] = (self.fontType,12)
        self.hisLabel['anchor'] = 'e'
        self.hisLabel.grid(column = 0, row = 0, columnspan = 4, sticky = 'nswe')
    # Now Label
        self.nowLabel = tk.Label(self.mainForm)
        self.nowLabel['bg'] = self.backgrondColor
        self.nowLabel['fg'] = self.fontColor
        self.nowLabel['text'] = '0'
        self.nowLabel['font'] = (self.fontType, 25,'bold')
        self.nowLabel['anchor'] = 'e'
        self.nowLabel.grid(column = 0, row = 1, columnspan = 4, sticky = 'nswe')
    # All Clear Button
        self.acButton = self.SpectialButton('AC', 0, 2)
        self.acButton['command'] = self.ACButtonCallBack
    # Sign Button
        self.signButton = self.SpectialButton('±', 1, 2)
        self.signButton['command'] = self.SignButtonCallback
    # Back Button
        self.backButton = self.SpectialButton('<<', 2, 2)
        self.backButton['command'] = self.BackButtonCallBack
    # Arithmetic Button
        self.devideButton = self.ArithmeticButton('÷', 3, 2)
        self.devideButton['command'] = lambda btnText = '÷': self.ArithmeticButtonCallBack(btnText)
        self.multiplyButton = self.ArithmeticButton('×', 3, 3)
        self.multiplyButton['command'] = lambda btnText = '×': self.ArithmeticButtonCallBack(btnText)
        self.minusButton = self.ArithmeticButton('-', 3, 4)
        self.minusButton['command'] = lambda btnText = '-': self.ArithmeticButtonCallBack(btnText)
        self.plusButton = self.ArithmeticButton('+', 3, 5)
        self.plusButton['command'] = lambda btnText = '+': self.ArithmeticButtonCallBack(btnText)
        self.equalButton = self.ArithmeticButton('=', 3, 6)
        self.equalButton['command'] = self.EqualButtonCallback
    # Number Button
        self.numButton = []
        for i in range(10):
            self.numButton.append(self.NumberButton(str(i), (i-1)%3, 5-(i-1)//3))
            self.numButton[i]['command'] = lambda text = str(i): self.NumberButtonCallBack(text)
        self.numButton[0].grid(column = 0, row = 6, columnspan = 2)
        
        self.numButton.append(self.NumberButton('.', 2, 6))
        self.numButton[10]['command'] = lambda text = '.': self.NumberButtonCallBack(text)
    # Grid Weight Setting
        # Column weight setting
        for i in range(4):
            self.mainForm.columnconfigure(i, weight = 1)
        # Row weight setting
        self.mainForm.rowconfigure(0, weight = 1)
        for i in range(1,7):
            self.mainForm.rowconfigure(i, weight = 2)
# ------------ Sub-Function for Create Components ------------
    # Special Button as "AC, ±, <<"
    def SpectialButton(self, text, col, row):
        btn = tk.Button(self.mainForm,
                        bg = '#D0D0D0',
                        text = text, 
                        font = ('Calibri', 20, 'bold'),
                        width = 3)
        btn.grid(column = col, row = row, padx = 1, pady = 1, sticky = 'nswe')
        return btn
    # Arithmetic Button as "+, -, ×, ÷"
    def ArithmeticButton(self, text, col, row):
        btn = tk.Button(self.mainForm,
                        bg = '#FF9224',
                        text = text,
                        font = ('Calibri', 20, 'bold'),
                        width = 3)
        btn.grid(column = col, row = row, padx = 1, pady = 1, sticky = 'nswe')
        return btn
    # Number Button as "0 ~ 9"
    def NumberButton(self, text, col, row):
        btn = tk.Button(self.mainForm,
                        bg = '#4F4F4F',
                        fg = '#FFFFFF',
                        text = text,
                        font = ('Calibri', 20, 'bold'),
                        width = 3)
        btn.grid(column = col, row = row, padx = 1, pady = 1, sticky = 'nswe')
        return btn
# -------------- Main Code --------------
calculator = CalculatorCUI()
