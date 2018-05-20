import urllib2 # libraries
import requests
from bs4 import BeautifulSoup
import os
import  pydub
import  datetime
from pydub import AudioSegment

pydub.AudioSegment.converter = r"C:\ffmpeg\bin\ffmpeg.exe"



Logfile = open("logfile.txt", "w")#to record everything
Logfile.truncate()

def merge_files(directory_path): #merges the files together to make a new file

    combined = AudioSegment.empty()
    folder_name = directory_path.split("\\")[-1]
    Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + "\nMerging files of  : "+ folder_name+"\n")
    files_list = os.listdir(directory_path)
    for mp3_file in files_list:
        audio_file = AudioSegment.from_mp3(folder_name + '\\' + mp3_file)
        Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + " Merged File Name :"+ mp3_file+"\n")
        combined += audio_file
    try:
        combined.export("./" + folder_name + "/SecondHalf.mp3", format='mp3', bitrate="192k")
        combined.close()
        Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + "Successfully Merged all the files \n\n\n")
    except Exception:
        combined.close()
        Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + "Successfully Merged all the files \n\n\n")
        return


def download_now(filename,href): #downloads the audio file found at href
    mp3_request = requests.get(href, stream=True)
    with open(filename, 'wb') as file:
        for chunk in mp3_request.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                file.flush()

def download_mp3(list,qari_name,path):#to download the audio files in a paritcular folder
   for href in list[-26:]:#get the last 26 links
      file_name=href.split('/')[-1]
      Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + " File : " + file_name + "\n")
      filename = path+file_name
      download_now(filename,href)


def generate_qari_list(href):#to store the links of all the mp3 files
    global qari_list
    qari_list.append(href)



def qari_files(href,path,qari_name):#to retrieve all the files from the website and call approriate functions to store them
   try:
        global qari_list
        my_html_quranic = urllib2.urlopen(href)
        soup_quranic = BeautifulSoup(my_html_quranic, 'html.parser')
        a_tags_quranic=soup_quranic.findAll("a")
        for a_tag_quranic in a_tags_quranic[1:]:
              newhref=href+a_tag_quranic["href"]
              file_name=a_tag_quranic.text
              generate_qari_list(newhref)
        if a_tag_quranic["href"] != "../" :
            download_mp3(qari_list, qari_name, path)  # mp3file link
            qari_name=qari_name.split("/")[0]
            absoulte_path = 'C:\Users\HP\PycharmProjects\SPAssignment\\' + qari_name
            try:
                merge_files(absoulte_path)
                qari_list=[]
            except :
                qari_list=[]
   except:
       return

print "Processing,please wait..."

count =1
qari_list=[]
html_page="https://download.quranicaudio.com/quran/"#Main page
my_html = urllib2.urlopen(html_page)
soup = BeautifulSoup(my_html,'html.parser')

a_tags=soup.findAll("a") #contains all the links->qari names

qari_count=len(a_tags)-1 #ignore the first one
Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S")+" Total Qaris "+ str(qari_count)+"\n\n")

processing_cnt=1

for a_tag in a_tags[1:]:
        qari_name=a_tag.text
        path="./"+qari_name
        if not os.path.isdir(path):
            os.makedirs(path)
            new_href=html_page+qari_name
            Logfile.writelines("\n\n"+datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + " Start Processing of  " + str(processing_cnt)+" out of "+str(qari_count)+"\n\n")
            Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + " Qari Name : " +qari_name.split("/")[0]+"\n")
            qari_files(new_href,path,qari_name)
        else:
            new_href = html_page + qari_name
            Logfile.writelines("\n\n"+datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + " Start Processing of  " + str(processing_cnt)+" out of "+str(qari_count)+"\n\n")
            Logfile.writelines(datetime.datetime.today().strftime("%Y-%m-%d %H-%M-%S") + " Qari Name : " +qari_name.split("/")[0]+"\n")
            qari_files(new_href,path,qari_name)
        processing_cnt+=1

