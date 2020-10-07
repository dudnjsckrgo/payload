import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from dataclasses import dataclass
from tika import parser

@dataclass
class Miner:
    context2: str = "crawler/data2/"
    context3: str = 'E:/data/'
    file: str =''
    context4: str = 'E:/data/pdf-txt/'
class MinerController:
    def __init__(self):
        self.miner = Miner()
        self.service = MinerService()
    def loop(self,mytype):
        miner=self.miner
        miner.context3= os.path.join(miner.context3,mytype)
        print(miner.context3)
        
        mylist=MinerService.search(miner)
        for item in mylist:
            full_path= os.path.join(miner.context3, item)
            print(full_path)
            text=MinerService.pdf_to_text(full_path)
            title = item.rstrip('.'+mytype)
            MinerService.saveFile(miner,text,'txt',title)
class MinerService:
    def __init__(self):
        self.miner = Miner()

    @staticmethod
    def pdf_to_text(path):
        raw=parser.from_file(path)
        return raw['content']
    @staticmethod
    def search(miner):
        dirname = miner.context3
        filenames = os.listdir(dirname)
        mylist=[]
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            mylist.append(full_filename)
            print (full_filename)
        return mylist
    @staticmethod
    def searchfile(miner):
        dirname = miner.context3
        filenames = os.listdir(dirname)
        mylist=[]
        for filename in filenames:
            full_filename = filename
            mylist.append(full_filename)
            print (full_filename)
        return mylist
    @staticmethod
    def saveFile(miner,text,mytype,title):
        
        filename =os.path.join(miner.context4, title + '.'+mytype)
        # print(mysrc)
        # print(filename)

        with open(filename, mode='wt',encoding='utf-8') as fw:
            try:
                fw.write(text) # 바이트 형태로 저장
                print(f'{filename} 저장완료!!!!!!!!!!!!')
            except:
                pass
    
if __name__ =="__main__":
    miner= MinerController()
    miner.loop('pdf')
