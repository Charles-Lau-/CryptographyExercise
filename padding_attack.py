################################################################################
#attack padding################################################################
import copy

def hex_to_int(hex_str):
    """
         from ffeeaa to int[]

    """
    str_len = len(hex_str)
    intlist = []
    for i in range(0,str_len,2):
        intlist.append(int(hex_str[i]+hex_str[i+1],16))
    return intlist

def int_to_hex(intlist):
    """
        from int[] to hex
    
    """
    hexlist = []
    int_len = len(intlist)
    for i in intlist:
        hexlist.append("%02x" % i)
    return "".join(hexlist)
    
def send_to_server(ciphertext):
    from oracle import Oracle_Connect,Oracle_Send,Oracle_Disconnect	
    
    ctext = [(int(ciphertext[i:i+2],16)) for i in range(0, len(ciphertext), 2)]
     
    Oracle_Connect()
    rc = Oracle_Send(ctext, 3)
    Oracle_Disconnect()	
    return rc


def get_length_of_padding(ciphertext):
    """
       obtain length of the padding part in ciphertext:iv c1, c2,c3,c4..cn, change bit of iv one to one       

    """ 
    intlist = hex_to_int(ciphertext) 
    int_len = len(intlist)

    for i in range(0,int_len/2):
         intlist_copy = copy.copy(intlist)
         intlist_copy[i] = 255 
         response = send_to_server(int_to_hex(intlist_copy))
         if(response==1):
             continue
         else:
             return i

def decrypt_data(data,length):
     """
         decrypt the remain part 

     """  
     intlist = hex_to_int(data)
     intlist.reverse()
     int_length = len(intlist)
     key = []
     
     while(int_length>=length): 
         #set the decrypt of padding be one larger
         for i in range(0,length):
                intlist[i] ^= length^(length+1)
             
         #if after 256 tries, we do not get correct response, it means
         #the padding size is happened to be the block size
         found = False 
         for i in range(0,256):
                list_copy = copy.copy(intlist)
                list_copy[length] = i 
                list_copy.reverse()
                response = send_to_server(int_to_hex(list_copy))
                if(response!=1):
                    continue
                else:
                    print i
                    found = True 
                    key.append(i^(length+1))
                    break
              
         if(not found):
                intlist = intlist[length:]
                int_length = int_length-length  
                length = 0
         else:
                length +=1
     return key
if __name__ =="__main__":
    import sys
    if(len(sys.argv) < 2):
	 print "please enter python <filename>"
	 exit()	  
    f = open(sys.argv[1])
    data = f.read()
    length_of_padding = get_length_of_padding(data) 
    decrypt_data( )

         

