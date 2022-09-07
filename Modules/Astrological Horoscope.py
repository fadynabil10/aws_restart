#   طريقة التأريخ لحساب تاريخ ميلادك:
#2002.7.1 (Format)
import string
birthday = input("الرجاء إدخال سنة الميلاد والشهر واليوم (التنسيق: xx.xx.xx):") 
print("\n")
bir = birthday.split(".")
#print(bir)

 
year = int(bir[0])
month = int(bir[1])
day = int(bir[2])
#print(year,month,day)
 
def CalXingzuo():
    if month==1 :
        if day<=19:
                         xing = "الجدي"
        else:
                         xing = "برج الدلو"
    if month==2:
        if day<=18:
                         xing = "برج الدلو"
        else:
                         xing = "الحوت"
    if month==3:
        if day<=20:
                         xing = "الحوت"
        else:
                         xing = "برج الحمل"
    if month==4:
        if day<=19:
                         xing = "برج الحمل"
        else:
                         xing = "برج الثور"
    if month==5:
        if day<=20:
                         xing = "برج الثور"
        else:
                         xing = "الجوزاء"
    if month==6:
        if day<=21:
                         xing = "الجوزاء"
        else:
                         xing = "السرطان"
    if month==7:
        if day<=22:
                         xing = "السرطان"
        else:
                         xing = "ليو"
    if month==8:
        if day<=22:
                         xing = "ليو"
        else:
                         xing = "برج العذراء"
    if month==9:
        if day<=22:
                         xing = "برج العذراء"
        else:
                         xing = "الميزان"
    if month==10:
        if day<=23:
                         xing = "الميزان"
        else:
                         xing = "برج العقرب"
    if month==11:
        if day<=22:
                         xing = "برج العقرب"
        else:
                         xing = "القوس"
    if month==12:
        if day<=21:
                         xing = "القوس"
        else:
                         xing = "الجدي"
    return xing
c = CalXingzuo()

print ("بروجك هو {}.". format (c))
 
 