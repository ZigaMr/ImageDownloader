from urllib.request import Request, urlopen
import DownloadImage
import re

req = Request("http://boards.4chan.org/g/catalog", headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

titles = []
tits = webpage.decode("utf8").split("\"")[:-1]

for i,t in enumerate(tits):
    if t == "sub":
        if tits[i+2] != "":
            titles.append(tits[i+2].replace("&#039;","\'").replace("\/","/"))
        else:
            titles.append("teaser: "+tits[i+6].replace("&#039;","\'").replace("\/","/").replace("&gt;",">"))



a =""
thread_numbers = []
img_count = []
b=0
for i in webpage.decode("utf8").split(":"):
    if '{"date"' in i:
        thread_numbers.append(a.split(",")[-1])
    if b == 1:
        img_count.append(int(i.split(",")[0]))
        b=0

    if '"i"' in i:
        b = 1

    a = i
for i,x in enumerate(thread_numbers):
    print("http://boards.4chan.org/g/thread/"+x.strip('"'),titles[i], "\n Image count: ", img_count[i])
print(len(thread_numbers),len(titles), len(img_count))

thread = input("Which one is it then: ")

req = Request(thread, headers={'User-Agent': 'Mozilla/5.0'})
images_website = urlopen(req).read()
tits = images_website.decode("utf8")

matches = re.findall(r'href=[\'"]?([^\'" >]+)', tits)

sez=[]
for i in matches:
    if "//is" in i and i not in sez:
        sez.append(i)

for x,i in enumerate(sez[2:]):
    a=DownloadImage.Download("http:"+i,str(x)+".jpg", "Img_for_"+str(thread).replace("http://boards.4chan.org/g/thread/",""))
    a.DL()