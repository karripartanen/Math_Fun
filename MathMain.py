import sympy
import numpy as np
import time
import os
from colorama import Back as CB, Fore as CF, Style as CS
from sympy import symbols, solve
# calculate some damn matrices or SOE if u feel like it


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def solve_systems():
    x, y, z = symbols('x, y, z')
    equations = []
    print("Enter the desired equations in the form: a*x + b*y + c*z = d")
    for i in range(3):
        while True:
            try:
                equation_str = input(f"Enter equation {i+1}: ")
                equation = sympy.sympify(equation_str.replace('=', '-').replace(' ', '') + '- 0')
                equations.append(equation)
                break
            except (ValueError, TypeError, SyntaxError):
                print("Invalid equation format! Try again.")
    try:
        solution = solve(equations, (x, y, z))
        clear()
        print(f"Equations: {equations}")
        print(f"Solution: {solution}")
    except Exception as e:
        print(f"Error solving the equations: {e}")


def decimal_to_binary(decimal):
    try:
        decimal = int(decimal)
        if decimal < 0:
            raise ValueError("Decimal number must be positive.")
        binary_num = bin(decimal)
        return binary_num
    except ValueError as ve:
        return None
    except TypeError:
        return None


def binary_to_decimal(binary):
    try:
        decimal = int(binary, 2)
        return decimal
    except ValueError:
        return None


def hex_to_binary(hexadecimal):
    try:
        decimal = int(hexadecimal, 16)
        binary = bin(decimal)[2:]
        return binary
    except ValueError:
        return None


def create_matrix(rows, cols):
    matrix = []
    print("Enter the elements of the matrix row-wise")

    for i in range(rows):
        row = []
        while True:
            try:
                elements = input(f"Enter {cols} elements for row {i+1} separated by space(' '): ")
                row = list(map(int, elements.split()))
                if len(row) == cols:
                    matrix.append(row)
                    break
                else:
                    print(f"Invalid input! {cols} elements expected!")
            except ValueError:
                print("Invalid input! Please enter a valid integer.")
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


def check_matrix(matrix):
    cols_count = len(matrix[0])
    for row in matrix:
        if len(row) != cols_count:
            return False
        return True


while True:
    try:
        clear()
        valid_option = True
        print(f"{CF.LIGHTGREEN_EX}Choose from the following:{CF.RESET}")
        print("\n1. Calculate Matrices")
        print("2. Solve Systems of Equations")
        print("3. Decimal to binary/hex")
        print("4. Binary to decimal/hex")
        print("5. Hexadecimal to decimal/binary.")
        print(f"{CF.RED}6. Exit the program{CF.RESET}")
        option = input(f"{CF.YELLOW}\nEnter your choice (1 / 2 / 3...):{CF.RESET} ")

        if option == '1':
            rows = int(input("Enter the number of rows in the matrix: "))
            cols = int(input("Enter the number of columns in the matrix: "))

            while True:
                matrix = create_matrix(rows, cols)
                if check_matrix(matrix):
                    clear()
                    print("\nThe matrix: ")
                    print_matrix(matrix)

                    matrix_t = np.transpose(matrix)
                    print(f"\nTranspose =\n{matrix_t}\n")

                    determinant = np.linalg.det(matrix)
                    print(f"Determinant = {determinant:.1f}\n")

                    input("Press ENTER to continue.")
                    clear()
                    break
                else:
                    print("\nInvalid matrix! Number of rows and columns need to match.")

        elif option == "2":
            solve_systems()

        elif option == "3":
            clear()
            while True:
                decimal = input("Enter a decimal number: ")
                binary = decimal_to_binary(decimal)
                if binary is not None:
                    print(f"Binary representation: {binary[2:]}")
                    hexadecimal = hex(int(decimal))[2:]
                    print(f"Corresponding hexadecimal: {hexadecimal}")
                    input("\nPress ENTER to continue: ")
                    break
                else:
                    print("Invalid input! Enter a valid decimal.")

        elif option == "4":
            clear()
            while True:
                binary = input("Enter a binary number (ie. 01011101): ")
                decimal = binary_to_decimal(binary)
                if decimal is not None:
                    clear()
                    print(f"Decimal representation: {decimal}")
                    hexadecimal = hex(decimal)[2:]
                    print(f"Corresponding hexadecimal: {hexadecimal}")
                    input("\nPress ENTER to continue: ")
                    break
                else:
                    print("Invalid input! Enter a valid hexadecimal.")

        elif option == "5":
            clear()
            while True:
                hexadecimal = input("Enter a hexadecimal number: ")
                binary = hex_to_binary(hexadecimal)
                if binary is not None:
                    clear()
                    print(f"Hexadecimal: {hexadecimal}")
                    print(f"Binary representation: {binary}")
                    decimal = int(binary, 2)
                    print(f"Corresponding decimal: {decimal}")
                    input("\nPress ENTER to continue: ")
                    break
                else:
                    print("Invalid input! Enter a valid hexadecimal.")

        elif option == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid input! Type in '1' or '2'")

    except KeyboardInterrupt:
        print("\nUser interrupted the program. Exiting.")
        time.sleep(2)
        break
    except ValueError:
        print("\nInvalid input! Not a valid Integer")
    except Exception as e:
        print(f"\nError detected (Most likely solving the determinant): {e} ")
