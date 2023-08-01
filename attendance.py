global count
dataBase={
    1:[0,'rohit',7349857398,"rohit@123"],
    2:[0,'kamlesh',5689545980,"kamlesh@123"],
    3:[0,'brijesh',4895945879,"brijesh@123"]
       }
count=len(dataBase)+1

def authenticate(rollno,password):
    if dataBase[rollno][3]==password:
        return rollno
    else:
        return 0
def login():
    userid=int(input("enter the roll no."))
    userpass=input("enter the password")
    return authenticate(userid,userpass)

while True:
    authid=login()
    if authid in dataBase:
        print("WELCOME TO ABC COMPANY MARK YOUR ATTENDANCE")
        if authid==1:
            choice = int(input("For marking attendance press 1 \n For add a user press 2 \n For logout press 3 \n For get your information press 4"))
            if choice==1:
                dataBase[authid][0]=dataBase[authid][0]+1
                print("Attendance marked")
                print("your total attendance is ",dataBase[authid][0])
            elif choice==2:
                dataBase[count]=[0,input("enter the name"),int(input("enter the phonenumber")),input("enter the password")]
                count+=1
            elif choice==3:
                break
            elif choice==4:
                print("Name :",dataBase[authid][1],"\n Attendance :",dataBase[authid][0],"\nPNO.:",dataBase[authid][2])
        elif authid==0:
            
            print("password is wrong try again")
    else :
        print("user id not present")
    
        
   
    