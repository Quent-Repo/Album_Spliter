import os
import re

##
Regex_Time = r'^\d+:?\d+:\d+'
Regex_Name = r"[a-zA-Z\s'().-]*\s"  ## this misses the last word
def run():
    f = open("file.txt", "r")
    txt = ""
    txt = f.read()
    #x = input("name of the file: \n") ## could also set it to search the folder with the music file and store name
    #y = input("name of the .txt file with times and numbers: \n") ## could also set it to search the folder for a *.txt file
    x = re.findall(Regex_Time, txt, flags=re.M)
    y = re.findall(Regex_Name, txt, flags=re.M)
    z = "song.mp3"
    ##for loop to run shit
    for i in range(len(x)):
        print(x[i] + " " + x[i+1] + y[i])
        yz = y[i].replace("\n","")
        ##os.system("ffmepg -i " + z + " -acodec copy -ss " + x[i] + " -to " + x[i+1] + " " + y[i] + ".mp3")
        os.system("ffmpeg -i " + z + " -acodec copy -ss " + x[i] + " -to " + x[i+1] + " " + y[i].replace("\n","").replace(" ","",1).replace(" ","_")+ ".mp3")
run()    

