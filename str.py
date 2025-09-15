def pr_str(s):
    if not isinstance(s, str):
        return "Очікується string"
    return s

def ch_case(s):
    if not isinstance(s, str):
        return "Очікується string"
    if s.isupper():
        return "Великі"
    elif s.islower():
        return "Малі"
    else:
        return "Змішані"

def uppercase_let(word):
    if not isinstance(word, str):
        return "Очікується string"
    return [char.upper() for char in word]