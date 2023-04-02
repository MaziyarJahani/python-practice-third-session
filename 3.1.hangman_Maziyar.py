#hangman
import random
words_bank = ["gene", "genome", "transcriptome", "proteome", "metabolome"]
x = random.randint (0, len(words_bank)-1)
word = words_bank [x]
#second_word = random.choice (words_bank)
user_mistakes = 0
good_chars = []
bad_chars = []
nice_one = 0
while user_mistakes < 6:
    nice_one = 0
    for i in range(len(word)):
        if word[i] in good_chars:
            print(word[i], end=" ")
            nice_one = nice_one + 1
        else:
            print("_ ", end=" ")
    if nice_one == len(word):
        print("\n you won 💚")
        break
    user_character2 = input("please write your guess:")
    user_character = user_character2.lower()
    if len(user_character) == 1:
        if user_character in word:
            good_chars.append(user_character)
            print("✅")
        else:
            bad_chars.append(user_character)
            user_mistakes +=1
            print("❌")
    else:
        print("please enter one word")
if user_mistakes == 6:
    print("game over 💔")

