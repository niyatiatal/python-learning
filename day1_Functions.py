def sumeven(ar,n):
    sum = 0
    i = 0
    for i in range(n):
        if(ar[i]%2==0):
            sum = sum + ar[i]
    return sum

def countvowels(str):
    count = 0
    for i in range(len(str)):
        if (str[i] == 'a' or str[i] == 'e' or str[i] == 'i' 
            or str[i] == 'o' or str[i] == 'u' or str[i] == 'A' or str[i] == 'E' 
            or str[i] == 'I' or str[i] == 'O' or str[i] == 'U'):
            count = count + 1
    return count

def min_max(ar,n):
    min = ar[0]
    max = ar[0]
    for i in range(n):
        if(ar[i] < min):
            min = ar[i]
        if(ar[i] > max):
            max = ar[i]
    return min,max

num = int(input("Enter number for array :"))
sentence = input("enter a sentence : ")
a = [0]*num
for j in range(num):
    a[j] = int(input("Enter a number : "))

print("Sum of even numbers : ", sumeven(a,num))
print("Number of vowels : ", countvowels(sentence))
minimum, maximum = min_max(a,num)
print("Minimum : ", minimum)
print("Maximum : ", maximum)