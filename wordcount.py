def get_word_count(file):
	
	word_count = {}

	poem = open(file)
	for line in poem:
		line = line.rstrip().split()

		for word in line:
			word = word.strip("~!@#$%^&*()_+`-=[}{|;',<.>/?:")
			word = word.lower()
			word_count[word] = word_count.get(word, 0) + 1

	for k, v in word_count.items():
		print('{} {}'.format(k,v))

get_word_count('test.txt')

