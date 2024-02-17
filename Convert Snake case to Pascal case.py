def snake_to_pascal(s):
    return ''.join(word.capitalize() for word in s.split('_'))

snake_case_string = input("Enter a string in snake_case: ")
pascal_case_string = snake_to_pascal(snake_case_string)
print("String in PascalCase:", pascal_case_string)
