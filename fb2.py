#!/usr/bin/env python3
# 
import PySimpleGUI as sg
import sys
import os
import subprocess

valid_remotes = subprocess.getoutput('rclone listremotes').splitlines()
print(valid_remotes)

event, values = sg.Window('Local Directory Selection',
                [[sg.Text('Select local directory')],
                [sg.In(), sg.FolderBrowse()],
                [sg.Open(), sg.Cancel()]]).read(close=True)
if values[0]:
    fname = values[0]
else:
    fname = os.getcwd()

if not os.path.isdir(fname):
    sg.popup(fname+" is not a valid directory")
    raise SystemExit("Cancelling - not a valid directory") 

remote_path_parts = fname.split("/")
print(len(remote_path_parts))
print(remote_path_parts)

remote = remote_path_parts[4]
remote_label = remote+":"
if len(remote_path_parts)>5:
    remote_tree = "/".join(remote_path_parts[-(len(remote_path_parts)-5):])
else:
    remote_tree = "/"+remote

print(remote)
print(remote_tree)

if remote_label not in valid_remotes:
    sg.popup(remote_label+" is not a valid Backblaze bucket")
    raise SystemExit("Cancelling - not a valid Backblaze bucket")   

if not fname:
    sg.popup("Cancel", "No directory name supplied")
    raise SystemExit("Cancelling: no directory name supplied")

remote_complete_description = remote_label+remote_tree

layout = [[sg.Text("Local: "+fname)],
          [sg.Text("Remote: "+remote_complete_description)],
          [sg.Text("DIRECTION------------------------------------------------")],
          [sg.T("         "), sg.Radio('Local to Remote', "DIRCTN", default=True, key="-IN1-")],
          [sg.T("         "), sg.Radio('Remote to Local', "DIRCTN", default=False)],
          [sg.Text("COPY/CLONE---------------------------------------------")],         
          [sg.T("         "), sg.Radio('Copy', "COSY", default=True, key="-IN2-")],
          [sg.T("         "), sg.Radio('Sync', "COSY", default=False)],
          [sg.Text("---------------------------------------------------------------")],
          [sg.T("         "), sg.Checkbox('Selection active', default=False, key="-SEL-")],
          [sg.T("")],[sg.T("        "), sg.Button("Action",size=(12,4))], [sg.T("")]]

###Setting Window
window = sg.Window('rclone assistant', layout, size=(500,400))

###Showing the Application, also GUI functions can be placed here.

event, values = window.read()

if event == sg.WIN_CLOSED or event=="Exit":
    raise SystemExit("Window closed")

if values["-SEL-"] == True:
    if values["-IN1-"] == True:
        if values["-IN2-"] == True:
            print("Local to Remote Copy")
            cmd = "rclone copy "+fname+" "+remote_complete_description
        else:
            print("Local to Remote Sync")
            cmd = "rclone sync "+fname+" "+remote_complete_description
    else:
        if values["-IN2-"] == True:
            print("Remote to Local Copy")
            cmd = "rclone copy "+remote_complete_description+" "+fname
        else:
            print("Remote to Local Sync")
            cmd = "rclone sync "+remote_complete_description+" "+fname
    print(cmd)
    subprocess.getoutput(cmd)
            
window.close()
