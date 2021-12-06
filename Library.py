import datetime
import os
import random

stack = []
def bubbleSort(arr):
    n = len(arr)
  
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
            arr[j + 1] = key
            
    #3rd Concept
def linearsearch(arr, x):
    for i in range(len(arr)):
        if str(arr[i]) == str(x):
            return i
        else:
            return -1
    

def binary_search(arr, low, high, x):
     
        # Check base case
        if high >= low:
     
            mid = (high + low) // 2
     
            # If element is present at the middle itself
            if int(arr[mid]) == int(x):
                return arr[mid]
     
            # If element is smaller than mid, then it can only
            # be present in left subarray
            elif int(arr[mid]) > int(x):
                return binary_search(arr, low, mid - 1, x)
     
            # Else the element can only be present in right subarray
            else:
                return binary_search(arr, mid + 1, high, x)
     
        else:
            # Element is not present in the array
            return -1
            
class Node:
    def __init__(self, particular, qty, unitprice):
        self.particular = particular
        self.qty = qty
        self.unitprice = unitprice
        self.amount = int(self.qty) * int(self.unitprice)
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.Name = None
        self.company = None
        self.date = None
        self.contact = None
        self.totalbill = 0
        self.start = None
    def insert(self, particular, qty, unitprice):
        if (self.start is None):
            self.start = Node(particular,qty,unitprice)
        else:
            ptr = self.start
            while (ptr.next != None):
                ptr = ptr.next
            ptr.next = Node(particular, qty, unitprice)
    def Billing(self):
        self.date = datetime.date.today()
        check = True
        while (check):
            x = str(input('\tEnter Book ID: '))
            qty = str(input('\tEnter Quantity: '))
            for line in open("books.txt", "r").readlines():   
                data=line.split(',')
                if(data[0]== x):
                    particular= data[1]
                    unitprice = data[2]
                      
            self.insert(particular, qty, unitprice)
            self.totalbill += int(qty) * int(unitprice)
            inpt = input("Press Enter to continue to add items or type NO to exit: ")
            if (inpt == "No" or inpt == "no" or inpt == "NO"):
                check = False
    def Print(self):
        self.billno= random.randint(0,5)
        print("\n══════════════════════════════════════════════════════════════════════")
        print("Bill:    " + str(self.billno) + "\t\t\t\t\t""Date:    " + str(self.date))
        print("══════════════════════════════════════════════════════════════════════")
        print("S/no\tName \t\t Qty \t\t Rate  \t\t Amount\n")
        ptr = self.start
        i = 1
        while(ptr != None):
            print(str(i) + "\t "+ ptr.particular + "\t "+ ptr.qty + "\t\t " + ptr.unitprice + "\t\t "+str(ptr.amount))
            ptr = ptr.next
            i += 1
        print("══════════════════════════════════════════════════════════════════════")
        print("\n\t\t\t\t\t\t\t\t\t\t" + "Total: " + str(self.totalbill))
        
