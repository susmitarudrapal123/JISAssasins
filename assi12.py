#qu no-12 by susmita rudra pal
def reverseword(s): 
   
   w = s.split(" ")        
                           
                           
   nw = [i[::-1] for i in w]
                           
   ns = " ".join(nw)
   return ns
# Driver's Code 
s = input("ENTER A SENTENCE PROPERLY ::")
print(reverseword(s))

