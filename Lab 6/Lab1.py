
# coding: utf-8

# In[1]:


def divisible_func():
    list=[]
    for num in range(2000,3201):
        if (((num%7)==0) and (num%5!=0)):
            list.append(num)
    return list
list=divisible_func()
print "The numbers divisible by 7 but not by 5 are between (2000-3200) : \n"
print list


# In[ ]:


def generate_list_tuple(args):
    num_list=args.split(',')
    mylist=[]
    for num in num_list:
        mylist.append(num)
    print mylist 
print "Enter comma seperated values"
input=raw_input("prompt")
generate_list_tuple(input)


# In[17]:


def upper_case(args):
    new_arg=args.upper()
    print "The sentence you entered : ",args
    print "Upper case sentence : ", new_arg
print "Enter a sentence"
input=raw_input("prompt")
upper_case(input)


# In[25]:


def count_letter_digit(args):
    l_count=0
    d_count=0
    for ch in args:
        if ch.isdigit():
            d_count+=1
        if ch.isalpha():
            l_count+=1
    print "You entered : ", args
    print "Letters ",l_count," | ","Digits ",d_count
print "Enter a sentence"
input=raw_input("prompt")
count_letter_digit(input)


# In[34]:


def generate_dictionary(args):
    dict={}
    for num in range(1,args+1):
        dict[num]=num*num
    print "You entered ",args
    print "Dictionary looks like ", dict
generate_dictionary(8)


# In[1]:


def generate_sorted(args):
    my_list=input.split(',')
    my_list.sort()
    print "\nUnsorted List : ",args
    print "Sorted List : ",my_list
print "Enter a comma sentence"
input=raw_input("prompt")
generate_sorted(input)


# In[13]:


def generate_white_sorted(args):
    new_list=[]
    my_list=args.split(' ')
    my_list.sort()
    new_list.append(my_list[0])
    for num in my_list:
        if new_list[-1]!=num:
            new_list.append(num)
    print "\n\nSorted List : "
    for num in new_list:
        print num
print "Enter a space sentence"
input=raw_input("prompt")
generate_white_sorted(input)

