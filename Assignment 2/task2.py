import  urllib2
from bs4 import BeautifulSoup
import sys;
reload(sys);
sys.setdefaultencoding("utf8")


article_list=[]
link_list=[]

input=raw_input("Enter a list of words and I will display links of articles that are made up of those words\n")
input=input.split(" ")
url_link = "https://propakistani.pk/category/sports/"


def generate_list(url_link,input):
    total_pages = 5
    current_page = 1
    while(1):

        my_html = urllib2.urlopen(url_link)
        soup = BeautifulSoup(my_html, 'html.parser',from_encoding="utf-8")
        article_tags=soup.findAll("article")
        for article_tag in article_tags:
            link_list.append(article_tag.find("a")["href"])
            article_list.append(article_tag.find("a").text)
        current_page+=1
        if(current_page<=total_pages):
            url_link="https://propakistani.pk/category/sports/page/"+str(current_page)+"/"
            continue
        else:
            break

    cntr=0
    status=0
    for article in article_list:
        flag=False
        words=article.split(" ")
        comparing_words=[] #case_insensitive search
        for word in words:
            comparing_words.append(word.upper())
        for input_word in input:
            if input_word.upper() in comparing_words:
                flag=True
                break
        if flag==True:
            print "Article Title : {title}\nArticle link : {link} \n".format(link=link_list[cntr],title=article_list[cntr])
            status+=1
        cntr+=1

    if(status==0):
        print "Sorry , No results found"

generate_list(url_link,input)

