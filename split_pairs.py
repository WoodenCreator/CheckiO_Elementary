def split_pairs(a:str)-> list:
    x = 0
    y = 0
    maff = a
    arr=[]
    if len(maff) % 2 == 1 and len(maff) >= 2:
        while y < len(maff):
            if y == len(maff)-1:
                arr.append(maff[x]+'_')
                y+=1
            else:
                arr.append(maff[x]+maff[y+1])
                x+=2
                y+=2
    elif len(maff) % 2 == 0 and len(maff) >= 2:
         while y < len(maff):
                arr.append(maff[x]+maff[y+1])
                x+=2
                y+=2
    else:
        if (len(maff) == 1):
            arr.append(maff[x] + '_')
    return arr



if __name__ == '__main__':
    print("Example:")
    print(list(split_pairs('abcd')))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")