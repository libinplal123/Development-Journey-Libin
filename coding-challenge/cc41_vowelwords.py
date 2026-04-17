# Part A
def words_with_vowels(sentence):
    vowels = "aeiou"
    vowel_words = []
    word_list = sentence.split(" ")
    for word in word_list:
        for ch in vowels:
            if ch in word and word not in vowel_words:
                vowel_words.append(word)
    return vowel_words
print(words_with_vowels("you have no rhythm"))

# Part B
class Ford():
    def __init__(self,car_model,Color,Year,Transmission,Electric):
        self.car_model = car_model
        self.Color = Color
        self.Year = Year
        self.Transmission = Transmission
        self.Electric = Electric
        print(f"""
car_model = {self.car_model}
Color = {self.Color}
Year = {self.Year}
Transmission = {self.Transmission}
Electric = {self.Electric}""")
class BMW(Ford):
    def __init__(self,car_model,Color,Year,Transmission,Electric):
        super().__init__(car_model,Color,Year,Transmission,Electric)
class Tesla(Ford):
    def __init__(self,car_model,Color,Year,Transmission,Electric):
        super().__init__(car_model,Color,Year,Transmission,Electric)

ford1  = Ford("focus","white",2020,"Auto",False)
bmw1 = BMW("x6","silver",2018,"Auto",False)
tesla1 = Tesla("S","beige",2017,"Auto",True)