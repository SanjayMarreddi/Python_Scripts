"""
This File contains Code that converts the given 8 bit ASCII (in Hexagonal Notation) to string Format and then performs Rotation of Characters.
Author : Sanjay Marreddi
Date  : 14th September ,2020.

"""

given_str = "0a4c626820706e612078727263206c626865206f626a79726566206f796e70782c0a4c6268652067626320756e6766206679727278206e617120676e79792c0a5362652056277a20677572205562746a6e656766204662656776617420556e670a4e6171205620706e6120706e63206775727a206e79792e0a0a47757265722766206162677576617420757671717261207661206c6268652075726e710a477572204662656776617420556e6720706e612767206672722c0a46622067656c207a72206261206e61712056206a7679792067727979206c62680a4a75726572206c6268206268747567206762206f722e0a0a4c6268207a76747567206f72796261742076612054656c737376617162652c0a4a7572657220716a72797920677572206f656e6972206e672075726e65672c0a477572766520716e657661742c2061726569722c206e617120707576696e79656c0a4672672054656c7373766171626566206e636e65673b0a0a4c6268207a76747567206f727962617420766120556873737972636873732c0a4a75726572206775726c206e65722077686667206e61712079626c6e792c0a477562667220636e6776726167205568737379726368737366206e657220676568720a4e61712068616e73656e767120627320676276793b0a0a4265206c7267207661206a7666722062797120456e69726170796e6a2c0a7673206c6268276972206e2065726e716c207a7661712c0a4a75726572206775626672206273206a7667206e61712079726e65617661742c0a4a767979206e796a6e6c66207376617120677572766520787661713b0a0a426520637265756e63662076612046796c6775726576610a4c6268277979207a6e7872206c6268652065726e7920736576726171662c0a4775626672207068616176617420736279786620686672206e616c207a726e61660a4762206e70757672697220677572766520726171662e0a0a466220636867207a7220626121205162612767206f72206e73656e7671210a4e617120716261276720747267207661206e2073796e63210a4c626827657220766120666e737220756e6171662028677562687475205620756e69722061626172290a5362652056277a206e20477576617876617420506e63210a" 


# Converts the 8 bit ASCII(Hexagonal) string to ASCII format string 
def hexToASCII(Hex): 
  
    # Initializing the ASCII code string as empty. 
    ascii = "" 
  
    for j in range(0, len(Hex), 2): 
  
        # Extract two characters from hex string 
        part = Hex[j : j + 2] 
  
        # Change it into base 16 and typecasting as the character  
        char = chr(int(part, 16)) 
  
    
        ascii += char 
      
    return ascii 
  

# Computing for given String
result = hexToASCII(given_str )

# Storing the ascii Values 
ascii_values = [ord(i) for i in result]

# Defining list of Ascii Values of Alphabets.
small = list(range(97,123))
capital = list (range(65,91))
total = small + capital


"""
Rotates the characters by given n.A rotation by 1 means an "A" becomes a "B", a "B" becomes a "C" and "Z" becomes an "A". Similarly, a rotation by 2 means "A" becomes "C", and so on.

Input : Int
Output : List
"""
def  rotate(n):
    tem=[]
    for i in ascii_values:
        if i in total :
            if 97<=i<= 122:
                if (i+n) >122:
                    tem.append( ((96+ n)-(122- i))  ) 
                else: 
                    tem.append(i+n)

            if 65 <= i <= 90:
                if (i+n) >90 :
                    tem.append( ((65+ n)-(90- i))-1    ) 
                else: 
                    tem.append(i+n)

        else:
            tem.append(i)
    return tem


# Attempting to find the value of N
for N in range(0,27):
    
    # Joing the list of strings
    res = ''.join(chr(val) for val in rotate(N)) 

    # Lets print only 50 characters to find the Value of N
    print ("The string for N = ", N ,"is \n", str(res)[:50]) 
    print("\n")


# From above Observation N=13 seems to be Correct

# So, Lets try using N = 13 for entire String
final = rotate(13)

res = ''.join(chr(val) for val in final) 
print("-"*100)
print("The correct value of N is 13") 
print ("Finally the text from the book is :- \n\n", str(res)) 
print("-"*100)


  
