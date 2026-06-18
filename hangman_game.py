import random
words=["python","program","tuples","syntax", "coding"]
word=random.choice(words)
print("Welcome to Hangman")
guessed_word=[]
for letter in word:
    guessed_word.append("_")
print(" ".join(guessed_word))
wrong_guesses=0
max_guesses=6
guessed_letters=[]
while wrong_guesses < max_guesses and "_" in guessed_word:
    guess=input("Guess the word by guessing the letter: ").lower()
    if len(guess) != 1:
        print("Please enter only one letter.")
        continue
    if guess in guessed_letters:
        print("Already guessed letter")
        continue
    guessed_letters.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print("Remaining chances:", max_guesses - wrong_guesses)

    print(" ".join(guessed_word))
if "_" not in guessed_word:
        print("Congratulations!!\nYou guessed the word:", word)
else:
        print("Game Over!")
        print("The word was:", word)
