w,x,y,z=[],[],[],[]
def prt(brand,price,discount,sale,countr):
    w.append(brand)
    x.append(price)
    y.append(discount)
    z.append(sale)
    count1=0
    print("-------------------------------------------------------------")
    print("รุ่น                            ราคา             ส่วนลด           จ่ายจริง")
    print("-------------------------------------------------------------")
    e=1
    for i in range(0,countr,1):
        print(e,w[i]+"           "+x[i]+"             "+y[i]+"             "+str(z[i]))
        count1+=z[i] 
        e+=1
    print("--------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\t\t       -TOTAL-\n\t\t\t\t\t\t\t\t        "+str(count1))
    print("--------------------------------------------------------------------------------")
count=0
while True:
    print("====================================\n\tCellphone by PHN\n====================================\nBrand list:\n1) Apple[a]\n2) Samsung[s]\n3) Huawei[h]\n4) Oppo[o]\n5) Exit [e]")
    b=input("[Select brand]: ")
    count+=1
    if b == 'a' or b == 'A':
        print("--------------------------Apple---------------------------")
        print("1. Apple iPhone X")
        print("2. Apple iPhone 11")
        print("3. Apple iPhone 8")
        t=input("Select : ")
        if t == '1':
            prt("Apple iPhone X  ","24600","20%",19680,count)
        elif t == '2':
            prt("Apple iPhone 11 ",'34000','20%',27200,count)
        elif t == '3':
            prt("Apple iPhone 8  ",'18600','20%',14880,count)
        else:
            print("[ Error,Please input a number (1,2,3) ]")
            continue
    elif b == 's' or b == 'S':
        print("--------------------------Samsung---------------------------")
        print("1. Samsung S10")
        print("2. Samsung A50")
        print("3. Samsung Note 10+")
        t=input("Select : ")
        if t == '1':
            prt("Samsung S10     ",'25000','30%',17500,count)
        elif t == '2':
            prt("Samsung A50     ",'18600','30%',13020,count)
            continue
        elif t == '3':
            prt("Samsung Note 10+",'37300','30%',2110,count)
            continue
        else:
            print("[ Error,Please input a number (1,2,3) ]")
            continue
    elif b == 'h' or b == 'H':
        print("--------------------------Huawei---------------------------")
        print("1. HUAWEI Mate 20")
        print("2. Huawei P30 Pro")
        print("3. Huawei Nova 5T")
        t=input("Select : ")
        if t == '1':
            prt("HUAWEI Mate 20t ",'14599','70%',4380,count)
            continue
        if t == '2':
            prt("Huawei P30 Pro  ",'22599','70%',6780,count)
            continue
        if t == '3':
            prt("Huawei Nova 5T  ",'10900','70%',32700,count)
            continue
        else:
            print("[ Error,Please input a number (1,2,3) ]")
            continue
    elif b == 'o' or b == 'O':
        print("--------------------------Oppo---------------------------")
        print("1. Oppo A5")
        print("2. Oppo A4")
        print("3. Oppo A3")
        t=input("Select : ")
        if t == '1':
            prt("Oppo A5        ",'20000','15%',17000,count)
            continue
        if t == '2':
            prt("Oppo A4        ",'30000','15%',25500,count)
            continue
        if t == '3':
            prt("Oppo A3        ",'25000','15%',21250,count)
            continue
    elif b == 'e' or b == 'E':
        print("\n\t=== See you next time.! ===")
        break
    else:
        print("\n!!!!!!Error,Please input again [A,S,C,B,E,a,s,c,b,e]!!!!!!\n")
        continue