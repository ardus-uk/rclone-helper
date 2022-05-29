#!/usr/bin/env python3
# 
import PySimpleGUI as sg
import sys
import os


event, values = sg.Window('Local Directory Selection',
                [[sg.Text('Select local directory')],
                [sg.In(), sg.FolderBrowse()],
                [sg.Open(), sg.Cancel()]]).read(close=True)
if values[0]:
    fname = values[0]
else:
    fname = os.getcwd()

remote = fname.split("/")
print(remote)


if not fname:
    sg.popup("Cancel", "No directory name supplied")
    raise SystemExit("Cancelling: no directory name supplied")
else:
    layout = [[sg.Text("Local: "+fname)],
          [sg.Text("Remote: "+remote[4]+":"+os.path.basename(fname))],
          [sg.Text("DIRECTION------------------------------------------------")],
          [sg.T("         "), sg.Radio('Local to Remote', "RADIO1", default=True, key="-IN1-")],
          [sg.T("         "), sg.Radio('Remote to Local', "RADIO1", default=False)],
          [sg.Text("COPY/CLONE---------------------------------------------")],         
          [sg.T("         "), sg.Radio('Copy', "RADIO2", default=True, key="-IN2-")],
          [sg.T("         "), sg.Radio('Clone', "RADIO2", default=False)],
          [sg.Text("---------------------------------------------------------------")],
          [sg.T("         "), sg.Checkbox('Selection active', default=False, key="-SEL-")],
          [sg.T("")],[sg.T("        "), sg.Button("Action",size=(12,4))], [sg.T("")]]

###Setting Window
    window = sg.Window('rclone assistant', layout, size=(500,400))

###Showing the Application, also GUI functions can be placed here.

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event=="Exit":
            break
        if values["-SEL-"] == True:
            if values["-IN1-"] == True:
                if values["-IN2-"] == True:
                    print("Local to Remote Copy")
                else:
                    print("Local to Remote Clone")
            else:
                if values["-IN2-"] == True:
                    print("Remote to Local Copy")
                else:
                    print("Remote to Local Clone")
            
    window.close()
