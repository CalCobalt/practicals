from programming_language import ProgrammingLanguage


languages = [
    ProgrammingLanguage("Java", "Static", True, 1995),
    ProgrammingLanguage("C++", "Static", False, 1983),
    ProgrammingLanguage("Python", "Dynamic", True, 1991),
    ProgrammingLanguage("Visual Basic", "Static", False, 1991),
    ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
]

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", False, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    print(ruby)
    print(python)
    print(visual_basic)
    is_dynamic()

def is_dynamic():
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

main()