class Book:
    books = []
    def __init__(self,bokid,bookname,price,quantity):
        self.bookid=bokid
        self.bookname=bookname
        self.price=price
        self.quantity=quantity
    
    def Purchase_book(self):
        Bill = DoublyLinkedList()
        Bill.Billing()
        Bill.Print()
        
    
    def Book_details(self):
            file= "books.txt"
            if os.path.exists(file):
                for line in open(file, "r").readlines():
                    data = line.split(',')
                    self.books.append((data[0]))
        
        
    def File_Deletion(self,file,file2):
         with open(file,"r") as f:
            with open(file2, "w+") as f1:
                for line in f:
                    f1.write(line)
                f.close()
                f1.close()
         if os.path.exists(file):
             os.remove(file)
         else:
            print("The file does not exist")
    
    
    def DisplayAllbook(self):
        self.books= []
        self.Book_details()
        order = int(input("\t1. Ascending Order\n\t2. Descending Order: "))
        if(order == 1):
            bubbleSort(self.books)
            if(os.path.exists("books.txt")):
                for i in range(len(self.books)):
                    
                    for line in open("books.txt", "r").readlines():   
                        data=line.split(',')
                        if(self.books[i] == data[0]):
                            
                            print(str("\n\tbook #")+ str(i+1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))    
            else:
                print("\tNo books in Our Library")
        elif(order == 2):
            bubbleSort(self.books)
            if(os.path.exists("books.txt")):
                for i in range(len(self.books)):
                    #Stack for Descending Sort
                    x = self.books.pop()
                    for line in open("books.txt", "r").readlines():   
                        data=line.split(',')
                        if(x == data[0]):
                            
                            print(str("\n\tbook #")+ str(i+1))
                            print("\tID: \t" + str(data[0]))
                            print("\tName: \t" + str(data[1]))
                            print("\tPrice: \t" + str(data[2]))
                            print("\tQuantity: \t" + str(data[3]))    
            else:
                print("\tNo books in Our Libaray")
            
            
        str(input("\tPress Any Key"))     
        
    def Search_book(self):
        var = True
        for line in open("books.txt","r").readlines():
            data = line.split(',')     
            
            #Linear Search
            if(self.bookid==data[0]):
                
                print("\tID: " + str(data[0]))
                print("\tName: " + str(data[1]))
                print("\tPrice: " + str(data[2]))
                print("\tQuantity: " + str(data[3]))
                str(input("\tPress Any Key To Go Back To The main menu\n\n"))
                
                var = True
            else:
                var = False
        if(var == False):
            print("\tNo Book Found")
     
    def Is_book_alreadytaken(self):
        self.books =[]
        self.Book_details()
        if(binary_search(self.books,0,len(self.books)-1,self.bookid)== -1):
            return False
        else:
            return True
            
    def Addbook(self):
        if(self.Is_book_alreadytaken()==False):
            if(int(self.quantity)>0):
                f = open("books.txt","a+")
                f.write(str(self.bookid) + "," 
                        + str(self.bookname)+ "," 
                        + str(self.price) +"," 
                        + str(self.quantity) +"," 
                        + "\n")
                print('\n\tBook Successfully Added')
                str(input('\n\tPress Any Key'))
            else:
                print("\tPlease enter Quantity greater thn zero")
        else:
            print("\tBook ID is Already Taken")
            str(input("\tPress any Key To Continue"))
        
        
    
    def Editbook(self):
        file= "books.txt"
        file2= "tempbooks.txt"
        x = open(file2,"w")
        for line in open(file,"r").readlines():
            data = line.split(',')
            print()
            print()
            if(str(self.bookid)==str(data[0])):
                x.write(str(input('\tEnter New ID: '))+ "," 
                         + str(input('\tEnter New Name: ')) +","
                         + str(input('\tEnter New Price: '))+ ","
                         + str(input('\tEnter Your New Quantity: '))
                         + ",\n")        
            else:
                x.write(str(data[0]) + "," + 
                         str(data[1])+ "," + 
                         str(data[2]) +"," + 
                         str(data[3])+ ",\n" )
                         
        x.close()
        str(input("\n\tSuccessfully Edited\n\tPress Any Key To Go Back To The main menu\n\n"))
        self.File_Deletion(file2,file)
        
    def Deletebook(self):
        file= "books.txt"
        file2= "tempbooks.txt"
        f = open(file,"r")
        f2 = open(file2,"w")
        for line in f.readlines():
            data = line.split(',')
            #Linear Search
            if(str(self.bookid)==str(data[0])):  
                continue
            else:   
                f2.write(
                    str(data[0]) + "," + 
                    str(data[1])+ "," + 
                    str(data[2]) +"," + 
                    str(data[3]) +",\n" )
                
        f.close()
        f2.close()
        str(input("\n\tSuccessfully Deleted\n\tPress Any Key To Go Back To The main menu\n\n"))
        self.File_Deletion(file2,file)
    
    def DeleteAllbooks(self):
        confirmation = str(input("Are You Sure You Want To Delete All Books Y/N: "))
        if (os.path.exists("books.txt")) and (confirmation =='Y'):
            os.remove("books.txt")
        
