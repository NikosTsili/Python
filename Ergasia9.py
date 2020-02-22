import random

#Αξία χαρτιών
def get_card_value(x):
	if x[1] == "J":
		return 11
	elif x[1] == "Q":
		return 12
	elif x[1] == "K":
		return 13
	elif x[1] == "A":
		return 14
	else:
		return int(x[1])


#έλεγχος flush
def check_flush(hand):
	suits = [h[0] for h in hand]
	if len(set(suits)) == 1:
	  return True
	else:
	  return False

#έλεγχος straight
def check_straight(values):
	return sorted(values) == list(range(min(values), max(values)+1))

#έλεγχος straight flush
def check_straight_flush(values, hand):
	if check_flush(hand) and check_straight(values):
		return True
	else:
		return False

#έλεγχος four of a kind
def check_four_of_a_kind(values):
	values.sort()
	if values[0] == values[1] == values[2] == values[3] or values[1] == values[2] == values[3] == values[4]:
		return True
	return False

#έλεγχος full house
def check_full_house(values):
	values.sort()
	if values[0] == values[1] and values[1] != values[2] and values[2] == values[3] ==values[4]:
		return True
	elif values[0] == values[1] == values[2] and values[2] != values[3] and values[3] ==values[4]:
		return True
	return False

#έλεγχος three of a kind
def check_three_of_a_kind(values):
	values.sort()
	if values[2] == values[1] and (values[1] == values[0] or values[2] == values[3]):
		return True
	elif values[2] == values[3] and values[3] == values[4]: 
		return True
	return False


#έλεγχος High Card
def check_high_card(values1, values2):
	values1.sort()
	values2.sort()
	if values1[4]>values2[4]:
		print("Player1 wins!")
	elif values1[4]<values2[4]:
		print("Player2 wins!")
	elif values1[3]>values2[3]:
		print("Player1 wins!")
	elif values1[3]<values2[3]:
		print("Player2 wins!")
	elif values1[2]>values2[2]:
		print("Player1 wins!")
	elif values1[2]<values2[2]:
		print("Player2 wins!")
	elif values1[1]>values2[1]:
		print("Player1 wins!")
	elif values1[1]<values2[1]:
		print("Player2 wins!")
	elif values1[0]>values2[0]:
		print("Player1 wins!")
	elif values1[0]<values2[0]:
		print("Player2 wins!")
	else:
		print("Tie!")


# δημιουργία τράπουλας
xrwma = ["S", "H", "D", "C"]
figoura = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
trapoula = []
for i in xrwma:
	for j in figoura:        
		trapoula.append([i,j])

# ανακάτεμα τράπουλας
random.shuffle(trapoula)
#print(trapoula)
hand1=[]
hand2=[]

#μοίρασμα 5 χαρτιών, εναλλάξ από ένα, σε κάθε παίχτη
for i in range(5):
	hand1.insert(i,trapoula.pop())
	hand2.insert(i,trapoula.pop())
print("Hand of first player:",hand1)
print("Hand of second player:",hand2)

#εύρεση αξίας χαρτιών
values1=[]
values2=[]
for c in hand1:	
	values1.append(get_card_value(c))
for c in hand2:
	values2.append(get_card_value(c))
#print(values1)
#print(values2)


# έλεγχος αποτελεσμάτων συναρτήσεων (δεν απαιτούνται στο τελικό πρόγραμμα)
#print(check_flush(hand1))
#print(check_flush(hand2))
#print(check_straight(values1))
#print(check_straight_flush(values1,hand1))
#print(check_four_of_a_kind(values1))
#print(check_full_house(values1))
#print(check_three_of_a_kind(values1))


if check_straight_flush(values1,hand1) == True and check_straight_flush(values2,hand2) == False:
	print("Straight Flush: Player1 wins!")
elif check_straight_flush(values1,hand1) == False and check_straight_flush(values2,hand2) == True:
	print("Straight Flush: Player2 wins!")
elif check_straight_flush(values1,hand1) == True and check_straight_flush(values2,hand2) == True:
	print("Straight Flush for both players")
	check_high_card(values1,values2)
elif check_four_of_a_kind(values1) == True and check_four_of_a_kind(values2) == False:
	print("Four of a kind: Player1 wins!")
elif check_four_of_a_kind(values1) == False and check_four_of_a_kind(values2) == True:
	print("Four of a kind: Player2 wins!")
elif check_four_of_a_kind(values1) == True and check_four_of_a_kind(values2) == True:
	print("Four of a kind for both players")
	check_high_card(values1,values2)
elif check_full_house(values1) == True and check_full_house(values2) == False:
	print("Full House: Player1 wins!")
elif check_full_house(values1) == False and check_full_house(values2) == True:
	print("Full House: Player2 wins!")
elif check_full_house(values1) == True and check_full_house(values2) == True:
	print("Full House for both players")
	check_high_card(values1,values2)
elif check_flush(hand1) == True and check_flush(hand2) == False:
	print("Flush: Player1 wins!")
elif check_flush(hand1) == False and check_flush(hand2) == True:
	print("Flush: Player2 wins!")
elif check_flush(hand1) == True and check_flush(hand2) == True:
	print("Flush for both players")
	check_high_card(values1,values2)
elif check_straight(values1) == True and check_straight(values2) == False:
	print("Straight: Player1 wins!")
elif check_straight(values1) == False and check_straight(values2) == True:
	print("Straight: Player2 wins!")
elif check_straight(values1) == True and check_straight(values2) == True:
	print("Straight for both players")
	check_high_card(values1,values2)
elif check_three_of_a_kind(values1) == True and check_three_of_a_kind(values2) == False:
	print("Three of a kind: Player1 wins!")
elif check_three_of_a_kind(values1) == False and check_three_of_a_kind(values2) == True:
	print("Three of a kind: Player2 wins!")
elif check_three_of_a_kind(values1) == True and check_three_of_a_kind(values2) == True:
	print("Three of a kind for both players")
	check_high_card(values1,values2)
else:
	check_high_card(values1,values2)