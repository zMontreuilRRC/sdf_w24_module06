# class: plan for the design of instances of the type
class Human:
    # defining a constructor replaces the default constructor
    def __init__(self, name: str, age: int):
        print("New human!")

        # assigning two new attributes for the instance
        # underscore is the convention of a private attribute
        # private attributes should never be accessed outside of the class definition
        if age > 0 and len(name) >= 0:
            self._name = name
            self._age = age
        else:
            raise ValueError("Argument error for instantiation")
        
    # accessor methods
    # "publicly exposed" value of an attribute
    @property
    def age(self) -> int:
        return self._age
    
    @property
    def name(self) -> str:
        if self._age >= 18:
            return self._name
        else:
            raise Exception("Unable to access names of people who are not legal adults")

    @name.setter
    def name(self, new_value: str):
        if len(new_value) > 0:
            self._name = new_value
        else:
            raise ValueError("Cannot add an empty new name")


    
# three distinct instances of Human assigned to different variables
zach = Human("Zach", 33)

#_{attribute_name} = private attribute
# {attribute_name} = public property

print(zach.age)
print(zach.name)

zach.name = ""

zach._name = ""

print(zach.name)
