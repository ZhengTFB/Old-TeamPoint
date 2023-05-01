import time
list1 = []
z1=0
z2=0
z3=0
z4=0
z5=0
z6=0
z7=0
z8=0
z9=0
try:
    file = open('积分.txt', 'r')
except FileNotFoundError:
    print('File is not found')
else:
    lines = file.readlines()
    for line in lines:
        a = line.split()
        x = a[0]
        list1.append(x)
file.close()
JFFZ=[]
for x in list1:
 #   print(x)
    JFFZ.append(int(x))
#print(JFFZ)

list2 = []
try:
    file = open('积分.txt', 'r')
except FileNotFoundError:
    print('File is not found')
else:
    lines = file.readlines()
    for line in lines:
        a = line.split()
        x = a[2]
        list2.append(x)
file.close()
JFZH=[]
for x in list2:
  #  print(x)
    JFZH.append(int(x))
#print(JFZH)
ZS=(len(JFZH))
zs1=ZS-1
while zs1>-1:
    F=int(JFFZ[zs1])
    Z=int(JFZH[zs1])
 #   print(F,Z)
    if Z==1:
        z1=z1+F
    elif Z==2:
        z2=z2+F
    elif Z==3:
        z3=z3+F
    elif Z==4:
        z4=z4+F
    elif Z==5:
        z5=z5+F
    elif Z==6:
        z6=z6+F
    elif Z==7:
        z7=z7+F
    elif Z==8:
        z8=z8+F
    elif Z==9:
        z9=z8+F
    zs1=zs1-1
dic = [(z1,1),(z2,2), (z3,3), (z4,4), (z5,5), (z6,6),(z7,7), (z8,8), (z9,9)]
dic.sort()
a1=dic[0]
print('输出进度')
print('■')
time.sleep(0.6)
print('■')
time.sleep(0.31)
print('■')
time.sleep(1)
print('■')
time.sleep(0.2)
print('■')
time.sleep(0.1)
print('输出完成')
time.sleep(1)

print('第九名的分数是:',a1[0],'分   组号是:',a1[1])
time.sleep(1)

a2=dic[1]
print('第八名的分数是:',a2[0],'分   组号是:',a2[1])
time.sleep(1)

a3=dic[2]
print('第七名的分数是:',a3[0],'分   组号是:',a3[1])
time.sleep(1)

a4=dic[3]
print('第六名的分数是:',a4[0],'分   组号是:',a4[1])
time.sleep(1)

a5=dic[4]
print('第五名的分数是:',a5[0],'分   组号是:',a5[1])
time.sleep(1)

a6=dic[5]
print('第四名的分数是:',a6[0],'分   组号是:',a6[1])
time.sleep(1.5)

a7=dic[6]
print('第三名的分数是:',a7[0],'分   组号是:',a7[1])
time.sleep(1.9)

a8=dic[7]
print('第二名的分数是:',a8[0],'分   组号是:',a8[1])
time.sleep(2)

a9=dic[8]
print('第一名的分数是:',a9[0],'分   组号是:',a9[1])
time.sleep(10000)
