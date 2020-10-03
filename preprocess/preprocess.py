import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from dataclasses import dataclass
import re
from miner.miner import MinerService
from os.path import getsize
@dataclass
class Prepro():
    context3: str = 'E:/data/pdf-text'
    context4: str ='E:/data/text-text'
class PreproController:
    def __init__(self):
        self.prepro = Prepro()
        self.service = PreproService()
    def zremove_loopfun(self):
        prepro = self.prepro
        mylist=MinerService.search(prepro)
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
        mylist=MinerService.search(prepro)
        
        for item in mylist:
            title = item.rstrip('.txt')
            path = prepro.context3
            PreproService.lineStrip(prepro,title)
    def noNeedlinestrip_loopfun(self):
        prepro = self.prepro
        mylist=MinerService.search(prepro)
        
        for item in mylist:
            title = item.rstrip('.txt')
            path = prepro.context3
            PreproService.lineStrip(prepro,title)   
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
        
if __name__=='__main__':
    api = PreproController()
    # api.zremove_loopfun()
    api.linestrip_loopfun()
    # PreproService.lineStrip('E:/data/pdf-text/','(eBook)American_Accent_Training')