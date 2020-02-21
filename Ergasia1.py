from itertools import count 

cnt = count()
with open('data.txt', encoding='UTF-8') as infile:
			words = infile.read().split()
wordlist=sorted(words, key = lambda w : (len(w), next(cnt)),  
										reverse = True)[:5] 
print(wordlist)

for i in range(5): 
	word = wordlist[i]
	n = len(word)
	r = [' '] * n 
	print(word)
	for x in range(n):        
		r[x] = word[n - 1 - x]
		if (r[x] != 'a' and r[x] != 'e' and 
			r[x] != 'i' and r[x] != 'o' and 
			r[x] != 'u'): 
			print(r[x], end = "")
	print()