# -*- coding: utf-8 -*-
"""
Created on Thu May 28 10:14:33 2020

@author: johan
"""

# Python Project Using CSV File Handling

print('\t\t\t LIBRARY MANAGEMENT SYSTEM')
print('\t\t\t *-*-*-*-*-*-*-*-*-*-*-*-*')

# book_id, book_name, qty, price_4_one, total_price, supplier_code,
# supplier_mail_id

import csv


#add records
def addRecords():  #if same book name and supplier just increase quantity
    L=[]
    with open("lms.csv",'a',newline='') as csvfile:
        while True:
            book_id = input("Book ID: ") #index-0
            book_name = input("Book Name: ")   #index-1
            qty = int(input("Quantity: "))   #index-2
            price_4_one = int(input("Price for one: "))   #index-3
            total_price = qty * price_4_one        #index-4
            supplier_code = input("Supplier Code: ")   #index-5
            supplier_mail_id = input("Suplier Mail ID: ")   #index-6
            L.append([book_id, book_name, qty, price_4_one, total_price, supplier_code,supplier_mail_id])
            condition = input(("\nDo you want to add more records? (Y/N) "))
            condition=condition.upper()
            if condition != 'Y':
                break
        csvobj=csv.writer(csvfile)
        csvobj.writerows(L)
        csvfile.flush()
        print("Record(s) added successfully! ")
    
        
#display records
def displayRecords():
    csvfile=open('lms.csv','r',newline='')
    csvobj=csv.reader(csvfile)
    for line in csvobj:
        print('\n')
        for data in line:
            print(data,"\t",end='')
    csvfile.close()

#search records with supplier code
def search():
    control=0
    with open('lms.csv','r',newline='') as csvfile:
        csvobj=csv.reader(csvfile)
        while True:
            supplier_code = input("Enter Supplier code: ")
            for line in csvobj:
                if line[5] == supplier_code:
                    control+=1
                    for data in line:
                        print(data,'\t',end='')
            if control==0:
                print("No record with supplier code {} found".format(supplier_code))
            condition = input(("\nDo you want to search again? (Y/N) "))
            condition=condition.upper()
            if condition != 'Y':
                break
            

#delete record with book name
def delete():
    new_data = []
    with open('lms.csv','r',newline='') as csvfile1:
        csvobj1 = csv.reader(csvfile1)
        book_name = input("Enter name of book to delete: ")
        control=0
        for line in csvobj1:
            if line[1] == book_name:
                control+=1
                check=input("Are you sure you want to delete this record {} ? (Y/N) ".format(line))
                if check.upper() != 'Y':
                    new_data.append(line)
                else:
                    print("deleted successfully")
            else:
                new_data.append(line)
        if control==0:
            print("Record not found! ")
    with open('lms.csv','w',newline='') as csvfile2:
        csvobj2 = csv.writer(csvfile2)
        csvobj2.writerows(new_data)
        csvfile2.flush()
            
#edit records with book name
def edit():
    L=[]
    with open('lms.csv','r',newline='') as csvfile:
        csvobj=csv.reader(csvfile)
        for row in csvobj:
            L.append(row)
    while True:
        control=0
        name_edit=input("Enter Book Name to edit: ")
        for index in range(len(L)):
            if L[index][1]==name_edit:
                control+=1
                for data in L[index]:
                    print(data,'\t',end='')
            
                print("\n\nDo you want to edit: \n")
                print("1: Quantity")
                print("2: Price for one book")
                choice=int(input("\n Enter choice: "))
                def editQty():
                    new_qty=int(input("Enter new quantity: "))
                    L[index][2]=new_qty
                    L[index][4]=new_qty*int(L[index][3])
                def editPrice():
                    new_price=int(input("Enter new price: "))
                    L[index][3]=new_price
                    L[index][4]=int(L[index][2])*new_price
                if choice==1:
                    editQty()
                elif choice==2:
                    editPrice()
                else:
                    print("invalid input")
        
        if control==0:
            print("Record not found! ")
        condition = input(("\nDo you want to edit again? (Y/N) "))
        condition=condition.upper()
        if condition != 'Y':
            break
    with open('lms.csv','w',newline='') as f:
        csvobj1=csv.writer(f)
        csvobj1.writerows(L)
        f.flush()
        f.close()
    print("Record(s) successfully edited")
        

#sort all records
def sortRecords():
    L=[]

    with open('lms.csv','r',newline='') as csvfile:
        csvobj=csv.reader(csvfile)
        for line in csvobj:
            L.append(line)
    if len(L)>1:
        for index1 in range(len(L)):
            for index2 in range(0,len(L)-1-index1):
                if L[index2][1] > L[index2+1][1]:
                    L[index2] , L[index2+1] = L[index2+1] , L[index2]
        with open('lms.csv','w',newline='') as f:
            fobj=csv.writer(f)
            fobj.writerows(L)
            f.flush()
        print("Records succesfully sorted: ")
        displayRecords()
    
    else:
        print("Only 1 record present!!")
        
#main starts here        
 
while True:

    print('\n\n \t MENU :')
    print('1: Add records')
    print('2: Display Records')
    print('3: Search records with supplier code')
    print('4: Delete record with book name')
    print('5: Edit details with book name')
    print('6: Sort records with book name')
    print("O: Exit")


    choice=int(input('\n Enter your choice: '))
    if choice==1:
        addRecords()
    elif choice==2:
        displayRecords()
    elif choice==3:
        search()
    elif choice==4:
        delete()
    elif choice==5:
        edit()
    elif choice==6:
        sortRecords()
    elif choice==0:
        print("Thank you...")
        break
    else:
        print("Invalid input! Please Try again......")
    
input("Press any key to exit")
