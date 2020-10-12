def is_all_upper(text: str) -> bool:
   t = True
   x = 0
   arr=text
   y = len(text)
   print(type(x))
   while x < y:
        if (arr[x].isupper() or arr[x] == " " or arr[x].isdigit()):
            x+=1
            t = True
            continue
        else:
            t = False
            print(t)
            return False
   print(t)
   return t

if __name__ == '__main__':
    print("Example:")
  #  print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
