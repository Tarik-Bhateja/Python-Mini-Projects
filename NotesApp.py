import datetime
memolist=[]
def getdate_time():
    dt = datetime.datetime.now()
    dt_string1=dt.strftime("Date: %d/%m/%Y  time: %H:%M:%S")
    return dt_string1


def add():
    dt_string1=getdate_time()
    memo=input()
    memo=dt_string1+"\n"+memo
    memolist.append(memo)

# def edit():
#     dt_string1=getdate_time()
#     memo_new=input()
#     memo_new=dt_string1+"\n"+memo_new

def read():
  print("Choose from below:(1-2)") 
  print("1.Read Particular Memo \t2.Read all") 
  y=int(input())
  if(y==1): 
    i=int(input("""Enter Memo Number you want to read (for eg: "1" )"""))
    if(i>len(memolist)):
        print("MEMO NOT FOUND \n")
    else:
        print()
        print(memolist[i-1])
        print()
  elif(y==2):
    for i in memolist:
        print()
        print(i)
        print()
  else:
    print("INCORRECT INPUT \n")

def delete():
  print("Choose from below:(1-2)") 
  print("1.Delete Particular Memo \t2.Delete all") 
  y=int(input())
  if(y==1): 
    i=int(input("""Enter Memo Number you want to read (for eg: "1" )"""))
    if(i>len(memolist)):
        print("MEMO NOT FOUND \n")
    else:
        print(memolist[i-1])
        print()
        print("Do you want to delete it?\n")
        z=int(input("""Press 1 for "Yes" and 2 for "No" """))
        if(z==1):
            del memolist[i-1]
        if(z==2):
            menu()
        else:
         print("INCORRECT INPUT \n")
  elif(y==2):
     print("Do you want to delete all?\n")
     z=int(input("""Press 1 for "Yes" and 2 for "No" """))
     if(z==1):
            memolist.clear()
     elif(z==2):
            menu()
     else:
      print("INCORRECT INPUT \n")  
  else:
    print("INCORRECT INPUT \n")


def menu():
 print("MEMO PROGRAM \n Choose one from below(1-5)") 
 print("1.Add \t2.Edit \t3.Read \t4.Delete \t5.Exit \t")
 x=int(input())
 if(x==1):
    add()
    menu()
 elif(x==2):
    # edit()
    menu()
 elif(x==3):
    read()
    menu()
 elif(x==4):
    delete()
    menu()
 elif(x==5):
    exit()
 else:
    print("INCORRECT INPUT \n")

menu()
