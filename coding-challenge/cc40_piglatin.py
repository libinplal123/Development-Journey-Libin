def translate(sentence):
    vowels = "aeiou"
    words = sentence.split(" ")
    new_words = []
    for w in words:
        if w.startswith(vowels):
            w = w + "yay"
            new_words.append(w)
        else:
            w = w[1:] + w[0] + "ay"
            new_words.append(w)
    return " ".join(new_words)
print(translate("i love python"))
