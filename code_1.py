#creating list for encriotion and decripyion
main_chr=['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',' ',"\n"]
endcod_chr=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '`', '~', '{', '}', '[', ']', '|', ';', ':', "'", '<', ',', '.', '>', '/', '?', '0', 'devesh', 'gawai', '0101', '10101', 'dev-s-gawai', 'computer_science', 'Z']

#encription
def encoded_code(): #for encoding
    object=open("file.txt")#taking info from file
    readed=object.read()
    readed=list(readed)#creating list of information
    object.close()
    encoded=str()#creating string for storing value and writing it
    for i in range(len(readed)): #for storing encriptedvalues in string
        if readed[i] in main_chr:
            encoded=encoded+" "+ endcod_chr[main_chr.index(readed[i])]
        else:encoded=encoded+" "+ endcod_chr[main_chr.index(readed[i])]
    object=open("encode.txt","w")
    object.write(encoded)# writing encripted value in another file
    object.close()
    print(encoded)# for final test in shell

#decription
def decoded_code(): #for decoding
    object=open("encode.txt")#taking info from file
    readed=object.read()
    readed=readed.split()#creating list of information on the bases of spaces
    object.close()
    decoded=str()#creating string for storing value and writing it
    for i in range(len(readed)): #for storing encriptedvalues in string
        if readed[i]!=" ":
            decoded=decoded + main_chr[endcod_chr.index(readed[i])]
        else:decoded=decoded+ main_chr[endcod_chr.index(readed[i])]
    object=open("decode.txt","w")
    object.write(decoded)# writing encripted value in another file
    object.close()
    print(decoded)# for final test in shell


#calling function
encoded_code()
decoded_code()