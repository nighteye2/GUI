numbers = []
n= int(input("Length of list :"))
for i in range (1,n+1):
    num= int(input("Enter number "+str(i)+":"))
    numbers.append(num)
    
numbers.sort()
sorted_list=sorted(numbers)
print("the second largest number is "+ str(sorted_list[-2]) +".")