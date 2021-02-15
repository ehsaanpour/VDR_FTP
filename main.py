import requests
from ftplib import FTP
import PySimpleGUI as sg
class VDR:
    url = '192.168.57.38'
    

    def __init__(self ,username,password):
        self.username=username
        self.password= password
        
    def download_file(self): 
        ftp = FTP(VDR.url)
        ftp.login(self.username,self.password)
        print('we enter')
        filenames = ftp.nlst()

        for filename in filenames:

            with open( filename, 'wb' ) as file :

                ftp.retrbinary('RETR %s' % filename)

            file.close()
        #ftp.dir(self.files.append)
            
        #ftp.cwd(url)
        #ftp.retrbinary('iran.txt', open(files[0], 'wb').write)


vdr = VDR(username='tech',password='Prs6353')

vdr.download_file()
print(vdr.download_file())
#User interface app

sg.theme('LightBrown7')   # Add a touch of color
list1=["apple", "banana", "cherry", "apple", "cherry"]
print(list1[1])

# All the stuff inside your window.
layout = [  [sg.Text(text='           ')],
            [sg.Text('',size=(15,1)),sg.Text(text='VDR',font=('impact',22),text_color='orange'),sg.Text('')],
            [sg.Text('',size=(12,1)),sg.Text(text='انتقال فایل های ایکس دی کم',font='tahoma',text_color='green')],
            [sg.Text(text='           ')],
            [sg.Text('',size=(12,1)),
            sg.Text(text='Ip Adress',font='tahoma',text_color='green'),
            sg.Text('',size=(12,1)),
            sg.Text(text='Password',font='tahoma',text_color='green')],
            [sg.InputText(size=(20,2)),sg.InputText(size=(20,2),password_char='*')],
            
            [sg.Text(text='           ',font='impact',justification='center')],
            [sg.Text(text='           ')],
            [sg.Listbox(values=list1,size=(60,20))],
            [sg.Text('',size=(10,1)),sg.Button('ورود'), sg.Text('   '), sg.Button('خروج')],
            [sg.StatusBar('Status: ',size=(50,1), key='-comment1-')],
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
    if event == 'Go to Stream':
        username= values[0]
        password= values[1]
        # change the "output" element to be the value of "input" element
        live=InstaStream( username ,password )
        live.start()
        
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
        
