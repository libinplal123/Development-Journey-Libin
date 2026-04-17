from textblob import TextBlob
def spelling_checker():
    while True:
        word = (input("enter a word:")).lower()
        correct_word = TextBlob(word).correct()
        if word == correct_word:
            return word
        elif word != correct_word:
            check_input = (input(f"Did you mean '{correct_word}'? (yes/no) ")).lower()
            if check_input == "yes":
                return correct_word
            else:
                print("Let's try again...")
print(spelling_checker())
