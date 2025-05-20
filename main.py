import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='*************')

cur=con.cursor()
cur.execute("create database if not exists cafe_management")
cur.execute("use cafe_management")
cur.execute("create table if not exists coffee(sno int,products varchar(20),cost int)")
sql="select*from coffee"
cur.execute(sql)
res=cur.fetchall()
if res==[]:
    cur.execute("insert into coffee values(1,'coffee',240)")
    cur.execute("insert into coffee values(2,'chocolate',140)")
    con.commit()

cur.execute("create table if not exists available(Sno int,varieties varchar(20))")
sql="select*from available"
cur.execute(sql)
res=cur.fetchall()
if res==[]:
  cur.execute("insert into available values(1,'espresso')")
  cur.execute("insert into available values(2,'latte')")
  cur.execute("insert into available values(3,'black coffee')")
  cur.execute("insert into available values(4,'capacino')")
  con.commit()
 
cur.execute("create table if not exists staff(Sno int,Name varchar(20),Salary int)")
sql="select*from staff"
cur.execute(sql)
res=cur.fetchall()
if res==[]:
    cur.execute("insert into staff values(1,'Ram',12000)")
    cur.execute("insert into staff values(2,'Shyam',11000)")
    cur.execute("insert into staff values(3,'Raju',10000)")
    con.commit()

from datetime import datetime

print(".><><><><><><><><><><><><><><><><><><><><><><><.")
print( ":::::::::::::::::_________WELCOME_________::::::::::::::::: ")
print("::::::::::::::::::____________TO____________:::::::::::::::::: ")
print("..........................COFFEE SHOP SYSTEM........................")
print(".><><><><><><><><><><><><><><><><><><><><><><><.")

ch=' '
while ch!='N' or ch!='n':
 print("\n\nPLEASE CHOOSE \n1 FOR ADMIN \n2 FOR CUSTOMER\n3 for EXIT:\n")

 choice=int(input("Enter your choice:"))
 if choice==3:
        break

if choice==1:
    admin=input("USERNAME:")
    password=int(input("ENTER PASSWORD:"))
    if password==1234:
     print("**HELLO SIR, You logged in as Admin successfully**")
     print('------------------------------------------------------------------------')
     print("Press 1 To Add coffee in the cafe....")
     print("Press 2 To See coffee in the cafe....")
     print("Print 3 to update cost of any coffee....")
     print("Press 4  To Add toppings of your choice in cafe....")
     print("Press 5 To Add staff in the cafe.................")
     print("Print 6 To see staffs.....")
     print("Print 7 To update salary of any staff:")

    c=int(input('Enter your choice:'))
    if c==1:
       def add():
        sno=int(input("Enter sno:"))
        product1=input("Enter product name:")
        cost=int(input("Enter the cost:"))
        d1=(sno,product1,cost)
        s1='insert into coffee values (%s,%s,%s)'
        cur.execute(s1,d1)
        con.commit()
        print('.....................................COFFEE ADDED SUCCESSFULLY..................................')
    add()
elif c==2:
      def items():
       print("Items in the cafe:")
       sql="select*from coffee"
      cur.execute(sql)
      res=cur.fetchall()
      t=(['serial_no','products','cost'])
      for serial_no,products,cost in res:
           print(serial_no,":","\t",products,":\t\t",'cost',cost)
      items()
elif c==3:
      def money():
           sno=input("Enter the sno of product:")
           n_cost=input("Enter the Rupees to be added:")
           cur.execute("update coffee set cost=cost+"+n_cost+" where sno="+sno+';')
           con.commit()
           print("TABLE AFTER UPDATION:")
           sq="select*from coffee"
           cur.execute(sq)
           res=cur.fetchall()
           t=(['sno','products','cost'])
           for sno,products,cost in res:
             print(sno,":","\t",products,":","\t",'Cost',cost)
             money()
elif c==4:
      def variety():
         sno=input("Enter sno:")
         varieties=input("Enter varieties:")
         d2=(sno,varieties)
         s2='insert into available values(%s,%s)'
         cur.execute(s2,d2)
         con.commit()
    variety()
    
