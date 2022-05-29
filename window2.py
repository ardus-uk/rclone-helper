import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

event, values  = sg.Window('SHA-1 & 256 Hash', [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                        [sg.InputText(), sg.FileBrowse()],
                        [sg.Submit(), sg.Cancel()]]).read(close=True)

source_filename = values[0]     # the first input element is values[0]