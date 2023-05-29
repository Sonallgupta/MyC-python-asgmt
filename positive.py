myList = []
lLimit = int(input("Enter Lower limit of the range : "))
uLimit = int(input("Enter Upper limit of the range : "))

# printing all positive values in a range 
print("All negative numbers of the range : ")
for i in range(lLimit, uLimit):
    if i < 0:
	    print(i, end = " ")
