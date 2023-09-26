a = str(input("Enter your English word or Code Word:"))
def coding(a): 
    
    print(a)

    def swap(a):
        
        # storing the first character
        start = a[0]
        
        # storing the last character
        end = a[-1]
        
        swapped_string = end + a[1:-1] + start
        print(swapped_string)


    if(len(a)<=3):
        print(a[::-1])
    else:
        swap(a)


def decoding(a):
    
    print(a)

    def again_swap(a):
        
        # storing the first character
        start = a[0]
        
        # storing the last character
        end = a[-1]
        
        Orignal_string = end + a[1:-1] + start
        print(Orignal_string)
    
    if(len(a)<=3):
        print(a[::-1])
    else:
        again_swap(a)


x = str(input("Choose Coding or Decoding"))

match x:
    case "Coding":
        coding(a)
   
    case "Decoding":
        decoding(a)
