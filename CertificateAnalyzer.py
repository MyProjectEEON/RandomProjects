# Import required module
import re
  
  
# Function to depict use of finditer() method
def CntSubstr(pattern, string):
  
    # Array storing the indices
    a = [m.start() for m in re.finditer(pattern, string)]
    return a

def match(a, b):
    a=a.replace("$","a")
    a=b.replace("$","a")
    
    d={}
    latest = ""
    for i in range(len(b)):
        if i == len(b) - 1:
            print(latest)
            return
        
        if CntSubstr(b[0:i],a):
            latest = b[0:i]
        else:
            if latest:
                print(latest)
            latest = ""

            match(a[i:len(a)],b[i:len(b)])
        
  
  

