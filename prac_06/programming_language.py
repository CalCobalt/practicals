class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        
    def is_dynamic(self):
        return self.typing.lower() == "dynamic"
    
    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year
        )
        