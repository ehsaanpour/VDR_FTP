import os
from ftplib import FTP
import PySimpleGUI as sg


#login to FTP
def login_to(URL , user , passwd):
    global ftp
    ftp = FTP()
    ftp.connect(URL)
    ftp.login (user,passwd)


#identify the files name.
def file_name():
    global listing
    ftp.retrlines("LIST")
    ftp.cwd('')
    ftp.cwd('') # or ftp.cwd("folderOne/subFolder")
    listing = []
    ftp.retrlines("LIST", listing.append)
    window['-comment1-'].update(listing)
    return listing
    

# download the file
def download_All_file():
    local_filename = os.path.join(r"d:\myfolder", filename)
    lf = open(local_filename, "wb")
    ftp.retrbinary("RETR " + filename, lf.write, 8*1024)
    lf.close()

#download each file
def download_each_file():
    local_filename = os.path.join(r"d:\myfolder\project", filename)
    #for file in listing :



listing= []

layout = [  [sg.Text(text='           ')],
            [sg.Text('',size=(15,1)),sg.Text(text='VDR',font=('impact',22),text_color='orange'),sg.Text('')],
            [sg.Text('',size=(12,1)),sg.Text(text='انتقال فایل های ایکس دی کم',font='tahoma',text_color='green')],
            [sg.Text(text='           ')],
            [sg.Text('',size=(12,1),font='tahoma',text_color='green'),sg.Text('',size=(12,1))],
            [sg.Text(text='Ip Adress'),sg.InputText(size=(20,2))],
            [sg.Text(text='Password',font='tahoma',text_color='green'),sg.InputText(size=(20,2))],
            [sg.Text(text='Password',font='tahoma',text_color='green'),sg.InputText(size=(20,2),password_char='*')],
            
            [sg.Text(text='           ',font='impact',justification='center')],
            [sg.Text(text='           ')],
            [sg.Listbox(values=listing ,size=(60,20),key='-comment1-')],
            [sg.Text('',size=(10,1)),sg.Button('ورود'), sg.Text('   '), sg.Button('خروج')],
            [sg.StatusBar('Status: ',size=(50,1), key='-comment10-')],
            [sg.Text(text='All right reserved for Ehsanpour.com',text_color='yellow',enable_events=True)]
            
            ]

# Create the Window
window = sg.Window('VDR', layout)
print(window)
win2_active=False  
index_counter= 0
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'close': # if user closes window or clicks cancel
        break
    if event == 'ورود':
        print(values[0],values[1],values[2])
        URL = values [0]
        username= values[1]
        password= values[2]
        # change the "output" element to be the value of "input" element
        login_to(URL,user= username,passwd= password)
        #show file
        file_name()
        
    #windows 2 multiple page for STOP function
        

    if not win2_active and event == 'STOP':
        win2_active = True
        layout2 = [[sg.Text('Are you wanna save the live on IGTV')],
                   [sg.Button('Yes'),sg.Button('NO')]]
                    
        win2 = sg.Window('Save to IGTV', layout2)

    if win2_active:
        ev2, vals2 = win2.read()
        if ev2 == 'Yes':
            adress = sg.popup_get_file('import your file')
            title = sg.popup_get_text('Write fucking down a title', 'Title')
            description = sg.popup_get_text('Write fucking down a description', 'Description')
            live.end_broadcast()
            live.add_post_live_to_igtv(description, title)
            win2.close()
            
            
        else:
            #live.delete_post_live()
            #win2_active  = False
            #win2.close()
            live.end_broadcast()
            win2.close()
        window['-comment1-'].update("Live Posted to Story!, Live finished, Good Bye")
        