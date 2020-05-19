import nltk
import re
import os
import glob
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from fractions import Fraction
import math
nltk.download('stopwords')
def readtraintext(title):
    titlelist=[]
    porter = nltk.PorterStemmer()
    lancaster=nltk.LancasterStemmer()
    #dev폴더 지정
    os.chdir("C:/Users/ko/PycharmProjects/informaldata/dev/"+title)
    for file in glob.glob("*.txt"):
        with open(file, 'r') as f:
            s = f.read()
            #특수문자 제거
            onlyletter = re.sub('[^a-zA-Z]',' ', s)
            lemmatizer = WordNetLemmatizer()
            tokens = onlyletter.split()
            #불용어 제거
            ridstop = [w for w in tokens if not w in stopwords.words('english')]
            getstem=[lemmatizer.lemmatize(t) for t in ridstop]
            titlelist.append(getstem)
    return titlelist
#test_data 입력
def readtesttext(number):
    testtext=[]
    porter = nltk.PorterStemmer()
    lancaster=nltk.LancasterStemmer()
    #test 폴더 지정
    os.chdir("C:/Users/ko/PycharmProjects/informaldata/test/")
    for file in glob.glob(number+".txt"):
        with open(file, 'r') as f:
            s = f.read()
            #특수문자 제거
            onlyletter = re.sub('[^a-zA-Z]',' ', s)
            lemmatizer = WordNetLemmatizer()
            tokens = onlyletter.split()
            #불용어 제거
            ridstop = [w for w in tokens if not w in stopwords.words('english')]
            getstem=[lemmatizer.lemmatize(t) for t in ridstop]
            testtext=getstem
    return testtext
#성능 평가를 위한 Train_data 사용한 test
#def readtesttext(number):
#    testtext=[]
#    porter = nltk.PorterStemmer()
#    lancaster=nltk.LancasterStemmer()
#    #test 폴더 지정
#    os.chdir("C:/Users/ko/PycharmProjects/informaldata/testcase/")
#    for file in glob.glob(number+".txt"):
#        with open(file, 'r') as f:
#            s = f.read()
#            #특수문자 제거
#            onlyletter = re.sub('[^a-zA-Z]',' ', s)
#            lemmatizer = WordNetLemmatizer()
#            tokens = onlyletter.split()
#            #불용어 제거
#            ridstop = [w for w in tokens if not w in stopwords.words('english')]
#            getstem=[lemmatizer.lemmatize(t) for t in ridstop]
#            testtext=getstem
#    return testtext
#데이터 학습
title= ['interest','jobs','money_supply','trade']
devlist = []
for i in title:
    devlist.append(readtraintext(i))
interest=devlist[0]
jobs = devlist[1]
money_supply = devlist[2]
trade = devlist[3]
number=1
while(number!="0"):
 interp, jobsp, moneyp, tradep =0,0,0,0
 number=input("테스트문서 번호를 입력하세요, 종료하려면 0을 입력하세요")
 if number == "0" :
     print("종료합니다")
     break
 test = readtesttext(number)
 #TEST의 단어와 같은 개수의 리스트
 intercountlist=[]
 jobscountlist=[]
 moneycountlist=[]
 tradecountlist=[]
 #TRAIN SET의 단어수
 leninterest=0
 lenjobs=0
 lenmoney_supply=0
 lentrade=0
 #평탄화를 위한 중복을 제거한 TRAIN SET 의 단어수
 lenremoveinter=0
 lenremovejobs=0
 lenremovemoney=0
 lenremovetrade=0
 removeinter=[]
 removejobs=[]
 removemoney=[]
 removetrade=[]
 #중복 제거 과정
 for i in interest:
     for j in i:
      removeinter.append(j)
 remove_inter = list(set(removeinter))
 lenremoveinter=len(remove_inter)
 for i in jobs:
     for j in i:
      removejobs.append(j)
 remove_jobs = list(set(removejobs))
 lenremovejobs=len(remove_jobs)
 for i in money_supply:
     for j in i:
      removemoney.append(j)
 remove_money = list(set(removemoney))
 lenremovemoney=len(remove_money)
 for i in trade:
     for j in i:
      removetrade.append(j)
 remove_trade = list(set(removetrade))
 lenremovetrade=len(remove_trade)
 #print(lenremoveinter,lenremovejobs,lenremovemoney,lenremovetrade)
 #TRAIN SET의 총 단어수를 구하는 과정
 for a in interest:
  leninterest = leninterest + len(a)
 for a in jobs:
  lenjobs = lenjobs + len(a)
 for a in money_supply:
  lenmoney_supply = lenmoney_supply + len(a)
 for a in trade:
  lentrade = lentrade+ len(a)
 #print(leninterest,lenjobs,lenmoney_supply,lentrade)
 #TEST 파일에 단어를 주제별로 동일 한 개수를 찾고 리스트에 넣음
 for testlist in test:
     count = 0
     for trainlist in interest:
         for inlist in trainlist:
             if inlist == testlist:
                 count=count+1
     intercountlist.append(Fraction(count+1,(leninterest+lenremoveinter)))
 for testlist in test:
     count = 0
     for trainlist in jobs:
         for inlist in trainlist:
             if inlist == testlist:
                 count=count+1
     jobscountlist.append(Fraction(count+1,(lenjobs+lenremovejobs)))
 for testlist in test:
     count = 0
     for trainlist in money_supply:
         for inlist in trainlist:
             if inlist == testlist:
                 count=count+1
     moneycountlist.append(Fraction(count+1,(lenmoney_supply+lenremovemoney)))
 for testlist in test:
     count = 0
     for trainlist in trade:
         for inlist in trainlist:
             if inlist == testlist:
                 count=count+1
     tradecountlist.append(Fraction(count+1,(lentrade+lenremovetrade)))
 #print(intercountlist)
 #print(jobscountlist)
 #print(moneycountlist)
 #print(tradecountlist)
 pinter=0
 #언더플로를 방지하기위한 log함수
 loginter=[]
 logjobs=[]
 logmoney=[]
 logtrade=[]
 for i in range(0,len(intercountlist)-1):
    loginter.append(math.log(intercountlist[i]))
 for i in range(0,len(jobscountlist)-1):
    logjobs.append(math.log(jobscountlist[i]))
 for i in range(0,len(moneycountlist)-1):
    logmoney.append(math.log(moneycountlist[i]))
 for i in range(0,len(tradecountlist)-1):
    logtrade.append(math.log(tradecountlist[i]))
 for i in loginter:
     interp = interp+i
 for i in logjobs:
     jobsp = jobsp+i
 for i in logmoney:
     moneyp = moneyp+i
 for i in logtrade:
     tradep = tradep+i
 #argmax 계산 및 결과 출력
 if(max(interp,jobsp,moneyp,tradep)) == interp:
     print("해당 문서의 주제는 interest입니다")
 elif(max(interp,jobsp,moneyp,tradep)) == jobsp:
     print("해당 문서의 주제는 jobs입니다")
 elif(max(interp, jobsp, moneyp, tradep)) == moneyp:
     print("해당 문서의 주제는 money_supply입니다")
 elif(max(interp, jobsp, moneyp, tradep)) == tradep:
     print("해당 문서의 주제는 trade입니다")

