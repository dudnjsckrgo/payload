import sys
import os
import pickle
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import shutil
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import re
from urllib.request import urlopen
from selenium import webdriver
from urllib.request import urlopen
from dataclasses import dataclass ,asdict ,field
    
@dataclass
class ChromeDriver:
    # spyder :object = webdriver.Chrome('C:/chromedriver/chromedriver.exe')
    first_url : str = 'http://m.hackers.co.kr/?c=s_toeic/toeic_board/B_TOEIC_data&source=http://www.hackers.co.kr'
    sub_url: str = '&p='
    soup : object = None
    parser : str = 'html.parser'
    page : int = 131
    filename ="urls"
    url :str ="http://m.hackers.co.kr/?c=s_toeic/toeic_board/B_TOEIC_data&p=3&uid=771347"
    context: str ="crawler/data/"
    context2: str = "crawler/data2/"
    context3: str = "E:/data/"
    root_url: str ='http://m.hackers.co.kr'
    mydict : object =None
    new_folder_name : str = 'data3'
    count :int =902
    countPdf: int =0
    countZip: int = 0
class ChromeListener:
    def __init__(self):
        self.driver = ChromeDriver()
        self.bs4Sel = Bs4Sel()
        
    def searching_data(self,i=0):
        driver= self.driver
        if i==0 :
            driver= Bs4Sel.bs4_get_url(driver)
        if i !=0 :
            driver= Bs4Sel.bs4_get_url(driver,i)
        
        second_target = {'tag': 'article'}
        confirm_target = {'tag': 'img','class':'imgpos'}
        imgposs = Bs4Sel.bs4_get_docs(driver,confirm_target)
        urls=[]
        for imgpos in imgposs:
            text=Bs4Sel.bs4_find_parents(imgpos,'article','onclick')
            if text == None:
                return 
            text=text.lstrip("goHref('")
            text=text.rstrip("');")
            text= driver.root_url + text
            urls.append(text)
        print(urls)
        filename = driver.filename + str(i).zfill(2)
        context=driver.context
        Bs4Sel.savePickle(urls,context, filename)
    
    def searching_data_2(self,**kargs):
        for key, value in kargs.items():
            if key =='i':
                i = value
            if key== 'url':
                url = value
                
        driver= self.driver
        if len(kargs)==2:
            driver.first_url= url
        driver=Bs4Sel.bs4_get_url(driver)
        target= {'tag':'article',"class":"text_area"}
        tag=Bs4Sel.bs4_get_doc(driver,target)
        # print("tag.name:",tag.name)
        tags= tag.select('div:nth-last-child(1)')
        # print("selet:" ,tags)
        # print(type(tags))
        urls = []
        
        driver.mydict ={'pdf':{},'zip':{}}
        mydict = driver.mydict
        for tag in tags:
            try:
                if tag.a == None:
                    continue
                if tag.a.attrs['href'] =="https://www.hackers.co.kr/?c=s_toeic/toeic_board/B_TOEIC_QA":
                    continue
                
                tags=tag.find_all('a')
                # print("tags: ",tags)
        
                for tag in tags:
                    text=tag.text.strip()
                    
                    sub_url= tag.attrs['href'] 
                    # print("#"*30+text)
                    # print("+"*50,tag)
                    # print("+"*50,tag.name)
                
                    full_url=driver.root_url + sub_url
                    urls.append((text,full_url))
                    
                    if text.find('.zip') != -1:
                        title =text.rstrip(".zip")
                        mydict['zip'][title]=full_url
                        mytype ='zip'
                        Bs4Sel.saveFile(driver,full_url,mytype,title)
                        driver.countZip += 1
                        print(f"zip파일이 {driver.countZip}개 생겼습니다")
                    if text.find('.pdf') != -1: 
                        title =text.rstrip(".pdf")
                        mydict['pdf'][title]=full_url
                        mytype= 'pdf'
                        Bs4Sel.saveFile(driver,full_url,mytype,title)
                        driver.countPdf += 1
                        print(f"pdf파일이 {driver.countPdf}개 생겼습니다")
                    # print(full_url)
            except Exception as err:
                print(err)
            
 
                
        filename = driver.filename + str(driver.count).zfill(2)
        driver.count += 1
        context=driver.context2
        Bs4Sel.savePickle(mydict,context, filename)
        
    def loopfun(self):
        driver = self.driver
        for i in range(51,driver.page):
            self.searching_data(i)
            
    def loopfun2(self):
        driver = self.driver
        for i in range(52,driver.page):
            filename= driver.filename + str(i).zfill(2)
            context= driver.context
            try:
                mylist=Bs4Sel.loadPickle(context,filename)
            except:
                continue
            # print(mylist)
            set(mylist)
            print(set(mylist))
            for j, url in enumerate(set(mylist)):
                self.searching_data_2(i=j,url=url)
                # break #차후에 제거
        
