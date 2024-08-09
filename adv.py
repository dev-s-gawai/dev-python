file_name="file.txt" #default value
runner='' #default value
def create():
    global file_name
    file_name=input("enter the file name : ")
    file_name=str(file_name + ".txt")
    object=open(file_name,"w")
    object.close()

def add():
    count=int(input("enter the total number of records : "))
    object=open(file_name,'a')
    print("maximum marks are 100")
    for i in range(count):
            #per_cent=str(str((int(int(english)+int(maths)+int(hindi))/100)) + '%')
            object.write("information of roll_no :" + input("enter the roll no of student : ") + "\n"+"name:"+ input("enter the name of student : ") + "\t"+"class:" + input("enter the class of student : ") + "\n"+"marks:hindi:"+ str(int(input("enter the marks of hindi subject : "))) +"\t"+"marks:engilsh:"+ str(int(input("enter the marks of english subject : "))) +"\t"+"marks:maths:"+ str(int(input("enter the marks of maths subject : "))) +"\n\n")
            print("record entered in file \n\n")
    object.close()

def search():
    roll_search="information of roll_no :"+ str(int(input("enter the roll no for search:"))) +"\n"
    object=open(file_name,'r')
    x=object.readlines(-1)
    y=0
    for i in range(len(x)):
        if roll_search == x[i]:
            print("\n \t yes it is in file")
            print(x[i+1] +"\n"+ x[i+2])
            y=1
            break
    if y==0:
        print("record not found")  
    object.close()

def modify():
    object=open(file_name ,"r")
    x=object.readlines(-1)
    print("maximum marks are 100")
    edit_roll="information of roll_no :"+ str(int(input("enter the roll no which you want to edit :"))) +"\n"
    for i in range(len(x)):
        if edit_roll == x[i]:
            x[i+1]='name:'+ input("enter the name of student : ") +'\tclass:'+ input("enter the class of student : ") + '\n'
            x[i+2]='marks:hindi:'+str(int(input("enter the marks of hindi subject : "))) +'\tmarks:engilsh:'+ str(int(input("enter the marks of english subject : "))) +'\tmarks:maths'+ str(int(input("enter the marks of maths subject : "))) +'\n'
    object_=open(file_name,"w")
    object_.writelines(x)
    object_.close()
    object.close()

def display():
    object=open(file_name ,"r")
    choice=int(input("enter 1 for display all \nenter 2 for display single record \n==> "))
    if choice==1:
        x=object.read()
        print(x)
    elif choice==2:
        roll_dis="information of roll_no :"+ str(int(input("enter the roll no for search:")))+"\n"
        x=object.readlines(-1)
        for i in range(len(x)):
            if roll_dis== x[i]:
                print("\n"+ x[i+1] + "\n" + x[i+2])
    object.close()
while runner !="0":
    runner=input("press \n 1 for create \n 2 for add \n 3 for search \n 4 for modify \n 5 for display \n 0 for exit \n\n ==>")
    if runner=='1':
        create()
    elif runner=='2':
        add()
    elif runner=='3':
        search()
    elif runner=='4':
        modify()
    elif runner=='5':
        display()
    elif runner=='0':
        exit()
    else: pass