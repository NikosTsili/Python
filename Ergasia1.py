from itertools import count 

cnt = count()
#άνοιγμα, ανάγνωση αρχείου κατά λέξεις.
with open('data.txt', encoding='UTF-8') as infile:
			words = infile.read().split()
#δημιουργία λίστας με ταξινόμηση των 5 μεγαλύτερων λέξεων, από την μεγαλύτερη στην μικρότερη
wordlist=sorted(words, key = lambda w : (len(w), next(cnt)),  
										reverse = True)[:5] 
print(wordlist)

for i in range(5): 
	#ανάγνωση κάθε λέξης ξεχριστά
	word = wordlist[i]
	n = len(word)
	#δημιουργία κενής λίστας που θα μπει η αντεστραμένη λέξη
	r = [' '] * n 
	print(word)
	for x in range(n): 
		#αντιστροφή λέξης
		r[x] = word[n - 1 - x]
		#απαλοιφή φωνηέντων
		if (r[x] != 'a' and r[x] != 'e' and 
			r[x] != 'i' and r[x] != 'o' and 
			r[x] != 'u'): 
			print(r[x], end = "")
	print()
