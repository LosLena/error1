list = input("Введите операцию сложение (+, -, *, /): ")
t = ['+', '-', '*', '/']
try:
  assert list in t
  number1 = input("Введите 1 положительное число: ")
  number2 = input("Введите 2 положительное число: ")
  print(f"Необходимо вычислить {list} {number1} {number2}")
  try:
    if int(number1) >= 0 and int(number2) >= 0:
      if list == t[0]:
        print(f"Значение сложение {int(number1)+int(number2)}")
      elif list == t[1]:
        print(f"Значение вычитания {int(number1)-int(number2)}")
      elif list == t[2]:
        print(f"Значение умножения {int(number1)*int(number2)}")
      elif list == t[3]:
        try:
          #if int(number2) == 0:
          print(f" Значение  {int(number1)/int(number2)}")
        except ZeroDivisionError:
            print("Вы ввели 0, деление на 0 невозможно") 

  except:
    print("Вы ввели не положительные числа") 
except:
    print("Операция не входит в список разрешенных") 
 