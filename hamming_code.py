import random
print("------------------------  WELCOME TO 7-bit HAMMING CODE SIMULATOR -------------------------")
print("")
data=input("Enter data stream : ")
#print(data)
while len(data)%4!=0:
    data='0'+data
ham=""
print("Tokenised Data :",data)
arr=list()
for i in range(int(len(data)/4)):
    d7,d6,d5,d3= data[i*4:(i+1)*4]
    #print(d7,d6,d5,d3)
    ham=ham+d7+d6+d5
    k=int(d5)^int(d6)^int(d7)
    if k==0:
        p4="0"
    elif k==1:
        p4="1"
    ham=ham+p4+d3
    ######
    #######
    k = int(d3)^int(d6)^int(d7)
    if k == 0:
        p2 = "0"
    elif k == 1:
        p2 = "1"
    ham = ham + p2
    ######
    #######
    k = int(d3)^int(d5)^int(d7)
    if k == 0:
        p1 = "0"
    elif k == 1:
        p1 = "1"
    ham = ham + p1
    ######
    ham=ham+" "
print("_________________________________________________________________________________________________________________")
print("Hamming code generated at sender end:",ham)
print("_________________________________________________________________________________________________________________")
ham1=ham.replace(" ","")
#print(ham1)
ham2=""
eham=ham1
elist=list()
clist=list()
appended=list()

for i in range(len(eham)):
    elist.append(int(eham[i]))
    clist.append(int(eham[i]))
#print("elist=",elist)
print("-----------------------------------------------------------------------------------------------------------------")
print("Data is ready for transmission......")
print("-----------------------------------------------------------------------------------------------------------------")
p=input("Enter probability:")
p=float(p)
print("_________________________________________________________________________________________________________________")
for i in range(int(len(eham)/7)):
    values=range(11)
    x=random.choice(values)/10
    d7, d6, d5, p4, d3, p2, p1 = elist[7 * i:(i + 1) * 7]
    err = random.choice([1, 2, 3, 4, 5, 6])
    print("Random error position =", err)
    if x>p :
        #print("one",a,p) #just for checking mam
        #continue
        z=0
        z+=1#nothing

    else:
        if err==1:
            if p1==1:
                p1=0
            else:
                p1=1
        if err==2:
            if p2==1:
                p2=0
            else:
                p2=1
        if err==4:
            if p4==1:
                p4=0
            else:
                p4=1
        if err==3:
            if d3==1:
                d3=0
            else:
                d3=1
        if err==5:
            if d5==1:
                d5=0
            else:
                d5=1
        if err==6:
            if d6==1:
                d6=0
            else:
                d6=1

    f_ham=[d7,d6,d5,p4,d3,p2,p1]
    print("random probability:",x)
#
    print("Data word",i+1,"after passing through channel : ",f_ham)
    appended=appended+f_ham
    print("-------------------------------------------------------------------------------------------------------------")



####################################################################################
print("message without error:",clist)
print("message with error   :",appended)

##########################  error detection #################################
for i in range(int(len(appended)/7)):
    d7,d6,d5,p4,d3,p2,p1 = appended[7*i:(i+1)*7]

    P1=d7^d5^d3^p1
    P2=d7^d6^d3^p2
    P4=d7^d6^d5^p4
    if P4==0 and P2==0 and P1==0:
        pos=0
    if P4==0 and P2==0 and P1==1:
        pos=1
    if P4==0 and P2==1 and P1==0:
        pos=2
    if P4==0 and P2==1 and P1==1:
        pos=3
    if P4==1 and P2==0 and P1==0:
        pos=4
    if P4==1 and P2 == 0 and P1 == 1:
        pos = 5
    if P4==1 and P2==1 and P1==0:
        pos=6
    print("___________________________________________________________________________")
    print("___________________________________________________________________________")
    print("Data word",i+1,":","[",d7,d6,d5,p4,d3,p2,p1,"]")
    if pos==0:
        print("No error!!")
    if pos==1 or pos==2 or pos==4:
        print("There is only ONE error")
        print("Error position     :",pos)
        if pos==1:
            if p1==1:
                p1=0
            else:
                p1=1
            print("Corrected Data Word:","[",d7,d6,d5,p4,d3,p2,p1,"]")
        if pos==2:
            if p2==1:
                p2=0
            else:
                p2=1
            print("Corrected Data Word:","[",d7,d6,d5,p4,d3,p2,p1,"]")
        if pos==4:
            if p4==1:
                p4=0
            else:
                p4=1
            print("Corrected Data Word:","[",d7,d6,d5,p4,d3,p2,p1,"]")


    if pos==3 or pos==5 or pos==6:
        print("There are TWO errors!!")
        if pos==3:
            print("Error at parity: 1 and 2")
            print("Correction at : 3rd, data bit")
            if d3==1:
                d3=0
            else:
                d3=1
            print("Corrected Data Word:","[",d7,d6,d5,p4,d3,p2,p1,"]")

        if pos==5:
            print("Error at parity: 1 and 4")
            print("Correction at : 5th,data bit")
            if d5==1:
                d5=0
            else:
                d5=1
            print("Corrected Data Word:","[",d7,d6,d5,p4,d3,p2,p1,"]")

        if pos==6:
            print("Error at parity: 2 and 4")
            print("Correction at : 6th,data bit")
            if d6==1:
                d6=0
            else:
                d6=1
            print("Corrected Data Word:","[",d7,d6,d5,p4,d3,p2,p1,"]")

    print("____________________________________________________________________________")


n=input()