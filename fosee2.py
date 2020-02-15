def word_frequency(s, n):
	words = dict()
	for word in s.split():
		words[word] = 1 + words.get(word, 0)

	sol = []
	count = 0
	print(words)
	print(sorted(words))
	for i in sorted(words):
		sol.append((i, words[i]))

	sol2 = []
	count = 0
	i = 0
	while count < n:
		sol2.append(sol[i])
		while i + 1 < len(sol) and sol[i] == sol[i + 1]:
			i += 1
			sol2.append(i)
		i += 1
		count += 1

	return sol2

s = "aaa a a aa Aa aa"
l = word_frequency(s, 2)
print(l)