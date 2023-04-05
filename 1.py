#0405
'''
#문자열
str = "파이썬수업 씨수업 파이썬수업 파이썬수업"
str2 = "파이썬수업, 씨수업, 자바수업,이썬수업, 파이썬수업"

#format
#3+4=7
print(3,"+",4,"=",7)
f1 = "{} + {} = {}".format(3,4,3+4)
f2 = "{0} + {1} = {2} ,{2} ,{2} ,{2}".format(3,4,3+4)
f3 = "{0:d} + {1:f} = {2:f} ,{2} ,{2} ,{2}".format(3,4.0,3+4.0)
f4 = "{0:10d} + {1:10f} = {2:10.3f}".format(3,4.0,3+4.0)

print(f4)

#join
#"**".join(str)

#split
#print(str.split())
print(str2.split(","))
print(str2.split("업"))

#replace
print(str.replace("파이썬","자바",3))

#count
print(str.count("파이썬"))

#find , index
print("find : " , str.find("파이썬") , "index : " , str.index("씨"))
print(str.find("에이아이")) #없을때 return -1
print(str.index("에이아이")) #없을때 error 냄

#boolean
print(type(True),type(False))
a = "Hello"
print(bool("Hello"),bool("hi"),bool(3),bool(1.2),bool(-2))
print(bool(""),bool(0))
print(int(True),int(False),str(True))

#조건문
if 조건1 : 
    실행문1
else :  
    실헹문2  #거짓

    
if 조건1 : 
    실행문1  #참
elif 조건2 : 
    실행문2
elif 조건10 :
    실행문10
else :  
    실헹문2  #거짓


#오전/오후/저녁/점심
h = 9
if h <12 :
    #h가 12 보다 작을 때
    print("오전",h,"가 12보다 작다. ")
elif h<18 : #12<h<18
    print("오후 ",h,"는 12보다 크고 18보다 작아요. ")
else : #18<h
    print("저녁 ",h,"는 18보다 크다. ")


lunch = input("밥먹을래?")
if lunch == "yes" :
    print("밥을 먹고싶군요")
    cafeteria = input("학식?")
    if cafeteria == "yes" :
        print("8호관 1층으로")
    else : 
        print("학식을 싫어하시는군요")
        subway = input("subway?")
        if subway == "yes" :        
            print("8호관 1층으로 고고")
        else :
            print("subway 를 싫어하시는군요")
else : 
    print("밥 먹기 싫군요")

#for , while
#반복문
#in range

for i in 10,25,32,4352,565,624 :
    print ("i : ", i)

#range
for i in range(0,20,1) :
    print ("i : " , i)
for i in range(20) :
    print ("i : " , i)



#1부터 10까지 합을 구하시오
#2가지 방법으로 , range 도 쓰고 그냥 명시도 하고

sum = 0
for i in 1,2,3,4,5,6,7,8,9,10 :
    sum = sum + i
    print(i,"번째 loop입니다. sum은 " ,sum," 입니다")
    #print ("하하하")

print("range를 사용하였음")
sum = 0    
for i in range(1,11,1) :
    sum += i
    #sum = sum + i
    print(i,"번째 loop입니다. sum은 " ,sum," 입니다")
    
  

#sum , 0-10까지 숫자를 찍음
#sum 을 구할것임
sum = 0
n = 0
while n < 11 :
    #print("n : " ,n)
    sum += n
    print(n,"  번째 sum : " , sum )
    #print(n,end=" ")
    n = n+1

print("while밖에서 sum 의 값 : " , sum)

while 0 :
    print("실행이 되지않음")

print("while 0 다음줄입니다")


#while True :
 #   print("무한루프")

#while False :
 #   print("실행이 되지않음")
 
  
#break continue
#단어 입력을 무한 루프로 받는다
#그 글자를 3 번 써줌
#"exit" -> 루프를 끝내고 종료
#"apple" -> 3번 안쓰고 그냥 다시 단어를 입력받음

while True : 
    word = input("단어를 입력하세요 -> ")
    if word == "exit" :
         print("넌 exit 를 입력했다. break를 만난다.")
         break
         print("break 뒤의 문장")
    elif word == "apple" :
         print("넌 apple을 입력했다. continue를 만난다.")
         continue
         print("continue 뒤의 문장")
    else :
        for i in range(3) :
            print(word, end=' ')
        print("해당 단어 끝")

   
while True :
    if exit인 경우 :
        break
    elif apple인 경우 :
        continue
    else :
        for :
            3번 찍는다

 '''

#import random 

#print(random.randint(0,10000))

from random import randint
print(randint(0,10000))