import random
import getpass

mystery_words_animals = ["ant", "monkey", "swordfish", "rhino", "girrafe"]
mystery_words_fruit = ["apple", "pear", "pineapple", "orange", "mango", "grape"]
mystery_words = ["telephone", "fridge", "communication", "porridge", "soul", "torch"]
progress_word = []

def start():
    no_of_players = int(input("Enter number of players(1 or 2): "))
    if (no_of_players == 1):
        topic = str(input("Choose a topic(animals, fruits or random): "))
        if topic in ["animals", "fruits", "random"]:
            decide_mystery_word(no_of_players, topic)
        else:
            print("Sorry, invalid topic")
            start()
    elif (no_of_players == 2):
        decide_mystery_word(no_of_players)
    else:
        print("Sorry, invalid number")
        start()

def decide_mystery_word(no_of_players, topic = None):
    if (no_of_players == 1):
        if (topic == "animals"):
            word_to_guess = chooseRandom(mystery_words_animals)
        elif (topic == "fruits"):
            word_to_guess = chooseRandom(mystery_words_fruit)
        else:
            word_to_guess = chooseRandom(mystery_words)
    else:
        print("First player get ready to choose the word!")
        word_to_guess = getpass.getpass("Enter your mystery word: ")
    
    for i in word_to_guess:
        progress_word.append("_")
    
    print("Get ready to start guessing!")
    game_start(word_to_guess)

def chooseRandom(name_of_list):
    return random.choice(name_of_list)

def game_start(word_to_guess):
    number_of_wrong_guesses = 0
    guessed_letters_words = []
    correct_guessed_letters = []
    while number_of_wrong_guesses != 7:
        if("".join(progress_word) == word_to_guess):
            endgame(True, word_to_guess)
            break
        player_guess = str(input("\nGuess a letter or a word: ")).lower()
        if len(player_guess) > 1:
            if (player_guess != word_to_guess):
                print("Opps! Wrong word! Try again")
                number_of_wrong_guesses += 1
                guessed_letters_words.append(player_guess)
                hangman(number_of_wrong_guesses, word_to_guess)
                continue
            else:
                endgame(True, player_guess)
                break
        else:
            if player_guess in guessed_letters_words:
                print(f"\n{player_guess} already guessed! Try again")
                letters_guessed(guessed_letters_words, correct_guessed_letters)
                continue
            if player_guess in word_to_guess:
                correct_guessed_letters.append(player_guess)
                guessed_letters_words.append(player_guess)
                print(f"{player_guess} is in the word!")
                letters_guessed(guessed_letters_words, correct_guessed_letters)
                word(word_to_guess, player_guess)
                continue
            else: 
                number_of_wrong_guesses += 1
                guessed_letters_words.append(player_guess)
                hangman(number_of_wrong_guesses, word_to_guess)
                letters_guessed(guessed_letters_words, correct_guessed_letters)
                continue

def word(word_to_guess, player_guess):
    index = 0
    for i in word_to_guess:
        if (i == player_guess):
            progress_word[index] = player_guess
            index += 1
        else:
            index += 1

    print("The word:\n" + " ".join(progress_word))

def letters_guessed(guessed_letters_words, correct_guessed_letters):
    print("\nTake a look at all your guesses: " + ",".join(guessed_letters_words))
    print(f"You guessed {len(correct_guessed_letters)} letters correct: " + ",".join(correct_guessed_letters))

def hangman(wrong_guess, word_to_guess):
    if (wrong_guess == 1):
        print("_______")
    elif (wrong_guess == 2):
        print(
"""
              |
              |
              |
              |
              |
            _______
""")
    elif (wrong_guess == 3):
        print(
"""
       -------
              |
              |
              |
              |
              |
           _______
""")
    elif (wrong_guess == 4):
        print(
"""
       -------
       |      |
              |
              |
              |
              |
           _______
""")        
    elif (wrong_guess == 5):
        print(
"""
       -------
       |      |
       O      |
              |
              |
              |
           _______
""")   
    elif (wrong_guess == 6):
        print(
"""
       -------
       |      |
       O      |
       |      |
      / \     |
              |
           _______
    ONE LAST GUESS TO LOSE THE GAME!
""")
    elif (wrong_guess == 7):
        print(
"""
       -------
       |      |
       O      |
       |      |
      /|\     |
      / \     |
           _______
""")   
        endgame(False, word_to_guess = word_to_guess)

def endgame(player_won: bool, guess = None, word_to_guess = None):
    if (player_won):
        print (f"YOU WON! {guess} was the mystery word")
    else:
        print("YOU LOST!")
        print(f"The word was: {word_to_guess}")


start()
