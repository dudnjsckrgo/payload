import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
basedir =os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
from dataclasses import dataclass
import re
from miner.miner import MinerService
from os.path import getsize
import pandas as pd 
from collections import defaultdict
@dataclass
class Prepro():
    context3: str = os.path.join(basedir,'pdf-text-linestrip-0kbremove')
    context4: str ='E:/data/text-text'
    context5: str =os.path.join(basedir,'text-csv2')
class PreproController:
    def __init__(self):
        self.prepro = Prepro()
        self.service = PreproService()
    def zremove_loopfun(self):
        prepro = self.prepro
        mylist=MinerService.searchfile(prepro)
        try:
            for item in mylist:
                file=os.path.join(prepro.context3,item)
                print(file)
                gfile=getsize(file)
                print(gfile)
                if gfile <=1000:
                    print(file )
                    os.remove(file)
        except:
            pass
    def linestrip_loopfun(self):
        prepro = self.prepro
        mylist=MinerService.searchfile(prepro)
        
        for item in mylist:
            title = item.rstrip('.txt')
            path = prepro.context3
            PreproService.lineStrip(prepro,title)
    def part5_loopfun(self):
        prepro = self.prepro
        mylist = MinerService.searchfile(prepro)
        for item in mylist:
            try:
                print(item)
                title = item.rstrip('.txt')
                path =os.path.join(prepro.context3,item)
                mydict=PreproService.part5process(path)
                df=PreproService.dictToDataFrame(mydict)
                newpath= os.path.join(prepro.context5, title+'.csv')
                PreproService.dfToCsv(df,newpath)
                
            except:
                pass
            
class PreproService:
    def __init__(self):
        self.prepro = Prepro()
    @staticmethod
    def lineStrip(payload,title):
        path = os.path.join( payload.context3,  title+'.txt' )
        f =open(path, mode ='rt', encoding='utf-8') 
        lines=f.readlines()
        f.close()
        path1= os.path.join(payload.context4,title+'.txt' )
        fw  =open(path1,mode='wt',encoding='utf-8') 
        for line in lines:
            obj=re.compile(r'\w')
            li=obj.search(line)
                    
            if not li:
                        # print(li)
                continue
            text = line.lstrip()
                    
            fw.write(text)
        fw.close()
    @staticmethod
    def noNeedlineStrip(payload,title):
        path = os.path.join( payload.context3,  title+'.txt' )
        f =open(path, mode ='rt', encoding='utf-8') 
        lines=f.readlines()
        f.close()
        path1= os.path.join(payload.context4,title+'.txt' )
        fw  =open(path1,mode='wt',encoding='utf-8') 
        for line in lines:
            obj=re.compile(r'\w')
            li=obj.search(line)
                    
            if not li:
                        # print(li)
                continue
            text = line.lstrip()
                    
            fw.write(text)
        fw.close()
    @staticmethod
    def part5process(path):
        f = open(path,mode='rt',encoding='utf-8')
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
                
                text= line.rstrip('\n').lstrip(imsi_matchobj.group())

            if myindex == index:
                if matchobj3:
                    print(matchobj3.group())
                    text+= line.rstrip('\n')
                    myindex = index +1
                elif matchobj2:
                
                    
                    mydict[text]=[]
                    print(matchobj2.group())
                    imsi_regex2 = re.compile(r'^\([A-D]\)')
                    imsi_matchobj2= imsi_regex2.search(matchobj2.group())
                    mydict[text].append( line.rstrip('\n').lstrip(imsi_matchobj2.group()))
                    answerIndex = index +1

            if answerIndex==index:
                if matchobj2:
                    print(matchobj2.group())
                    answerIndex = index +1
                    imsi_regex2 = re.compile(r'^\([A-D]\)')
                    imsi_matchobj2= imsi_regex2.search(matchobj2.group())
                    mydict[text].append( line.rstrip('\n').lstrip(imsi_matchobj2.group()))
                    
                else:
                    answerIndex=-1
                    
                
                    
                # matchobjlist2.append((index,matchobj2.group()))
        # print(matchobjlist)
        # print(matchobjlist2)
        print(mydict)
        f.close()
        return mydict
    @staticmethod
    def dictToDataFrame(mydict):
        df =pd.DataFrame.from_dict(mydict)
        df=df.T
        
       
        # print("+++++",df.isnull().values.any())
        # rint(df.index)
        # print(df)
        # df.to_csv(path,index=False)
        return df
    @staticmethod
    def dfToCsv(df,path):
        
        df.to_csv(path,encoding='utf-8-sig', errors= 'strict', index_label='problem')
        pass
if __name__=='__main__':
    api = PreproController()
    # api.zremove_loopfun()
    api.part5_loopfun()