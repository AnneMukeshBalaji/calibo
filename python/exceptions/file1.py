x = input("Enter a Integer : ")
try : 
    x = int(x)
    print(f'x is {x}')
except Exception as e :
    print('Invaid Integer')
