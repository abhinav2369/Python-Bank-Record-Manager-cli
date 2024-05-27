#------------------------------------------#
#         BANK  MANAGEMENT  SYSTEM         #
#------------------------------------------#
#             SOURCE  CODE                 #
#------------------------------------------#



#  [ READING ]  FUNCTION

def read():
    import pickle
    file = open('User Database.dat','rb') 
    try:
        while True: 
            d = pickle.load(file) 
            print(d) 
    except: 
            file.close()


# ---------------------------------------------------------------------------------


#  [ WRITING ]  FUNCTION

def write(): 
    import pickle 
    file = open('User Database.dat','wb') 
    data = {} 
    n = int(input("How many User data you want to enter ? ")) 
    for a in range(n): 
        data['Employee No.'] = int(input("Enter Employee Number : ")) 
        data['Name'] = input("Enter Employee Name : ") 
        data['Department'] = input("Enter Department : ") 
        data['Salary'] = int(input("Salary : ")) 
        pickle.dump(data,file)
        print("-"*5)
    file.close() 


# ---------------------------------------------------------------------------------


#  [ APPENDING ]  FUNCTION

def append(): 
    import pickle 
    file = open('User Database.dat','ab') 
    n = int(input("How many user data you want to enter ? ")) 
    data = {} 
    for a in range(n): 
        data['Employee No.'] = int(input("Enter Employee Number : ")) 
        data['Name'] = input("Enter Employee Name : ") 
        data['Department'] = input("Enter Department : ") 
        data['Salary'] = int(input("Salary : ")) 
        pickle.dump(data,file) 
    file.close() 


# ---------------------------------------------------------------------------------


#  [ SEARCHING ]  FUNCTION
 
def search(): 
    import pickle 
    file = open('User Database.dat','rb') 
    found = 0 
    h = int(input("Enter Employee Number : ")) 
    try : 
        while True:
            d = pickle.load(file) 
            if h == d['Employee No.']: 
                print(d) 
                found = found + 1 
    except: 
        if found == 0: 
            print("Sorry,\n No record found with Employee Number : ",h) 
    file.close()


# ---------------------------------------------------------------------------------


#  DATA  [--MODIFY--]  FUNCTION

def modify(): 
    import pickle 
    file = open('User Database.dat','rb+') 
    h = int(input("Enter Employee Number : ")) 
    found = 0 
    L = []
    try:
        while True:
            d = pickle.load(file)
            if h == d['Employee No.']: 
                sal = int(input("Enter new salary : ")) 
                d['Salary']=sal 
                found += 1 
            L.append(d) 
    except:
        if found == 0:
            print("No user to modify ") 
        file.seek(0) 
        file.truncate(0) 
        for a in L: 
            pickle.dump(a,file) 
        file.close()


# ---------------------------------------------------------------------------------

#  [--DELETE--]  FUNCTION 

def delete():
    import pickle 
    file = open('User Database.dat','rb+') 
    L = [] 
    m = int(input("Enter Employee Number to be deleted : ")) 
    try: 
        while True:
            d = pickle.load(file) 
            if m != d['Employee No.']:
                L.append(d) 
    except : 
        file.seek(0) 
        file.truncate(0) 
    for a in L: 
        pickle.dump(a,file) 
    file.close() 


# ---------------------------------------------------------------------------------


#  CALLING  STATEMENTS

while True: 
    print('-'*50) # symbols used for separating 
    print("1-Create\n2-Display\n3-Search\n4-Modify\n5-Delete\n6-Append\n7-Exit") 
    ch = int(input("Enter your Choice ")) 
    print('-'*70) # symbols used for separating 
    if ch==1: 
        write() 
    elif ch==2: 
        read() 
    elif ch==3: 
        search() 
    elif ch==4: 
        modify() 
    elif ch==5: 
        delete() 
    elif ch==6: 
        append() 
    elif ch==7: 
        break 
    else: 
        print("Invalid Choice") 
