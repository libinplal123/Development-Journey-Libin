import re
def analyse_string(sentence):
    char_dict = {}
    special_char = re.findall(r"[^\w\s]",sentence)
    words = re.findall(r"[a-zA-Z]+",sentence)
    total_char = re.findall(r"\S",sentence)
    char_dict["special characters"] = len(special_char)
    char_dict["words"] = len(words)
    char_dict["total characters"] = len(total_char)
    print(char_dict)
test_sentence = """Python has a string format operator %. This functions analogously to printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2) evaluates to "spam=blah eggs=2"."""
analyse_string(test_sentence)