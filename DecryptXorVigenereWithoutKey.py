#this program aimed at decrypting a Xor vigenere ciphertext
#basic idea is to find the length of the key first and then
#recover the key
import math

def decrypt(ciphertext):
        key_length = find_key_length(ciphertext)
        plaintext = recover_key(key_length,ciphertext)
        return plaintext
        
#select every i-th letter in ciphertext, and calculate /sigma 0,255{qi*qi}
#let the key length be n so that the n-th sum will be the largest one.
def find_key_length(ciphertext):
        ciphertext_length = len(ciphertext)
        frequency_sum= [0 for i in range(0,int(math.sqrt(ciphertext_length)))]
        for i in range(0,int(math.sqrt(ciphertext_length))):
            letter_occurrence = [0 for p in range(0,256)] 
            counter=0.0
            for  j in range(i,ciphertext_length,i+1):
                letter_occurrence[ciphertext[j]] += 1
                counter +=1.0
            for l in letter_occurrence:
                frequency_sum[i] += pow(l/counter,2)
    
        return frequency_sum.index(max(frequency_sum))+1               

#select  i-th position character (0<i<length) of every block, and let k 0~255,
#select k with largest sum of square frequency
def recover_key(key_length,ciphertext):
        decryption = []
        for i in range(0,key_length):
            part_decryption = []
            part_ciphertext = []
            #put each j-th character in the list
            for j in range(i,len(ciphertext),key_length):
                part_ciphertext.append(ciphertext[j])
            #choose legal k
            for k in range(0,256): 
                for c in part_ciphertext:
                    xor = k ^ c
                    #if legal, then store according plain character
                    if(xor >= ord('A') and xor <= ord('Z') ):
                        part_decryption.append(chr(xor))
                    elif(xor >= ord('a') and xor <= ord('z')):
                        part_decryption.append(chr(xor))
                    elif(xor == ord(',') or xor==ord(' ') or xor==ord('.')):
                        part_decryption.append(chr(xor))
                    else: 
                        part_decryption = []
                        break
                if(part_decryption==[]):
                    continue
                else:
                    break
          
            decryption.append(part_decryption)

        #get the plaintext
        plaintext = []
        for i in range(0,len(decryption[-1])):
            for j in decryption:
                plaintext.append(j[i])
        return plaintext

#test example
if __name__ == "__main__":
    ciphertext_hex_prime  = """F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF
                     1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032
                     BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB
                     27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFC
                     D33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3F
                     E2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF
                     67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794"""
    ciphertext_hex = []
    
    ciphertext = []
    
    for c in ciphertext_hex_prime:
        if(c!=' ' and c!='\n'):
            ciphertext_hex.append(c)
     
    for i in range(0,len(ciphertext_hex),2): 
        ciphertext.append(int(ciphertext_hex[i]+ciphertext_hex[i+1],16))

     
    print "".join(decrypt(ciphertext))   
