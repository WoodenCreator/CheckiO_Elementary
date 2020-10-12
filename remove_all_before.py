from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:
   x = 0
   count = 0
   z:bool = True
   y:list = []
   while x < len(items): # проверяю есть ли граница в списке как число
      if (items[x] != border and count == 0):
           x+=1
      else:
          break
   if x == len(items):
       z = False
   x = 0
   if z == True:
        while x < len(items): # вывод чисел
            if (items[x] != border and count == 0):
                x+=1
            else:
                y.insert(count, items[x])
                x+=1
                count+=1
   else:
        while x < len(items):
            y.insert(count, items[x]) #вводим новый элемент списка
            x+=1
            count+=1
   return y




if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")