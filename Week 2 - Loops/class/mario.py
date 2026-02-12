def main():
    print_square(4)

def print_square(size):
    for i in range(size):
        print("#" * size)

def print_row(width):
    print("?" * width)

def print_column(height):
    for _ in range(height):
        print("#")

main()