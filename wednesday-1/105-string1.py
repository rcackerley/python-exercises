# string = raw_input("What do you want capitalized?")

# caps_string = string.upper()
# print caps_string

# string = raw_input("What do you want capitalized?")

# print string.capitalize()

# print string[::-1]

# paragraph = raw_input("Give me some words")
# paragraph = list(paragraph)
# for i in range (0, len(paragraph)):
#     if paragraph[i] == 'A':
#         paragraph[i] = '4'
#     elif paragraph[i] == 'E':
#         paragraph[i] = '3'
#     elif paragraph[i] == 'G':
#         paragraph[i] = '6'
#     elif paragraph[i] == 'I':
#         paragraph[i] = '1'
#     elif paragraph[i] == 'O':
#         paragraph[i] = '0'
#     elif paragraph[i] == 'S':
#         paragraph[i] = '5'
#     elif paragraph[i] == 'T':
#         paragraph[i] = '7'

# paragraph = ''.join(paragraph)
        

# print paragraph

# given_word = raw_input('Give e a word!')

# for letter in range(0, len(given_word) - 1):
#     if given_word[letter] == given_word[letter + 1]:
#         # print given_word
#         given_word = list(given_word)
#         given_word[letter] = given_word[letter] + given_word[letter] + given_word[letter] + given_word[letter]
#         given_word = ''.join(given_word)
#         print given_word
#         break
#     else:
#         print given_word
#         break

message = 'lbh zhfg hayrnea jung lbh unir yrnearq'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
deciphered_message = []
for coded_letter in range(0,len(message)):
    for letter in range(0, len(alphabet)):
        if message[coded_letter] == alphabet[letter]:
            deciphered_message.append(alphabet[letter - 13])
            
deciphered_message = ''.join(deciphered_message)
print deciphered_message          
