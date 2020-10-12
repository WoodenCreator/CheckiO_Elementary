def between_markers(text: str, begin: str, end: str) -> str:
    str =""
    x = 0
    while text[x]:
        if (text[x] == begin):
            x+=1
            while (text[x] != end):
                str +=text[x]
                x+=1
            if text[x]== end:
                break
        else:
            x+=1

    return str


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
