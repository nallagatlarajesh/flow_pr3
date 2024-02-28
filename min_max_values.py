#program to input five numbers and print largest and smallest numbers
smallest=0
largest=0
for i in range(0,5):    #5 iterations =5 rounds 
    x=int(input("enter the number"))
    if i==0:
        smallest=largest=x
    if x<smallest:
        smallest=x
    if x>largest:
        largest=x
print("the smallest number is",smallest )
print("the largest number is ",largest) 
