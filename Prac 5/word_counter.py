string = input("Please enter a sentence: ")
text = string
string = string.lower()
string = string.split(' ')
string_dict = {}
print('Text: {}'.format(text))
longestword = 0
string_list = []
for word in string:
    if len(word) > longestword:
        longestword = len(word)

    string_dict[word] = 0

    for other_word in string:
        if word == other_word:
            string_dict[word] += 1

for word in string_dict:
    string_list.append(word)

string_list.sort()
for word in string_list:
    print('{:{}} = {}'.format(word, longestword, string_dict[word]))

