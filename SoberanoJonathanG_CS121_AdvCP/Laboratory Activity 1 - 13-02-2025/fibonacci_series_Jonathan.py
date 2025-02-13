n = int(input("Enter the number of terms: "))
num1 = 0
num2 = 1
count = 0

print ("Fibonacci Series: ", end=' ')
while count < n:
    print(num1, end=' ')
    numth = num1 + num2
    num1 =num2
    num2 = numth
    count += 1