##1
a=eval(input("請輸入國文成績:"))
if a<0 :
    print("輸入錯誤,請重新輸入")
    a=eval(input("請輸入國文成績:"))

b=eval(input("請輸入英文成績:"))
if b<0:
    print("輸入錯誤,請重新輸入")
    b=eval(input("請輸入英文成績:"))
c=eval(input("請輸入數學成績:"))
if c<0:
    print("輸入錯誤,請重新輸入")
    c=eval(input("請輸入數學成績:"))

    
    print(f"總分為:{a+b+c},平均成績為:{(a+b+c)//3}。")
##2
a=eval(input("請輸入梯形上底:"))
if a<=0 :
    print("輸入錯誤,請重新輸入")
    a=eval(input("請輸入梯形上底:"))
b=eval(input("請輸入梯形下底:"))
if b<=0:
    print("輸入錯誤,請重新輸入")
    b=eval(input("請輸入梯形下底:"))
c=eval(input("請輸入梯形高:"))
if c<=0:
    print("輸入錯誤,請重新輸入")
    c=eval(input("請輸入梯形高:"))

print(f"梯形面積為{((a+b)*c)//2}")
##3
a=eval(input("請輸入消費總金額:"))

if a >=2000:
    b=a*0.75
else:
    b=a*1
print("需支付金額為",b)
##4

month=int(input("請輸入月份:"))
while True:
    if 3<=month<=5:
        print(("季節為春天"))
        break
    elif  6<=month<=8:
        print("季節為夏天")
        break
    elif  9<=month<=11:
        print("季節為秋天")
        break
    elif month==12 or 1<=month<=2:
        print("季節為冬天")
        break
    else:
        month=int(input("輸入錯誤,請重新輸入月份:"))

##5
num1=0
for i in range(16):
    agg=1+(i*(i-1)/2)
    num1=num1+agg
print(num1)

##6
eng_Sentence=str(input("請輸入英文句子:"))

list1=eng_Sentence.split()

print(list1)
##7
list1=[]

while True:
    name=input("請輸入姓名,若要結束查詢請輸入finish:")
    if name.upper() == "FINISH":
        break
    number=input("請輸入電話,若要結束查詢請輸入finish:")         
    if number.upper() =="FINISH":
        break
    list1.append(name)
    list1.append(number)
searchName=input("請輸入想查詢的姓名或電話,若要終止查詢請輸入stop:")      
while searchName.upper()!="STOP":   
        for i,element in enumerate(list1):           
             if element==searchName and i%2==0:                 
                print("姓名:",searchName,"的電話是",list1[i+1])
             elif element==searchName and i%2!=0:                 
                print("電話:",searchName,"的姓名是",list1[i-1])
        if searchName not in list1:                
            print("不在通訊錄中")
        searchName=input("請輸入想查詢的姓名或電話,若要終止查詢請輸入stop:")                        
else: 
   print("查詢結束")
#####7-1
dic1={}
while True:
    name=input("請輸入姓名,若要結束查詢請輸入finish:")
    if name.upper() == "FINISH":
        break
    number=input("請輸入電話,若要結束查詢請輸入finish:")         
    if number.upper() =="FINISH":
        break
    dic1[name]=number
searchName=input("請輸入想查詢的姓名,若要終止查詢請輸入stop:")      
while searchName.upper()!="STOP":   
        for i,element in enumerate(dic1):           
             if element==searchName:                 
                print("姓名:",searchName,"的電話是",dic1[searchName])   
        if searchName not in dic1:                
            print("不在通訊錄中")
        searchName=input("請輸入想查詢的姓名或電話,若要終止查詢請輸入stop:")                        
else: 
   print("查詢結束")

##8
def f(x,y):
    return x**y

cal_1=int(input("請輸入要計算的整數:"))
cal_2=int(input("請輸入要計算的次方數:"))
print(f'{cal_1}的{cal_2}次方為{f(cal_1,cal_2):,.0f}')
         

           

