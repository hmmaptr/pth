class person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = person("Ilham", 16)
print(p1)