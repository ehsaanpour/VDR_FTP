import os
from ftplib import FTP
from sys import path
import PySimpleGUI as sg
from pathlib import Path

#login to FTP
def login_to(URL , user , passwd):
    global ftp
    ftp = FTP(URL)
    #ftp.connect()
    ftp.login (user,passwd)
    window['-comment10-'].update('Loging Successfully')

#identify the files name.
def file_name():
    global listing
    ftp.retrlines("LIST")
    ftp.cwd('clip') # or ftp.cwd("folderOne/subFolder")
    listing1 = []
    listing =[]
    filename = []
    ftp.retrlines("LIST", listing1.append)
    for file in listing1:
        words = file.split(None, 8)
        listing += [words[-1].lstrip()]
        # listing = filename.append
    window['-comment1-'].update(listing)
    return listing
    

#download files
# def download_All_file():
#     files = ftp.nlst()
#     folder_path = sg.PopupGetFolder('please open the folder')
#     print(folder_path)
#     for file in files:
# 	    print("Downloading..." + file)
#     window['-comment1-'].update(file,'در حال دانلود ')
# 	    ftp.retrbinary("RETR " + file ,open(folder_path + file, 'wb').write)

#             print(file,'Downloaded')
#     window['-comment1-'].update(file, 'دانلود کامل شد ')
#     ftp.close()    

#download the file
def download_All_file():
    files = ftp.nlst()
    folder_path = sg.PopupGetFolder('please open the folder') 
    #folder_path = folder_path + "\"
    window['-comment10-'].update('Please wait ...')
    for filename in files:
        #s = 'd:\VDR\{}'.format(filename)
        #local_filename = folder_path + filename
        #print(local_filename)
        window['-comment10-'].update('Please wait ...')
        local_filename = os.path.join(os.path.normpath(folder_path), filename)
        lf = open(local_filename, "wb")
        ftp.retrbinary("RETR " + filename, lf.write)
        print(filename, 'Downloaded')
        window['-comment10-'].update(f'{filename} Completed')
        lf.close()
    window['-comment10-'].update('Download Completed.')
#download each file
def download_each_file():
    window['-comment10-'].update('Please wait ...')
    each_file = values['-comment1-'][0]
    print(each_file,type(each_file))
    folder_path = sg.PopupGetFolder('please open the folder')
    #local_filename = folder_path + each_file
    local_filename = os.path.join(os.path.normpath(folder_path), each_file)
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR " + each_file, lf.write)
    print(each_file, 'Downloaded')
    window['-comment10-'].update(f'{each_file} Completed')
    lf.close()
    



listing= []

layout = [  [sg.Text('',size=(3,1)),sg.Text(text='VDR Transferer',font=('impact',35),text_color='orange'),sg.Text('')],
            [sg.Image('VDR.png'),sg.Image('arrow.png'),sg.Image('laptop.png')],
            [sg.Text('',size=(12,1),font='tahoma',text_color='black'),sg.Text('',size=(12,1))],
            [sg.Text(text='Ip Address', font='Elephant',text_color='black'),sg.InputText(default_text='192.168.1.10',size=(20,2),key='-Ip-')],
            [sg.Text(text='Username  ',font='Elephant',text_color='black'),sg.InputText(default_text='admin', size=(20,2),key='-user-'),sg.Button('Login',size=(8,3))],
            [sg.Text(text='Password  ',font='Elephant',text_color='black'),sg.InputText(default_text='pdw-hd1500',size=(20,2),key='-pass-')],
            [sg.Text(text='           ',font='impact',justification='center')],
            [sg.Listbox(values=listing ,size=(50,10),enable_events=True, key='-comment1-')],
            [sg.Button('Download All'),sg.Button('Download File')],
            [sg.StatusBar('Please Login ... ',size=(30,1), key='-comment10-',text_color='black',font=('Lilyupc',18))],
            [sg.Text(text='All right reserved for Ehsanpour.com and Hakamian',text_color='yellow',enable_events=True)]
            
            ]

# Create the Window
window = sg.Window('VDR Transferer', layout)
print(window)
win2_active=False  
index_counter= 0
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break
    if event == 'Login':
        URL = values ['-Ip-']
        
        username= values['-user-']
        
        password= values['-pass-']
        
        # change the "output" element to be the value of "input" element
        login_to(URL,user= username,passwd= password)
        #show file
        file_name()
    if event == 'Download All':  
        download_All_file() 

    if event == 'Download File':
        download_each_file()
    #windows 2 multiple page for STOP function
        

    # if not win2_active and event == 'STOP':
    #     win2_active = True
    #     layout2 = [[sg.Text('Are you wanna save the live on IGTV')],
    #                [sg.Button('Yes'),sg.Button('NO')]]
                    
    #     win2 = sg.Window('Save to IGTV', layout2)

    # if win2_active:
    #     ev2, vals2 = win2.read()
    #     if ev2 == 'Yes':
    #         adress = sg.popup_get_file('import your file')
    #         title = sg.popup_get_text('Write fucking down a title', 'Title')
    #         description = sg.popup_get_text('Write fucking down a description', 'Description')
    #         live.end_broadcast()
    #         live.add_post_live_to_igtv(description, title)
    #         win2.close()
            
            
        # else:
        #     #live.delete_post_live()
        #     #win2_active  = False
        #     #win2.close()
        #     live.end_broadcast()
        #     win2.close()
        # window['-comment1-'].update("Live Posted to Story!, Live finished, Good Bye")
        