elif c==5:
    def ad():
       sno=int(input("Enter sno:"))
       emp=input("Enter name:")
       salary=int(input("Enter the salary:"))
       dx=(sno,emp,salary)
       sy='insert into staff values (%s, %s,%s)'
       cur.execute(sy,dx)
       con.commit()
       print('........................staffs added successfully....................')
    ad()
elif c==6:
    def staffs():
        print("staffs in the shop:")
            sql="select*from staff"
            cur.execute(sql)
            res=cur.fetchall()
            t=(['serial_no', 'name','salary'])
            for serial_no,name,salary in res:
                print(serial_no,":","\t",name,":","\t",'cost',salary)
    staffs()
elif c==7:
       def up():
              print("Choose 1 to increse the salary:")
              print("Choose 2 to decrease:")
            name=input("Enter the name of EMPLOYEE:")

            
            n_salary=input("Enter the Rupees to be added:")

            sig=int(input("Enter choice(1/2):"))
            if sig==1:
                cur.execute("update staff set salary=salary+"+n_salary+" where name="+name+';')
                con.commit()
                print("TABLE AFTER UPDATION:")
            if sig==2:
                cur.execute("update staff set salary-salary-"+n_salary+"where name="+name+';')
                con.commit()
                print("TABLE AFTER UPDATION:")
                sq="select*from staff"
                cur.execute(sq)
                res=cur.fetchall()
                t=(['sno','name','salary'])
                for sno,name,salary in res:
                    print(sno,":","\t",name,":","\t",salary)
        up()


            
     else:
               print("SORRY..You have entered the Wrong Input, Input From 1 to 7")

    else:
              print("\t\t\t\t\t\t\t\ ***********Wrong Password ***********/t/t/t/t/t/t/t")
 elif choice==2:
         name=input("Enter your name:")
         phone=int(input("Enter your phone number:"))
         print("Press 1 to see the MENU ',sep='......')
         print('Press 2 to order an item')
        c=int(input("Enter your choice:'))
        if c==1:
            def items():
                 print("Items in the shop:")
                 sql="select*from coffee"
                 cur.execute(sql)
                 res=cur.fetchall()
                t=(['serial_no','products', 'cost'])
                for serial_no,products,cost in res:
                        print(serial_no,":","\t",products,":","\t",'cost',cost)
             items()
        elif c==2
                print("What do you want to order?")
                sql="select * from coffee"
                cur.execute(sql)
                res=cur.fetchall()
                t=(['serial_no','products','cost'])
                 for serial_no,products,cost in res:
                     print(serial_no,":","\t",products, ":","\t","cost",cost)
                sql="select sno from coffee"
                cur.execute(sql)
                res=cur.fetchall()
                print(res)
                l=[]
                for i in range(len(res)):
                      l.append(res[i][0])
                print(l)

    d=int(input("Enter your Serial No of the Item to Buy:"))
    if d==1:
        def items():
                print("Which coffee do you want?")
                kl="select*from available"
                cur.execute(kl)
                srh-cur.fetchall()
                 f=(['sno', 'varieties'])
                 for sno,varieties in srh:
                        print(sno,":","\t\t", varieties)
                 print("Choose which coffee do you want?")
                 ck=int(input("Enter choice:"))
                 if ck==1:
                      print("How much cups of espresso do you want?")
                      qty=int(input("Enter Qty."))
                       print("You have succesfully ordered your coffee!!!\t:")
                       cur.execute("select * from coffee where products='coffee""";')
                    for i in cur:
                        c=i[2]
                        con.commit()
                    print("Total amount:",qty*c)
                    print("\n")
                    print("YOUR BILL")
                    print("......................................ENJOY.............................")
                    print("Costumer's name:",name)
                    print("Contact no.:",phone)
                    print("Coffee type:Espresso")
                    print("No. of cups of coffee:",qty)
                    print("Total amount:",qty*c)
                    print("------------THANK_YOU FOR ORDERING FROM ISHITA'S CAFE-------------")
                    print("\t \t\t\tDate:",datetime.now())
                 if ck==2:
                 print("How much cups of latte coffee do you want?")
                 qty=int(input("Enter Qty."))
                 print("You have succesfully ordered your coffee!!!\t:")
                 cur.execute("select from*coffee where products='coffee""";")
                 for i in cur:
                        L=i[2]
                 print("Total amount",qty*L)
                 print("\n")
                 print("YOUR BILL")
                 print("......................................ENJOY.............................")
                 print("Costumer's name:",name)
                 print("Contact no.:",phone)
                 print("Coffee type:latte")
                 print("No. of cups of coffee:",qty)
                 print("Total amount:",qty*L)
                 print("------------THANK_YOU FOR ORDERING FROM ISHITA'S CAFE-------------")
                 print("\t \t\t\tDate:",datetime.now())
                 if ck==3:
                 print("How much cups of black coffee do you want?")
                 qty=int(input("Enter Qty."))
                 print("You have succesfully ordered your coffee!!!\t:")
                 cur.execute("select from*coffee where products='coffee""";")
                 for i in cur:
                        N=i[2]
                 print("Total amount",qty*N)
                 print("\n")
                 print("YOUR BILL")
                 print("......................................ENJOY.............................")
                 print("Costumer's name:",name)
                 print("Contact no.:",phone)
                 print("Coffee type:black coffee")
                 print("No. of cups of coffee:",qty)
                 print("Total amount:",qty*N)
                 print("------------THANK_YOU FOR ORDERING FROM ISHITA'S CAFE-------------")
                 print("\t \t\t\tDate:",datetime.now())
                 if ck==4:
                 print("How much cups of capacino coffee do you want?")
                 qty=int(input("Enter Qty."))
                 print("You have succesfully ordered your coffee!!!\t:")
                 cur.execute("select*from coffee where products='coffee""";")
                 for i in cur:
                        k=i[2]
                 print("Total amount",qty*k)
                 print("\n")
                 print("YOUR BILL")
                 print("......................................ENJOY.............................")
                 print("Costumer's name:",name)
                 print("Contact no.:",phone)
                 print("Coffee type:capacino")
                 print("No. of cups of coffee:",qty)
                 print("Total amount:",qty*k)
                 print("------------THANK_YOU FOR ORDERING FROM ISHITA'S CAFE-------------")
                 print("\t \t\t\tDate:",datetime.now())
            items()
      elif d==2:
          print("How much chocolate do you want:")
          past=int(input("enter your choice:"))
          print("You have successfully ordered",past," chocolate")
          cur.execute("select * from coffee where products='chocolate"";")
    for i in cur:
            c=i[2]
        print("Total amount =",past*c)
        print("\n")
        print("YOUR BILL")
        print("..................ENJOY....................")
        print("Costumer's name:",name)
        print("Contact no.:",phone)
        print("No. of chocolate:",past)
        print("Total amount:",past*c)
        print("------------THANK_YOU FOR ORDERING FROM ISHITA'S CAFE-------------")
        print("\t \t\t\tDate:",datetime.now())
    elif d in l:
        qty=int(input("Enter Qty."))
        print("You have successfully ordered your Selected item!!!!!!\t:")
        cur.execute("select*from coffee where sno="+str(d))
        for i in cur:
            L=i[2]
        print("Total amount",qty*L)
        print("\n")
        print("YOUR BILL")
        print("...........................ENJOY...............")
         print("Costumer's name:",name)
        print("Contact no.:",phone)
        print("Quantity:",qty)
        print("Total amount:",qty*L)
        print("------------THANK_YOU FOR ORDERING FROM ISHITA'S CAFE-------------")
        print("\t \t\t\tDate:",datetime.now())
    else:
        print("Wrong Input")

    else:
        print("\t\t\t\t\t\t\t**********************Wrong password*********************************************")
ch=input("DO YOU WANT TO CONTINUE (Y/N)?")
if ch=='n' or ch=="N":
    exit()


        
       


