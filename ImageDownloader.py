from urllib.request import Request, urlopen

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
for i in webpage.decode("utf8").split(":"):
    if '{"date"' in i:
        thread_numbers.append(a.split(",")[-1])
    a = i
for i,x in enumerate(thread_numbers):
    print("http://boards.4chan.org/g/thread/"+x.strip('"'),titles[i])
print(len(thread_numbers),len(titles))
