def main():
    number_of_rows = input("rows:")
    number_of_columns = input("columns:")
    print_gird(number_of_rows , number_of_columns)

def print_gird(number_of_rows , number_of_columns):
    for i in range(number_of_rows):
        print("*" * number_of_columns)
        print()