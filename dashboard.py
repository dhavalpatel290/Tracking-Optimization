# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 23:44:56 2018

@author: Dhaval
"""

import cx_Oracle
import os
from courier import MainCourier



class MainDashboard:
    def __init__(self, gotphone):  
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select * from c_details
                            where tphone=:1 """,
                            {"1":gotphone})
        putlist=cur.fetchall()
        con.close()
        gottuple=putlist[0]
        self.fullname = gottuple[0]
        self.email=gottuple[1]
        self.phone=gottuple[2]
        self.address=gottuple[3]
        self.postalcode=gottuple[4]
        self.city=gottuple[5]
    
    def printDetails(self):
        print(" \t\t Name      : "+self.fullname)
        print(" \t\t Address   : "+self.address)
        print(" \t\t City      : "+self.city)
        print(" \t\t Pin Code  : "+str(self.postalcode))
        print(" \t\t Email     : "+self.email)        
        print(" \t\t Phone no. : "+str(self.phone))
        return
        
    def getcost(self,weight,shipmenttype,tocity,fromcity):
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select tcost from cost_city 
                            where tfrom = :1 and tto=:2""", 
                            {"1":fromcity,"2":tocity})
        putlist=cur.fetchall()
        costcity=putlist[0][0]
        cur.execute("""select tcost from cost_shipmenttype 
                            where ttype = :1 """,
                            {"1":shipmenttype})
        putlist=cur.fetchall()
        costtype=putlist[0][0]
        cur.execute("""select tcost from cost_weight 
                            where tfrom <= :1 and tto >=:1""",
                            {"1":weight})
        putlist=cur.fetchall()
        costweight=putlist[0][0]
        totalcost=costcity+costtype+costweight
        return totalcost
    
    def insertintocourier(self,custobj,putweight,putshipmenttype,puttrackid):
        putstatus=self.city
        putcost=self.getcost(putweight,putshipmenttype,custobj.city,self.city)
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""insert into courier 
                            values(:1,:2,:3,:4,:5,:6,:7)""",
                            {"1":self.phone,"2":custobj.phone,"3":putweight,"4":putshipmenttype,"5":puttrackid,"6":putstatus,"7":putcost})
        con.commit()
        con.close()
        print("Order Placed Successfully !!")
        print("Here's the full reciept")
        coriobj=MainCourier(puttrackid)
        #print("done cori")
        coriobj.printReceipt()
    
    def usercheck(self,cmpphone,custphone):
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select tfullname from c_details
                            where tphone = :1""", 
                            {"1":custphone})
        putlist=cur.fetchall()
        if(len(putlist)>0):
            obj=MainDashboard(custphone)
            con.close()
            return True,obj
        else:
            con.close()
            return False,None
    
    def change_status(self):
        track_id = input("Enter track id : ")
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select * from courier 
                        where ttrackid=:1 and tfrom=:2""",
                        {"1":track_id,"2":self.phone})
        putlist=cur.fetchall()
        if(len(putlist)>0):
            coriobj=MainCourier(track_id)
            custobj=MainDashboard(coriobj.tocustphone)
            print("\n------------------------------")
            print("Details of Courier")
            print("------------------------------")
            print("\t Trackid : "+coriobj.trackid)
            print("\t Shipment type : "+coriobj.shipmenttype)
            print("\t Shipment weight : "+str(coriobj.weight))
            print("------------------------------")
            print("\t Old Status : "+coriobj.status)
            print("\t Dispatched from : "+self.city)
            print("\t Final Destination : "+custobj.city)
            print("------------------------------")
            print("------------------------------")
            newinput = input("Enter current city : ")
            cur.execute("""update courier set tstatus=:1 
                            where ttrackid=:2""",
                            {"1":newinput,"2":track_id})
            con.commit()
            con.close()
            print("Status Updated Successfully !!")
            print("\nUpdated Details of Courier ")
            print("\n------------------------------")
            print("------------------------------")
            print("\t Trackid : "+coriobj.trackid)
            print("\t Shipment type : "+coriobj.shipmenttype)
            print("\t Shipment weight : "+str(coriobj.weight))
            print("------------------------------")
            print("\t Updated Status : "+newinput)
            print("\t Dispatched from : "+self.city)
            print("\t Final Destination : "+custobj.city)
            print("------------------------------")
            print("------------------------------")
        else:
            print("Sorry, It seems like entered trackid doesn't exist :\ ")
            con.close()
        return
  
    #Create New Courier
    def new_courier(self):
        print("----------------------------------------------------------------------")
        print("----------------------------------------------------------------------")
        print("--------------- Welcome to RD SHIPMENTS PVT. LMT.---------------------")
        print("----------------------------------------------------------------------")
        print("--------------- Your going to place a new courier --------------------")
        print("----------------------------------------------------------------------")
        customer_phone =int(input("Enter phone number of customer : "))
        didexist,custobj=self.usercheck(self.phone,customer_phone)
        if(didexist):
            print("Entered customer already exist")
            print("Here's the customer detail")
            custobj.printDetails()
            print("Now, Enter the asked details :")
            putweight = float(input("courier weight(Kg) ? "))
            putshipmenttype = input("Shipment type(express/fast/regular) ? ")
            puttrackid=get_number()
            print("Your Unique Trackid is "+puttrackid)  # in main dbms table it is varchar() 
            self.insertintocourier(custobj,putweight,putshipmenttype,puttrackid)
        else:
            
            full_name=input("Enter Full Name : ")
            email = input("Enter Email Address : ")
            putadd = input("Enter Address : ")
            putcity = input("Enter City : ")
            putpost = int(input("Enter Pincode : "))  
            putweight = float(input("courier weight(Kg) ? "))
            putshipmenttype = input("Shipment type(express/fast/regular) ? ")
            puttrackid=get_number()
            print("Your Unique Trackid is "+puttrackid)  # in main dbms table it is varchar() 
            con=cx_Oracle.connect("system/sys@localhost/xe")
            cur=con.cursor()
            cur.execute("""insert into c_details 
                                values(:1,:2,:3,:4,:5,:6)""",
                                {"1":full_name,"2":email,"3":customer_phone,"4":putadd,"5":putpost,"6":putcity})
            con.commit()
            con.close()
            didexist,custobj=self.usercheck(self.phone,customer_phone)
            self.insertintocourier(custobj,putweight,putshipmenttype,puttrackid)
    
        return
    
    #existing courier
    def existing_courier(self): 
        print("\n\nTo change details of courier, ")
        track_id = input("Enter track id : ")
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select * from courier 
                            where ttrackid=:1 and tfrom=:2""",
                            {"1":track_id,"2":self.phone})
        putlist=cur.fetchall()
        if(len(putlist)>0):

            coriobj=MainCourier(track_id)
            custobj=MainDashboard(coriobj.tocustphone)
            print("\nCurrent Details of Customer ")
            custobj.printDetails()
            
            print("Which item would you like to change ? ")
            print(" 1.Name of customer")
            print(" 2.Address of customer ")
            print(" 3.City of customer ")
            print(" 4.Pincode of customer ")
            print(" 5.Email of customer ")
            choice=int(input())
            if(choice<6):   
                connect_list=[[],[1,'tfullname','full name'],[2,'taddress','address'],[3,'tcity','city'],[4,'tpostalcode','pin code'],[5,'temail','mail address']]
                newinput = input("Enter new "+connect_list[choice][2]+" : ")
                query="update c_details set "+connect_list[choice][1]+"=:1 where tphone=(select tto from courier where ttrackid=:2)"
                cur.execute(query,{"1":newinput,"2":track_id})
                con.commit()
                con.close()
                print("\n\nAll changes have been saved...")
                custobj=MainDashboard(coriobj.tocustphone)
                print("\n Updated Details of Customer ")
                custobj.printDetails()
                print("Order Updated Successfully !!")
                print("Here's the new reciept")
                coriobj=MainCourier(track_id)
                custobj=MainDashboard(coriobj.tocustphone)
                path ='.//Company//'+self.fullname+'//'+self.city+'To'+custobj.city+'//'+str(custobj.postalcode)+'//'
                os.remove(path+'Order_'+str(coriobj.trackid)+'.txt')
                coriobj.printReceipt()
            else:
                print("Invalid Choice")
                con.close()
        else:
            print("Sorry, It seems like entered trackid doesn't exist :\ ")
            con.close()
        return
  
    #cancel courier
    def cancel_courier(self):
        track_id = input("Enter track id : ")
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        cur.execute("""select * from courier 
                            where ttrackid=:1 and tfrom=:2""",
                            {"1":track_id,"2":self.phone})
        putlist=cur.fetchall()
        if(len(putlist)>0):
            ch=input("\tAre you sure you want to delete the shipment (y/n) ? ")
            if(ch=="y"):
                coriobj=MainCourier(track_id)
                custobj=MainDashboard(coriobj.tocustphone)
                path ='.//Company//'+self.fullname+'//'+self.city+'To'+custobj.city+'//'+str(custobj.postalcode)+'//'
                os.remove(path+'Order_'+str(coriobj.trackid)+'.txt')
                cur.execute("""delete from courier 
                                    where ttrackid=:1""",
                                    {"1":track_id})
                con.commit()
                con.close()
                print("Order Deletion Successfull !!! ")
            else:
                con.close()
                print("Deletion ABORTED !!!")
        else:
            print("Sorry, It seems like entered trackid doesn't exist :\ ")
            con.close()
        
        return
    
    #def getStatistics(self):
def get_number():
    con=cx_Oracle.connect("system/sys@localhost/xe")
    cur=con.cursor() 
    cur.execute("""select * from courier""")
    putlist=cur.fetchall()
    con.close()
    return str(len(putlist)+1)

   
        
        
        
#obj=MainDashboard(848)
#obj.new_courier()