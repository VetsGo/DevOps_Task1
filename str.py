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