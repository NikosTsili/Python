message = input("Enter message to encode: ")

print("Decoded string (in ASCII):")

#αντιστοίχιση κάθε χαρακτήρα του string στον αριθμό ASCII
num = int(''.join(str(ord(c)) for c in message))
print(num)

#έλεγχος αν είναι πρώτος
if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
      
else:
   print(num,"is not a prime number")
