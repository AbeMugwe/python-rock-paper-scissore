import re

with open ('number.txt','r') as number:
    data=number.read()

    #find_number=r'(?:[0-9]+ |(?:[0-9]{1,3},\d{3})| (?:[0-9]{1,3},\d{3})| (?:[0-9]{1}.\d{1})|(?:[0-9]{1}\.\d{1}))'
    find_number=r'\b\d+(?:,\d+)*(?:\.\d+)?\b'
    numbers=re.findall(find_number,data)
    sum_number=[]
    manual_sum=0
    for number in numbers:
      integer=float(number.replace(',',''))
      sum_number.append(integer)
      manual_sum+=integer

    print(manual_sum)  
    
    
        
        
               
       
         
  
              

    
  
        
        
    
    
        
    
    




    #print(re.findall(find_number,data))


