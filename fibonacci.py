n_terms = int(input ("How many terms to print? "))    
n_1 = 0  
n_2 = 1  
count = 0   
if n_terms <= 0:  
    print ("Number invalid")  
elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)    
else:  
    print ("The fibonacci no. sequence is:")  
    while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2  
        n_1 = n_2  
        n_2 = nth  
        count += 1  
