# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 13:00:15 2021

@author: Ballhow
"""

import tkinter as tk
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Cubic3D:
    def __init__(self, mainForm = tk.Tk()):
        self.mainForm = mainForm
        self.CreateComponent()
        self.Parameters()
        self.mainForm.mainloop()
    # -------------- Sub Fucntion --------------
    def Parameters(self):
        self.point = -np.ones([8,3])
        self.point[np.arange(8)%2 == 1, 0] = 1
        self.point[np.arange(8)%4 >= 2, 1] = 1
        self.point[np.arange(8)   >= 4, 2] = 1
        
        self.xlim_num = np.array([-2,2])
        self.ylim_num = np.array([-2,2])
        
        self.CubicPlot(self.point)
        
    def Rotate(self, point, axis, degree):
        axis = axis / np.sqrt((axis**2).sum()) # Axis normalized
        length = point.shape[0]
        p = np.concatenate((np.zeros((length,1)),point), axis=1)
        q = np.zeros([length,4])
        q_conj = np.zeros([length,4])
        q[:,0] = q_conj[:,0] = np.cos(degree/2/180*np.pi)
        q[:,1:] = np.sin(degree/2/180*np.pi) * axis
        q_conj[:,1:] = -np.sin(degree/2/180*np.pi) * axis
        p = self.Quaternion(q,self.Quaternion(p,q_conj))
        return p[:,1:]
        
    def Quaternion(self, a, b):
        length = a.shape[0]
        output = np.zeros((length,4))
        output[:,0] = a[:,0]*b[:,0] - a[:,1]*b[:,1] - a[:,2]*b[:,2] - a[:,3]*b[:,3]
        output[:,1] = a[:,0]*b[:,1] + a[:,1]*b[:,0] + a[:,2]*b[:,3] - a[:,3]*b[:,2]
        output[:,2] = a[:,0]*b[:,2] + a[:,2]*b[:,0] + a[:,3]*b[:,1] - a[:,1]*b[:,3]
        output[:,3] = a[:,0]*b[:,3] + a[:,3]*b[:,0] + a[:,1]*b[:,2] - a[:,2]*b[:,1]
        return output
    # -------------- Component Callback --------------
    def CubicPlot(self, point):
        self.axes.clear()
        color_num = np.copy(point[:,2])
        color_num -= color_num.min()
        color_num /= color_num.max()
        color_matrix = np.zeros([point.shape[0],3])
        color_matrix[:,1] = color_num
    # Line Plot
        color_line = [0,0.9,0]
        line_list = np.array([0,1,3,2,0])
        self.axes.plot(point[line_list,0], point[line_list,1], color = color_line)
        line_list += 4
        self.axes.plot(point[line_list,0], point[line_list,1], color = color_line)
        for i in range(4):
            self.axes.plot(point[[i,i+4],0], point[[i,i+4],1], color = color_line)
    # Point Plot
        self.axes.scatter(point[:,0], point[:,1], s = 100, color = color_matrix)
        self.axes.set_xlim(self.xlim_num)
        self.axes.set_ylim(self.ylim_num)
        self.canvasBox.draw()
        
    def RotateStart(self, e):
        self.rotary_center = np.array([e.x, e.y]);
        self.canvasBox.get_tk_widget()['cursor'] = "exchange"
        
    def RotateMotion(self, e):
        offset = np.array([e.x,e.y]) - self.rotary_center
        offset[1] = -offset[1] # sign convention between "axes" and "canvas coordinate"
        rotary_axis = np.array([-offset[1], offset[0], 0])
        degree = np.sqrt((offset**2).sum()) * 360 / self.canvasBox.get_width_height()[0]
        if degree == 0:
            return
        self.point = self.Rotate(self.point, rotary_axis, degree)
        self.CubicPlot(self.point)
        self.rotary_center = np.array([e.x,e.y])
        
    def MoveStart(self, e):
        self.move_center = np.array([e.x, e.y])
        self.canvasBox.get_tk_widget()['cursor'] = "fleur"
    
    def MoveMotion(self, e):
        offset = np.array([e.x, e.y]) - self.move_center
        offset[1] = -offset[1] # sign convention between "axes" and "canvas coordinate"
        offset = offset * 5 / self.canvasBox.get_width_height()[0]
        self.xlim_num = self.xlim_num - offset[0]
        self.ylim_num = self.ylim_num - offset[1]
        self.CubicPlot(self.point)
        self.move_center = np.array([e.x, e.y])
        
    def ActionEnd(self, e):
        self.canvasBox.get_tk_widget()['cursor'] = "arrow"
    
    def MouseScroll(self, e):
        if e.delta > 0:
            self.xlim_num = self.xlim_num * 0.95
            self.ylim_num = self.ylim_num * 0.95
        else:
            self.xlim_num = self.xlim_num / 0.95
            self.ylim_num = self.ylim_num / 0.95
        
        self.CubicPlot(self.point)
            
    def MainFormSizeChange(self, e):
        h = round(self.mainForm.winfo_height()/1.2)
        w = self.mainForm.winfo_width()-4
        hw = h if h < w else w
        self.canvasBox.get_tk_widget()['height'] = hw
        self.canvasBox.get_tk_widget()['width'] = hw
# -------------- Create component of Form --------------
    def CreateComponent(self):
    # Parameters
        self.fontType = 'Calibri' # Font type
    # Main Form
        self.mainForm.geometry('500x500')
        self.mainForm.title('3D Cubic Rotation')
        self.mainForm.bind("<Configure>", self.MainFormSizeChange)
    # Label Text
        self.desLabel = tk.Label(self.mainForm, 
                            font = (self.fontType, 12, 'italic'),
                            text = 'Mouse: <Right-Drag> Move / <Left-Drag> Rotate')
        self.desLabel.grid(column = 0, row = 0, sticky = 'nwse')
    # Canvas
        self.fig = Figure(figsize=(4,4), dpi=100) # Create Figure for canvas
        self.axes = self.fig.add_axes([0.1, 0.1, 0.8, 0.8])
        self.canvasBox = FigureCanvasTkAgg(self.fig, master = self.mainForm)
        self.canvasBox.get_tk_widget().bind("<Button-1>", self.RotateStart)
        self.canvasBox.get_tk_widget().bind("<B1-Motion>", self.RotateMotion)
        self.canvasBox.get_tk_widget().bind("<ButtonRelease-1>", self.ActionEnd)
        self.canvasBox.get_tk_widget().bind("<Button-3>", self.MoveStart)
        self.canvasBox.get_tk_widget().bind("<B3-Motion>", self.MoveMotion)
        self.canvasBox.get_tk_widget().bind("<ButtonRelease-3>", self.ActionEnd)
        self.canvasBox.get_tk_widget().bind("<MouseWheel>", self.MouseScroll)
        self.canvasBox.get_tk_widget().grid(column = 0, row = 1)
    # Button (Reset)
        self.resetButton = tk.Button(self.mainForm,
                                     text = 'Reset',
                                     command = self.Parameters)
        self.resetButton.grid(column = 0, row = 2, padx = 100, pady = 5, sticky = 'nwse')
        
        self.mainForm.columnconfigure(0, weight = 1)
        self.mainForm.rowconfigure(0, weight = 1)
        self.mainForm.rowconfigure(1, weight = 10)
        self.mainForm.rowconfigure(2, weight = 1)
    
# -------------- main code --------------
cubic = Cubic3D()
