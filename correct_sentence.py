def correct_sentence(text: str) -> str:
    res = ""
    if text[0].islower():
        res += text[0].upper()
    else:
        res += text[0]
    if text[-1] != '.':
        res += text[1:] + '.'
    else:
        res += text[1:]
    return res

if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