class Admin:
    
    users= []
    
    def __init__(self,name,email,password):
        
        self.name=name.lower()
        self.email=email
        self.password = password
        
        
    def getuserids(self):
        
        file= "Admins.txt"
        if os.path.exists(file):
            for line in open(file, "r").readlines():
                data = line.split(',')
                self.users.append(data[1])
        
        
    def Register(self):
        if(True):
            f = open("Admins.txt","a+")
            f.write(str(self.name) 
                        + "," + str(self.email)+ "," 
                        + str(self.password)
                        + ",\n")
            print("\tSuccessFully Registered")
        else:
            print("\tEmail already Taken")
        str(input("Press any Key To Move Further"))
        
        
    def Login(self):
        
        x=''
        if(os.path.exists("Admins.txt")):
            for line in open("Admins.txt", "r").readlines():
                data = line.split(',')
                if(self.email==data[1] and self.password == data[2]):
                    self.name = data[0]
                    self.email =data[1]
                    self.password= data[2]
                    self.WelcomeAdmin()
                else:
                    x = 'notfound'
                    
            if(x=='notfound'):
                print("\tInvalid Email or Password")
        else:
            print("\n\tNo User Registered")
            
            
    def WelcomeAdmin(self):
        while(True):
            print('\t\t\t»»————————————————————-———————————————————————-««')
            print("\t\t\t           WELCOME TO LIBRARY "+ self.name.upper())
            print('\t\t\t»»————————————————————-———————————————————————-««')
            
            print ("\n\tA. Add Book \n\tB. Edit Book \n\tC. Search Book \n\tD. Delete Book \n\tE. Purchase Book \n\tF. Delete All Book\n\tG. Display All Books \n\tH. Log Out")
            print()
            select=input("\tEnter Your Selection: ")
            
                
            
            if select=='A':
                
                book=Book(input("\tEnter Book ID: "),
                 input("\tEnter Book Name: "),
                 input("\tEnter Book Price: "),
                 input("\tEnter Book Quantity: "),
                    )
                book.Addbook()
                
            elif select=='B':
                books = Book(input("\tEnter Book ID: "),'none','none','none')
                books.Editbook()
                
            elif select=='C':
                books = Book(input("\tEnter Book ID: "),'none','none','none')
                books.Search_book()
                
            
            elif select=='D':
                books = Book(input("\tEnter Book ID: "),'none','none','none')
                books.Deletebook()
            
            elif select=='E':
                books = Book('none','none','none','none')
                books.Purchase_book()

            elif select=='F':
                books = Book('none','none','none','none')
                books.DeleteAllbooks()
            elif select=='G':
                books = Book('none','none','none','none')
                books.DisplayAllbook()
                
            elif select=='H':
                break
            
            else:
                print("\tWrong Input")
                


def start():
    
    while(True):
        print('\t╔═══════════════════════════════════════════════════╗')
        print("\t        WELCOME TO LIBRARY MANAGEMENT SYSTEM         ")
        print('\t╚═══════════════════════════════════════════════════╝')
        
       
        print ("\t1. Login  \n\t2. Register \n\t3. Exit")
        print()
        select=input("Enter Your Selection (1-3): ")
        if select=='1':

            admin= Admin('none',input("\tEnter Your Email: "),input("\tEnter Your Password: "),)
            admin.Login()
       
        elif select=='2':
            
            admin= Admin(
                input("\tEnter Your Name: "),input("\tEnter Your Email: "), input("\tEnter Your Password: "))
            admin.Register()
            
        elif select=='3':
            
            break
        
        else:
            print('Wrong Input')
                 

start()