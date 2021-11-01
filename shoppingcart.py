#shopping cart
#praveenkumar
#19-10-21
#modified:24-10-21
def admin():
        ba=input("enter admin name:")
        ac=input("enter password:")
        c=a1.index(ba)
        d=b1.index(ac)
        if ba in a1 or ba not in a1:
                if ac in b1 and d == c:
                        selection()
                elif ba == '' or ac == '':
                        print("*Field Required")
                        admin()
                else:
                        print("Enter valid user name or password!!")
                        admin()
def selection():
        print("add item\ndelete item\nupdate item\nadd admin\ndelete admin")
        option=input("what do you want:")
        if option == "add item":
                additem()
        elif option == "delete item":
                delitem()
        elif option == "update item":
                updateitem()
        elif option == "add admin":
                addadmin()
        elif option == "delete admin":
                deladmin()
        elif option == '':
                print("*Field Required")
                selection()
        else:
                print("Enter valid selection")
                return



def customer():
        
        items1=[]

        for x in grocessaryitems:
                print(x)

        
        items=int(input("how many items you want:"))
        if items != '':
                for i in range(items):
                        answer=input("enter item you want:")
                        if answer != '':
                                if answer in grocessaryitems:
                                        items1.append(answer)
                                        a=int(grocessaryitems[answer])
                                        print("stock\t" +str(a))
                                        b=int(input("how many "+answer+" you want:"))
                                        if b !='':
                                                if b <= a:
                                                        e=grocessaryitemsprices[answer]
                                                        c=b * e
                                                        print(str(c)+"$")
                                                        prices[0]=prices[0]+c
                                                        c1=a-b
                                                        grocessaryitems[answer]=c1
                                                        print("available stock"+answer+str(c1))
                                                        purchaselist[answer]=b
                        
                        
                                                else:
                                                        print("item out of stock!!!")
                                                        print("available stock:"+str(a))
                                                        ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                                        if ce == 'c' or ce == 'C':
                                                                customer()
                                                        elif ce == 'b' or ce == 'B':
                                                                selection()
                                                        elif ce == 'e' or ce == 'E':
                                                                print("Thank you visit again!!!")
                                                                login()
                                        else:
                                                print("*Field Required")
                                                customer()
                                else:
                                        print("item doesn't exist:")
                                        ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                        if ce == 'c' or ce == 'C':
                                                customer()
                                        elif ce == 'b' or ce == 'B':
                                                selection()
                                        elif ce == 'e' or ce == 'E':
                                                print("Thank you visit again!!!")
                                                login()
                        else:
                                print("*Field Required")
                                customer()

                ce=input("Enter 'c' to continue or 'e' to exit:")
                if ce == 'c' or ce == 'C':
                        customer()
                elif ce == 'b' or ce == 'B':
                        selection()
                elif ce == 'e' or ce == 'E':
                        g=prices[0]
                        for x,y in purchaselist.items():
                                print(str(x)+"   "+str(y))
                        print("Total amount:"+str(g)+"Rs.")
                        for x,y in purchaselist.items():
                                print(str(x)+"   "+str(y))
                        ca=input("If you want to return any item(y/n):")
                        if ca == 'y':
                                dele=int(input("How many items you want to delete:"))
                                for i in range(dele):
                                        item=input("Enter the item:")
                                        qty1=int(input("Enter how many"+item+"you want to return:"))
                                        if item in items1:
                                                del purchaselist[item]
                                                s=int(grocessaryitemsprices[item])
                                                y=s*qty1
                                                ab=g-y
                                                print("item "+item+"deleted successfully!!!")
                                                ce=input("Enter 'c' to continue or 'e' to exit:")
                                                if ce == 'c' or ce == 'C':
                                                        customer()
                                                elif ce == 'b' or ce == 'B':
                                                        selection()
                                                elif ce == 'e' or ce == 'E':
                                                        print("Total amount:"+str(ab)+"Rs.")
                                                        print("Thank You Visit Again!!!!!")
                                                        login()
                                        
                                
        else:
                print("*Field Required")
                customer()
                    

      
                
              






def additem():
        add=int(input("how many items you want to add:"))
        if add != '':
                for i in range(add):


                        for x in grocessaryitems:
                                print(x)



                        itemname=input("enter item name:")
                        a=grocessoryitems.index(itemname)
                        itemqty=input("enter item qty:")
                        itemprice=input("enter item price:")
                        if itemname in grocessaryitems:
                                print("Item already exists!!!")
                                ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                if ce == 'c' or ce == 'C':
                                        additem()
                                elif ce == 'b' or ce == 'B':
                                        selection()
                                elif ce == 'e' or ce == 'E':
                                        login()
                        
                        else:
                                grocessaryitems[itemname]=itemqty
                                grocessaryitemsprices[itemname]=itemprice
                        
                                for x in grocessaryitems:
                                        print(x)

                                ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                if ce == 'c' or ce == 'C':
                                        additem()
                                elif ce == 'b' or ce == 'B':
                                        selection()
                                elif ce == 'e' or ce == 'E':
                                        login()
                else:
                        print("*Field Required")
                        additem()

