#Συνάρτηση για την πρόσθεση των ψηφίων του αριθμού
def addDigits(x):
	add = 0
	while x != 0:
		dig = abs(x) % 10
		add = add + dig
		x = int(x/10)
	return add

num = int(input("Enter a Number: "))

#Επανάληψη διαδικασίας μέχρι ο αριθμός να γίνει μονοψήφιος
while num>9 or num<-9:
	print("3 * ", num,"+ 1 =")
	num = 3*num+1
	print(num)
	num=addDigits(num)
	print("Sum of digits equals to:", num)
	