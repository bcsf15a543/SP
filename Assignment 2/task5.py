import urllib2    #liibraries
from textblob import TextBlob
from bs4 import BeautifulSoup
from sys import maxint
import os


gsmarena_url="https://www.gsmarena.com/"#the website to hit
my_html = urllib2.urlopen(gsmarena_url)
soup = BeautifulSoup(my_html,'html.parser')
brand_sidebar=soup.find("div",attrs={"class":"brandmenu-v2"}) #get brand menu
li_list=brand_sidebar.findAll("li") #extract list


print "BRAND LIST -> \n" #display list
for li in li_list:
    print li.text


flag=False
while(1):#get valid input->brand name
    input=raw_input("\n\nSELECT BRAND\n\n");
    input_link=None
    for li in li_list:
        if str(li.text) == str(input):
            flag=True
            input_link=li.find("a")["href"]
            input_brand=li.text
            break
    if(flag==False):
        print "Wrong input, enter again"
        continue
    else:
        break


input_link=gsmarena_url+input_link #generate the next url to hit

brand_page = urllib2.urlopen(input_link) #hit the brand's website selected to get its html
brand_html = BeautifulSoup(brand_page, 'html.parser')

total_pages=1 # total pages visited of brand page selected


mobile_sentiment_list =[] # lists to store overall polairty vaue,mobile's name and href link to the mobile (corresponding)
mobile_href_list = []
mobile_name_list = []


print "\n\nNOTE : This might take some time\n\n"

print "Now Proccessing page ",total_pages


backup_link=None

def calculate_sentiment(href): #calculates overall mobile's polarity + updation of lists
    user_comment_pno=2
    backup_link=href
    #print "in comments section\n"
    global mobile_sentiment_list

    sentiment_comment_list = [] #to hold all the comments of a particular mobile
    mobile_page = urllib2.urlopen(href)  # go to the mobile page
    mobile_html = BeautifulSoup(mobile_page, 'html.parser')

    full_name=b = href.replace(gsmarena_url, '').split('-')[0]
    print "\n\n\nCurrently evaluating comments of : ", full_name
   # full_name = mobile_html.find("div", attrs={"id": "user-comments"}).find("h2").find("a").text #get name of the mobile
    #name = full_name.split("-")[0]
   # print "\n\n\nCurrently evaluating comments of : ",name

    flag=1
    backup_link=None
    while(1):

            try:
                user_comment = mobile_html.find("div", attrs={"id": "user-comments"})
                #COMMENTS FOUND!
                if flag==1:
                    all_comments_link = user_comment.find("div", attrs={"class": "sub-footer"}).find("div", attrs={"class": "button-links"}).find("ul").find("li").find("a")  # extact all comment's list
                    all_comments_link = gsmarena_url + all_comments_link["href"]
                    backup_link=all_comments_link
                comment_page = urllib2.urlopen(all_comments_link)  # go to the mobile page having all the comments
                commment_html = BeautifulSoup(comment_page, 'html.parser')
                user_thread_list=commment_html.find("div", attrs={"id": "all-opinions"}).findAll("div", attrs={"class": "user-thread"})
                for user_thread in user_thread_list:
                    try:
                        p = user_thread.find("p",attrs={"class":"uopin"}) #get text of a comment
                        blob = TextBlob(str(p.text))
                        value = blob.sentiment.polarity#calculate polarity of sentence
                        print "\nComment = {comment}\nThis comment is on page = {pno}\nPolarity of the comment {polarity}\n".format(comment=str(p.text),pno=user_comment_pno-1,polarity=value)
                        sentiment_comment_list.append(value)#store comment
                    except:#Unknown exception while retrieving content of a comment , rare cases
                        continue # skip comment


            except:
                #NO COMMENTS FOUND
                minimum_int = -maxint - 1 # generate the most negative value
                mobile_sentiment_list.append(minimum_int) #update mobile_sentiment_list
                break

            break_url=backup_link
            break_url=break_url.split("-")
            last_number = break_url[2].split('.')[0]
            href = break_url[0] + "-" + break_url[1] + "-" + last_number + "p" + str(user_comment_pno) + ".php"

            try:
                new_page = urllib2.urlopen(href)

                try:
                    mobile_html = BeautifulSoup(new_page, 'html.parser')
                    user_comment = mobile_html.find("div", attrs={"id": "user-comments"})
                    user_comment_pno+=1
                    all_comments_link=href
                    backup_link=backup_link
                    flag=2
                    continue
                except:
                    # LOOPHOLE IN THE WEBSITE -> EMPTY PAGE handled
                    break

            except:
                # NO URL
                break

    total_sentiment = sum(sentiment_comment_list)  # get overall polarity value
    mobile_sentiment_list.append(total_sentiment)  # update mobile_sentiment_list

page_number=2 # to iterate through all valid pages

while(1):# to go through all the pages of the brand page (resoloves pagination)

        mobile_list=brand_html.find("div",attrs={"class":"makers"}) # to get mobile list per brand page
        li_mobile_list=mobile_list.findAll("li") # to get each mobile
        for li_mobile in li_mobile_list:
            href=li_mobile.find("a")["href"] # link of each mobile
            href=gsmarena_url+href # generate new url to hit
            mobile_name_list.append(li_mobile.find("a").find("strong").find("span").text) #update name list with mobile name
            mobile_href_list.append(href) #update list with new href generated
            calculate_sentiment(href)

        # to generate the next existing page
        base_url = input_link
        break_url = base_url.split('-')
        new_url = break_url[0] + "-" + break_url[1] + "-f-" + break_url[2].split('.')[0] + "-0-p" + str(page_number) + ".php"
        try:
            new_page = urllib2.urlopen(new_url)
            new_html = BeautifulSoup(new_page, "html.parser")
            try:
                ul_list = new_html.find("div", attrs={"id": "body"}).find("div", attrs={"class": "makers"}).find("ul").find("li").text
                #VALID PAGE FOUND
                total_pages+=1
                print "Now Proccessing page ",total_pages
                page_number += 1
                brand_page = urllib2.urlopen(new_url)
                brand_html = BeautifulSoup(brand_page, 'html.parser')
                continue
            except:
                #LOOPHOLE IN THE WEBSITE -> EMPTY PAGE handled
                break

        except:
            #NO URL
            break


#calculate max polarity
maximum_sentiment_value=max(mobile_sentiment_list)
index=mobile_sentiment_list.index(maximum_sentiment_value)
#corresponding page
maximum_sentiment_href=mobile_href_list[index]
#corresponding name
maximum_sentiment_mobile = mobile_name_list[index]


print "\n\nRECOMMENDATION (BEST REVIEWS) : \n" #display result
print "Mobile Name : {name}\nMobile Link : {link}\\n".format(name=maximum_sentiment_mobile,link=maximum_sentiment_href)











