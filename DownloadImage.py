from urllib.request import urlretrieve
import os

class Download:
    def __init__(self, URL, name_file, name):
        self.URL = URL
        self.name = name
        self.name_file = name_file

    def DL(self):
        dir = os.getcwd()
        newpath=dir+"/"+self.name
        if not os.path.exists(newpath):
            os.mkdir(newpath)
        os.chdir(newpath)
        urlretrieve(self.URL,self.name_file)
        os.chdir("..")

a=Download("http://is.4chan.org/out/1363920914821.jpg", "Bear Hands.jpg", "Bear1")
a.DL()
