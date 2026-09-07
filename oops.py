
# Encapsulation

class class_value:
    def __init__(self) -> None:
        self.__privateValues = 10
        self._protectedValue = 20     
    def getvalue(self) -> int:
        return self.__privateValues
obj = class_value()
# print(obj.__privateValues) This will return an attribute error
print(obj.getvalue())

# Inheritance 

class parent :
    def __init__(self) -> None:
        print('Inside Parent Class')
    def parent_method(self) -> None:
        print('Inside Parent Method')

class child(parent): 
    def __init__(self) -> None:
        super().__init__()
        print('Inside Child Class')
obj = child()

# 
