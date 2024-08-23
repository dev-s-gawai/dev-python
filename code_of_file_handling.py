object=open("file.txt")         #opening file
main =list(object.read())       #creating list of existing data
vol="aAeEiIoOuU"                #all vowels in string form
todo=str()                      #empty string use to write ...
for i in range (len(main)):     #for replacing vowels by "#" 
    if main[i] in list(vol):    #if value is any value from vol
        main[i]="#"             #so replace it with "#"
for j in range(len(main)):      #to convert list to string
    todo=todo + main[j]
obj=open("file.txt","w")        #to overwrite file to main
obj.write(todo)
obj.close()                     #closeing objects
object.close()                  #end program