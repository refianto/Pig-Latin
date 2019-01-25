inp = input()
out = []

def pig():
	a = inp.split()
	result = []
	for i in a:
		word = []
		if len(i) < 2:
			text1 = i+'es'
			result.append(text1)
		elif len(i) == 2:
			j = len(i)
			for k in range(j):
				j -= 1
				word.append(i[j])
			text2 = ''.join(word)+'es'
			result.append(text2)
			# print (text)
		elif len(i) > 2:
			par = ['a','i','u','e','o']
			idx1 = []
			idx2 = []
			for j in i:
				if j in par:
					k = i.index(j)
					for l in range(k,len(i)):
						idx2.append(i[l])
					break
				idx1.append(j) 
			text3 = ''.join(idx2)+''.join(idx1)+'es'
			result.append(text3)
	text = ' '.join(result)
	return text
print (pig())