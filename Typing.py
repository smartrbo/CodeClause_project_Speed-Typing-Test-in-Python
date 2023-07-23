from time import *
import random as rd



def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!= usertest[i]:
                error =error+1
        except :
            error=error+1
    return error   

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_R=round(time_delay,2)
    speed =len(userinput)/ time_R
    return round(speed)    

while True:
    claers=input("Ready To test: Yes / No :")
    if claers == "Yes":
        Test=["A paragraph is about me i am certified ethical hacker and web developer ,i am enginer yhan you code clause to represnt you thank you "]
        test1=rd.choice(Test)
        print("____________Typing Speed________________")
        print(test1)
        print()
        print()
        print()
        time_1=time()
        testinput=input("ENter :")
        time_2=time()
        print(" Your speed:",speed_time(time_1,time_2,testinput),"w/sec")
        print(" Your Error:",mistake(test1,testinput) )

    elif claers =='No':
        print("thank You")
        break
    else:
        print("Enter valid Option")
