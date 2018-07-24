# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:04:41 2018

@author: Dhaval
"""

from dashboard import MainDashboard
from courier import MainCourier
import sys,os
import random
import cx_Oracle

#from goto import goto, label
import time

def main_menu():
    #os.system('clear')
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("--------------- Welcome to RD SHIPMENTS PVT. LMT.---------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("-------------- List of Cities in Which We Operate --------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    con=cx_Oracle.connect("system/sys@localhost/xe")
    cur=con.cursor()
    cur.execute("""select distinct tto from cost_city""")    
    putlist=cur.fetchall()
    for i in range(len(putlist)):
        print(" "+str(i+1)+". "+putlist[i][0].upper()+"\t",end=" ")
    con.close()
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")

    print ("Please choose an action:")
    print ("1.Sign In")
    print ("2.Sign Up")
    print ("3.Track the Courier")
    print ("0. Quit")
    choice =input("Enter your choice : ")
    exec_menu(choice)
    return
	
	
	
	
	

def exec_menu(choice):
    #os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print("Invalid selection, please try again.\n")
            menu_actions['main_menu']()
    return
#strating of signin menu
   
    
def track_order():
    print("\n\n----------------------------------------------------------------------")
    print("--------------- Track your order with Google Maps --------------------")
    print("----------------------------------------------------------------------")
    track_id = input("Enter track id : ")
    con=cx_Oracle.connect("system/sys@localhost/xe")
    cur=con.cursor()
    cur.execute("""select * from courier 
                        where ttrackid=:1 """,
                        {"1":track_id})    
    putlist=cur.fetchall()
    con.close()
    if(len(putlist)>0):
        coriobj=MainCourier(track_id)
        custobj=MainDashboard(coriobj.tocustphone)
        cmpobj=MainDashboard(coriobj.fromcmpphone)
        print("\n------------------------------")
        print("------------------------------")
        print("\t Trackid : "+coriobj.trackid)
        print("\t Shipment type : "+coriobj.shipmenttype)
        print("\t Shipment weight : "+str(coriobj.weight))
        print("------------------------------")
        print("\t Current Status : "+coriobj.status)
        print("\t Dispatched from : "+cmpobj.city)
        print("\t Final Destination : "+custobj.city)
        print("------------------------------")
        print("------------------------------")
        import webbrowser
        url="https://www.google.com/maps/dir/?api=1&origin="+coriobj.status+"&destination="+custobj.city
        webbrowser.open(url, autoraise=True)
    else:
        print("Sorry, It seems like entered trackid doesn't exist :\ ")
    
    print ("\n9. Back")
    print ("0. Quit")
    choice = input("Enter your choice : ")   
    exec_menu(choice)
    return


#Dashboard Menu
def gotoclassdashboard(putphone):
    #os.system('clear')

    cmpobj=MainDashboard(putphone)
    gotfullname=cmpobj.fullname.upper()
    print("\n\n")
    print("----------------------------------------------------------------------")
    print("------------------------- Welcome ------------------------------------")
    print("--------------- "+gotfullname)
    print("----------------------------------------------------------------------")
    

    print("1.Create New Courier")
    print("2.Update Existing Courier Details")
    print("3.Change Courier Status")
    print("4.Cancle Courier ")
    
    #print("4.Search & Statistics ")
    
    choice = input("Enter your choice : ")
    #exec_menu(choice)
     
    
    if(choice=='1'):
        cmpobj.new_courier()
    elif(choice=='2'):
        cmpobj.existing_courier()
    elif(choice=='3'):
        cmpobj.change_status()
    elif(choice=='4'):
        cmpobj.cancel_courier()
    else:
        print("Invalid Choice")
        
    print ("\n9. Back")
    print ("0. Quit")
    choice = input("Enter your choice : ")   
    exec_menu(choice)
    return

def checkindatabase(putphone,putpass):
    con=cx_Oracle.connect("system/sys@localhost/xe")
    cur=con.cursor()
    cur.execute("""select * from users 
                        where tphone=:1 and tpassword=:2""",
                        {"1":putphone,"2":putpass})
    cur.fetchall()
    if(cur.rowcount>=1):
        print("\n\t\tLogin Successful !!!")
        con.close()
        return True
    else:
        con.close()
        return False   
#Sign in
def signin():
    #os.system('clear')
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------- Login in ---------- --------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")

    #label .logindata
    print("\nEnter the Phone number & Password")
    phone=int(input("Enter PHONE NUMBER : "))
    password=input("Enter PASSWORD : ")
    
    if(checkindatabase(phone,password)):
        print("You will be redirected to Main dashboard in 5 seconds")
        print("Loading...")
        for i in range(6):
            sys.stdout.write("\r" + str(6-i))
            sys.stdout.flush()
            time.sleep(1)
        print("")
        gotoclassdashboard(phone)
    else:
        print("\t\tSorry, Login Failed...\n\t\t Please Enter the valid phone number or password")
        print("\t\tTry again :)")
        #goto .logindata
        
    return
#ending of the signin menu











#sign up
def entreindatabase(putfname,putemail,putphone,putadd,putpost,putcity,putpass):
    con=cx_Oracle.connect("system/sys@localhost/xe")
    cur=con.cursor()
    cur.execute("""select * from users 
                        where tphone = :1""", 
                        {"1":putphone})
    putlist=cur.fetchall()
    if(len(putlist)>0):
        print("\t\tSorry, This Phone number already exists")
        con.close()
        return False
    cur.execute("""select * from cost_city 
                        where tfrom = :1""",
                        {"1":putcity})
    putlist=cur.fetchall()
    if(len(putlist)>0):
        try:
            cur.execute("""insert into users 
                            values(:1,:2)""",
                            {"1":putphone,"2":putpass})
            cur.execute("""insert into c_details 
                                values(:1,:2,:3,:4,:5,:6)""",
                                {"1":putfname,"2":putemail,"3":putphone,"4":putadd,"5":putpost,"6":putcity})
            con.commit()
        except cx_Oracle.DatabaseError as e:
            print("Error in Database : ")
            print(e)
        finally:    
            con.close()
        return True
    else:
        print("\t\tSorry, Currently We dont\'t provide service in "+putcity+" city")
        con.close()
        return False
def signup():
    #os.system('clear')
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------- Sign Up ----------- --------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")
    print("----------------------------------------------------------------------")

    #label .enterdata
    full_name=input("Enter Full Name : ")
    company_email = input("Enter Email Address : ")
    address = input("Enter Address : ")
    city = input("Enter City : ")
    pincode = int(input("Enter Pincode : "))
    phone = int(input("Enter Phone Number : "))
    password = input("Enter password : ")
    confirm_password = input("Confirm Password : ")
    
    if(password == confirm_password):
         if(entreindatabase(full_name,company_email,phone,address,pincode,city,password)):
             print("Sign Up Successful !!!!!")
             print("You will be redirected to main menu in 5 seconds")
             print("Loading...")
             for i in range(5):
                sys.stdout.write("\r" + str(5-i))
                sys.stdout.flush()
                time.sleep(1)
             print("")
             main_menu()
         else:
            print("Try again")
    else:
        print("Password doesn't Match , Try Again...")
        #goto .enterdata
    return
#end of sign up
    

def back():
    menu_actions['main_menu']()

def done():
    return
# Exit program

 
menu_actions = {
    'main_menu': main_menu,
    '1': signin,
    '2': signup,
    '3': track_order,
    '9': back,
    '0': done,
}

if __name__ == "__main__":
    main_menu()