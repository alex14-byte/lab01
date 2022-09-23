import math as m



def nod(a,b):
    while a != b:
         if a > b:
            a = a - b
         else:
            b = b - a
    print(a)


if __name__ == '__main__':
  nod(2,4)