import sqlite3
import random as r
con=sqlite3.connect("c:\sqlite3\Second.db")
cur=con.cursor()
class Bank:
    cur.execute("create table if not exists Bank(acc text(10) primary key,pin text(4),name text(50),bal integer)")
    def create_acc(self):
        name=input("enter name")
        ac_no = "1"
        for i in range(9):
            ac_no = ac_no + str(r.randint(0, 9))
        pin=""
        for i in range(4):
            pin = pin + str(r.randint(0, 9))
        cur.execute("insert into Bank values(?,?,?,?)",(ac_no,pin,name,0))
        con.commit()
        print("account created successfully")
        cur.execute(f"select * from Bank where acc={ac_no}")
        i = cur.fetchone()
        print(i)
    def view(self,acc):
        cur.execute(f"select acc,name,bal from Bank where acc={acc}")
        i=cur.fetchall()
        if not i:
            print("no such account")
        else:
            print(i)
    def deposit(self,acc,amt):
        cur.execute(f"select acc from Bank where acc={acc}")
        i = cur.fetchone()
        if i:
            cur.execute(f"update Bank set bal=bal+{amt} where acc={acc}")
            print("amount deposited successfully")
        else:
            print("please enter valid account number")
    def withdraw(self,acc,amt,pin):
        cur.execute(f"select acc,pin,bal from Bank where acc={acc}")
        i=cur.fetchall()
        if not i:
            print("please enter valid account number")
        elif pin!=i[0][1]:
            print("invalid pin")
        elif not (i[0][2]>amt):
            print("insufficient balance")
        else:
            cur.execute(f"update Bank set bal=bal-{amt} where acc={acc}")
            print("amount withdrawn successfully")
obj=Bank()
print("Welcome to our bank")
exit=1
while(exit):
    print("1.create account")
    print("2.view details")
    print("3.deposit")
    print("4.withdraw")
    s=int(input("enter your option"))
    match(s):
        case 1:
            obj.create_acc()
        case 2:
            acc = input("enter account number")
            obj.view(acc)
        case 3:
            acc= input("enter account number")
            amt= int(input("enter amount"))
            obj.deposit(acc,amt)
            con.commit()
        case 4:
            acc = input("enter account number")
            amt = int(input("enter amount"))
            pin=input("enter pin")
            obj.withdraw(acc,amt,pin)
            con.commit()
    exit=int(input("enter 0 for exit,1 for continue"))
print("Thankyou visit us again")