class Bs4Sel:
    def __init(self):
        self.driver = ChromeDriver()

    @staticmethod
    def bs4_get_url(driver, *args):
        if len(args)==0:
            url = driver.first_url
        if len(args)==1:
            url = driver.first_url+ driver.sub_url+ str(args[0])
        response = urlopen(url)
        driver.soup = BeautifulSoup(response, driver.parser)
        # print(driver.soup)
        return driver
    @staticmethod
    def bs4_get_docs(driver,kargs):
        for key, value in kargs.items():
            if key =='tag':
                tag= value
            if key != 'tag':
                attrs =key
                # print(attrs)
                value =value
                # print(value)
        if len(kargs) == 2:
            targets = driver.soup.find_all(tag, attrs={attrs: value})
            # print("2: ",type(targets))
        if len(kargs) == 1:
            targets = driver.soup.find_all(tag)
            # print("1: ",type(targets))
        # for target in targets:
            # print("-"*30)
            # print(target)
            # print("-"*30)
        return targets
    @staticmethod
    def bs4_get_doc(driver,kargs):
        for key, value in kargs.items():
            if key =='tag':
                tag= value
            if key != 'tag':
                attrs =key
                # print(attrs)
                value =value
                # print(value)
        if len(kargs) == 2:
            target = driver.soup.find(tag, attrs={attrs: value})
            # print("2: ",type(target))
        if len(kargs) == 1:
            target = driver.soup.find(tag)
            # print("1: ",type(target))
      
        return target
    
    @staticmethod
    def bs4_find_parents(target,myparent,attrs):
        try:
            while target.name != myparent:
                target=target.parent
                # print(target.name)
            text=target.attrs[attrs]
            print(text)
            print(type(text))
            return text
        except:
            return
            
    
    @staticmethod
    def savePickle(mylist,context,filename):
        path = context +filename + '.pickle'
        print(type(mylist))
       
        with open(file=path,mode="wb") as fw:
            pickle.dump(mylist,fw)
            print(f'{filename}  피클 저장완료!!!!')
        # if type(mylist)=='dict': 
        #     with open(file=path,mode="wb") as fw:
        #         pickle.dump(mylist,fw, protocol=pickle.HIGHEST_PROTOCOL)
        #         print(f'{filename} 딕셔너리 피클 저장완료!!!!')
    @staticmethod
    def loadPickle(context,filename):
        path = context +filename+'.pickle'
        # print(path)
        with open(file=path,mode='rb') as fw:
            mylist=pickle.load(fw)
            print(f"{path} loading 완료!!!!!")
        return mylist
    @staticmethod
    def saveFile(driver,url,mytype,title):
        file = urlopen(url)
        filename = driver.context3 + mytype + '/' + title + '.'+mytype
        # print(mysrc)
        # print(filename)

        with open(filename, mode='wb') as fw:
            fw.write(file.read()) # 바이트 형태로 저장
            print(f'{filename} 저장완료!!!!!!!!!!!!')

           
    # @staticmethod
    # def create_folder_from_dict(driver)->object:
    #     # shutil : shell utility : 고수준 파일 연산. 표준 라이브러리
    #     dict = driver.dict
    #     folderName= driver.new_folder_name
    #     folder = './'+folderName +'/' # 유닉스 기반은 '/'이 구분자
    #     try:
    #         if not os.path.exists(folder):
    #             os.mkdir(folder)

    #         for dir in dict.values():
    #             path = folder + dir

    #             if os.path.exists(path):
    #                 # rmtree : remove tree
    #                 shutil.rmtree(path)

    #             os.mkdir(path)

    #     except FileExistsError as err:
    #         print(err)
    #     return folder
    
if __name__ == "__main__":
    api = ChromeListener()
    # api.searching_data()
    api.loopfun2()

