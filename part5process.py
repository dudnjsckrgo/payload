import re
import pandas as pd 
from collections import defaultdict
f = open('[해커스토익]_2014년_9월_김동영선생님_예상문제.txt',mode='rt',encoding='utf-8')
lines=f.readlines()
matchobjlist=[]
matchobjlist2=[]
myindex =-1
answerIndex=-1
text= ''
answertext=''
mydict = defaultdict()
mydictIndex = -1
for index, line in enumerate(lines):
    # print(line)
    regex=re.compile(r'^\d{2,3}\. [a-zA-Z\d\-\,\.\'\"\?\!]{1,200}[^ㄱ-힣]{2,100}') # 140. City regulations regarding disposal of recyclable materials
    regex2=  re.compile(r'^\([A-D]\) [a-zA-Z]{1,30}')#(D) impractically
    regex3= re.compile(r'^[a-zA-Z\d\-\,\.\'\"\?\!]{1,200}[^ㄱ-힣]{2,100}')
    matchobj=regex.search(line)
    matchobj2= regex2.search(line)
    matchobj3 = regex3.search(line)
    if matchobj:
        print('-'*30)
        print(matchobj.group())
        myindex = index+1
        imsi_regex = re.compile(r'^\d{2,3}\.')
        imsi_matchobj= imsi_regex.search(matchobj.group())
        
        text= matchobj.group().rstrip('\n').lstrip(imsi_matchobj.group())

    if myindex == index:
        if matchobj3:
            print(matchobj3.group())
            text+= matchobj3.group().rstrip('\n')
            myindex = index +1
        elif matchobj2:
           
            
            mydict[text]=[]
            print(matchobj2.group())
            imsi_regex2 = re.compile(r'^\([A-D]\)')
            imsi_matchobj2= imsi_regex2.search(matchobj2.group())
            mydict[text].append( matchobj2.group().rstrip('\n').lstrip(imsi_matchobj2.group()))
            answerIndex = index +1

    if answerIndex==index:
        if matchobj2:
            print(matchobj2.group())
            answerIndex = index +1
            imsi_regex2 = re.compile(r'^\([A-D]\)')
            imsi_matchobj2= imsi_regex2.search(matchobj2.group())
            mydict[text].append( matchobj2.group().rstrip('\n').lstrip(imsi_matchobj2.group()))
            
        else:
            answerIndex=-1
            break
        
            
        # matchobjlist2.append((index,matchobj2.group()))
# print(matchobjlist)
# print(matchobjlist2)
print(mydict)
f.close()
        
             