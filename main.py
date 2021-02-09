import requests
from ftplib import FTP

class VDR:
    def __init__(self ,username,password):
        self.download_file(username,password)
        
    def download_file(self,username,password): 
        self.username=username
        self.password= password
        files = []
        self.files=files
        ftp = FTP('192.168.57.38')
        ftp.login(self.username,self.password)
        ftp.dir(self.files.append)
        print(self.files)


VDR(username='tech',password='Prs6353')