def delitem():
         delete=int(input("how many items you want to delete:"))
         if delete != '':
                 for i in range(delete):
                         itemname=input("enter item name:")
                         if itemname in grocessaryitems:
                                 del grocessaryitems[itemname]
                                 del grocessaryitemsprices[itemname]

                    
                                 for x in grocessaryitems:
                                         print(x)

                                 ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                 if ce == 'c' or ce == 'C':
                                         delitem()
                                 elif ce == 'b' or ce == 'B':
                                         selection()
                                 elif ce == 'e' or ce == 'E':
                                         login()
                         else:
                                 print("Item doesnot exist!!!")
                                 ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                 if ce == 'c' or ce == 'C':
                                         delitem()
                                 elif ce == 'b' or ce == 'B':
                                         selection()
                                 elif ce == 'e' or ce == 'E':
                                         login()
         else:
                 
                print("*Field Required")
                delitem()

def updtateitem():
        update=int(input("how many items you want to changestock:"))
        if update != '':
                for i in range(update):
                        itemname=input("enter item name:")
                        if itemname in grocessaryitems:
                                sp=input("stock or prize or both:")
                                if sp == 'stock':
                                        cstock=input("enter stock:")
                                        grocessaryitems[itemname]=cstock
                                elif sp == 'prize':
                                        cprize=input("enter prize")
                                        grocessaryitems[itemname]=cprize
                                elif sp == 'both':
                                        cstock=input("enter stock:")
                                        cprize=input("enter prize")
                                        grocessaryitems[itemname]=cstock
                                        grocessaryitems[itemname]=cprize

                                for x,y in grocessaryitems.items():
                                        print(x,y)


                                for x,y in grocessaryitemsprices.items():
                                        print(x,y)
                                                        
                                ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                if ce == 'c' or ce == 'C':
                                        updateitem()
                                elif ce == 'b' or ce == 'B':
                                        selection()
                                elif ce == 'e' or ce == 'E':
                                        login()
                        else:
                                print("Item doesn't exist!!!")
                                ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                                if ce == 'c' or ce == 'C':
                                        updateitem()
                                elif ce == 'b' or ce == 'B':
                                        selection()
                                elif ce == 'e' or ce == 'E':
                                        login()
        else:
                print("*Field Required")
                updateitem()


                        
def addadmin():
         aname=input("enter new admin name:")
         pwd=input("enter new admin password:")
         if aname != '' or pwd != '':
                 if aname in a1:
                         print("admin name already exists!!!")
                         ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                         if ce == 'c' or ce == 'C':
                                 addadmin()
                         elif ce == 'b' or ce == 'B':
                                 selection()
                         elif ce == 'e' or ce == 'E':
                                 login()
                 else:
                         a1.append(aname)
                         b1.append(pwd)
                
                         for x in a1:
                                 print(a1)
                    
                         ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                         if ce == 'c' or ce == 'C':
                                 additem()
                         elif ce == 'b' or ce == 'B':
                                 selection()
                         elif ce == 'e' or ce == 'E':
                                 login()
         else:
                print("*Field Required")
                addadmin()
def deladmin():
        aname=input("enter admin name for delete:")
        if aname != '':
                if aname in a1:
                        delete1=a1.index(aname)
                        a1.remove(aname)
                        del b1[delete1]
                        

                        for x in a1:
                                print(x)
                                

                        ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                        if ce == 'c' or ce == 'C':
                                deladmin()
                        elif ce == 'b' or ce == 'B':
                                selection()
                        elif ce == 'e' or ce == 'E':
                                login()
                else:
                        print("Admin name doesn't exist!!!")
                        ce=input("Enter 'c' to continue or 'b' to back or 'e' to exit:")
                        if ce == 'c' or ce == 'C':
                                additem()
                        elif ce == 'b' or ce == 'B':
                                selection()
                        elif ce == 'e' or ce == 'E':
                                login()
        else:
                print("*Field Required")
                deladmin()
                


print("\t\t\t****Welcome to e-shopping mart****\t\t\t")


grocessaryitems={
    "pen" : 50,
    "pencil" : 100,
    "stick pen" : 60,
    "eraser" : 30,
    "notebook" : 50,
    "stapler" : 20,
    "A4 sheets" : 120
    }
grocessaryitemsprices={
    "pen" : 10,
    "pencil" : 5,
    "stick pen" : 20,
    "eraser" : 3,
    "notebook" : 50,
    "stapler" : 20,
    "A4 sheets" : 2
    }

purchaselist={
        }
        
a1=["praveen","ponnarasu","malini"]
b1=['pk123','ponnu','mali123']
prices=[0]



    
def login():
        ab=input("admin or customer:")
        if ab =="admin" :
                admin()
        elif ab == "customer":
                customer()
        elif ab == '':
                print("*Field Required")
                login()
        else: print("Enter correct selection!!!")
        login()
login()

                
