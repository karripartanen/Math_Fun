import sympy
import numpy as np
import time
import os
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
        print("Choose one:")
        print("1. Calculate Matrices")
        print("2. Solve Systems of Equations")
        option = input("Enter your choice (1 / 2): ")

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
        else:
            valid_option = False
            print("Invalid input! Type in '1' or '2'")

        if valid_option:
            repeat = input("Do you want to continue? (Y/N): ").lower().strip()
            if repeat != 'y':
                print("Exiting the program")
                time.sleep(2)
                break

    except KeyboardInterrupt:
        print("\nUser interrupted the program. Exiting.")
        time.sleep(2)
        break
    except ValueError:
        print("\nInvalid input! Not a valid Integer")
    except Exception as e:
        print(f"\nError detected (Most likely solving the determinant): {e} ")
