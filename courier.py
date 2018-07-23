# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 00:23:44 2018

@author: Dhaval
"""
import cx_Oracle
import os

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
    

class MainCourier():
    
    def __init__(self,puttrackid):
        con=cx_Oracle.connect("system/sys@localhost/xe")
        cur=con.cursor()
        print(puttrackid)
        cur.execute("""select * from courier 
                            where ttrackid=:1 """,
                            {"1":puttrackid})
        putlist=cur.fetchall()
        #print(putlist)
        con.close()
        gottuple=putlist[0]
        self.fromcmpphone = gottuple[0]
        self.tocustphone=gottuple[1]
        self.weight=gottuple[2]
        self.shipmenttype=gottuple[3]
        self.trackid=gottuple[4]
        self.status=gottuple[5]
        self.cost=gottuple[6]
        
    def printReceipt(self):
        print("\n\n--------------------------------------------")
        print("------------- Shipping Details -------------")
        print("--------------------------------------------")
        cmpobj=MainDashboard(self.fromcmpphone)
        custobj=MainDashboard(self.tocustphone)
        print("\n\nTrackid : "+self.trackid)
        print("\t\t Shipment type : "+self.shipmenttype)
        print("\t\t Shipment weight : "+str(self.weight))
        print("\t\t Final Amount to be paid : "+str(self.cost))
        print("\nCustomer Details")
        custobj.printDetails()
        print("\nCompany Details")
        cmpobj.printDetails()
        print("\n\n--------------------------------------------")
        print("--------------------------------------------")
        
        path ='.//Company//'+cmpobj.fullname+'//'+cmpobj.city+'To'+custobj.city+'//'+str(custobj.postalcode)+'//'
        # if folder doesn't exists then create new folder
        if not os.path.exists(path):
            os.makedirs(path)  
            
        saveFile = open(path+'Order_'+str(self.trackid)+'.txt','w')
        saveFile.write("\n\n--------------------------------------------")
        saveFile.write("\n------------- Shipping Details -------------")
        saveFile.write("\n--------------------------------------------")
        saveFile.write("\n\nTrackid : "+self.trackid)
        saveFile.write("\n\t\t Shipment type : "+self.shipmenttype)
        saveFile.write("\n\t\t Shipment weight : "+str(self.weight))
        saveFile.write("\n\t\t Final Amount to be paid : "+str(self.cost))
        saveFile.write("\nCustomer Details")
        saveFile.write(" \n\t\t Name      : "+custobj.fullname)
        saveFile.write(" \n\t\t Address   : "+custobj.address)
        saveFile.write(" \n\t\t City      : "+custobj.city)
        saveFile.write(" \n\t\t Pin Code  : "+str(custobj.postalcode))
        saveFile.write(" \n\t\t Email     : "+custobj.email)        
        saveFile.write(" \n\t\t Phone no. : "+str(custobj.phone))
        saveFile.write("\nCompany Details")
        saveFile.write(" \n\t\t Name      : "+cmpobj.fullname)
        saveFile.write(" \n\t\t Address   : "+cmpobj.address)
        saveFile.write(" \n\t\t City      : "+cmpobj.city)
        saveFile.write(" \n\t\t Pin Code  : "+str(cmpobj.postalcode))
        saveFile.write(" \n\t\t Email     : "+cmpobj.email)        
        saveFile.write(" \n\t\t Phone no. : "+str(cmpobj.phone))
        saveFile.write("\n\n--------------------------------------------")
        saveFile.write("\n--------------------------------------------")
        saveFile.close()
        
        
        os.system("notepad.exe "+path+'Order_'+str(self.trackid)+'.txt')
        return 



#obj=MainCourier('101')	
#print("done")
#obj.printReceipt()	