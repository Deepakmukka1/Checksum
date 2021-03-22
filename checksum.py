print("\n--------------Sender side-------------------------")
numbers=input("Enter the dataword (16bit) : \n")
def binaryToDecimal(a):
    n=len(a)
    sums=0
    for i in range(0,n):
        sums=sums+(int(a[i])*pow(2,n-i-1))
    return sums
def decimalToBinary(val):
    rem=0
    sums1=0
    i=1
    val=int(val)
    while val>0:
        rem=val%2
        sums1=sums1+int(rem)*int(i)
        i=i*10
        val=val/2
    return sums1
def reciever():
    print("\n--------------Reciever side-------------------------")
    inputs=input("Enter the reciever side dataword 24 bit (16+8 bit checksum) \n")
    string1=inputs[0:8]
    string2=inputs[8:16]
    string3=inputs[16:24]
    num1=binaryToDecimal(string1)
    num2=binaryToDecimal(string2)
    num3=binaryToDecimal(string3)
    ans=decimalToBinary(num1+num2+num3)
    ans1=str(ans)
    if len(ans1)>8:
        chars=int(ans1[0])
        fn=binaryToDecimal(ans1[1:])
        finalAnswer=decimalToBinary(fn+chars)
    else:
        finalAnswer=int(ans1)
    finalAnswer=11111111-finalAnswer
    if finalAnswer==0 :
        print("The checksum at reciever side","0"*8)
        print("There is no error in transmission",)
    else:
        print("The checksum at reciever side is : ",finalAnswer)
        print("There is Error in transmission  ")
string1=numbers[0:8]
string2=numbers[8:16]
num1=binaryToDecimal(string1)
num2=binaryToDecimal(string2)
ans=decimalToBinary(num1+num2)
ans1=str(ans)
if len(ans1)>8:  
    chars=int(ans1[0])
    fn=binaryToDecimal(ans1[1:])
    finalAnswer=decimalToBinary(fn+chars)
else:    
    finalAnswer=int(ans1)
finalAnswer=11111111-finalAnswer
print("The checksum is ",finalAnswer)
reciever()
