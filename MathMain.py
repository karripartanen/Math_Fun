import sympy
import numpy as np
import time
import os
from colorama import Back as CB, Fore as CF, Style as CS
from sympy import symbols, solve
import json
import requests as req
# calculate some damn matrices or SOE if u feel like it


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def country_info(country):
    try:
        request = f"https://restcountries.com/v3.1/name/{country}"
        response = req.get(request)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list) and data:
            country_info = data[0]
            print(f"\nCountry Information for {country}:")
            print(f"\nName: {country_info['name']['common']}")
            print(f"Capital: {country_info['capital'][0]}")
            print(f"Population: {country_info['population']}")
            print(f"Area: {country_info['area']} square kilometers")
            print(f"Region: {country_info['region']}")
        else:
            print(f"Learn to type.")
    except req.exceptions.RequestException as e:
        print(f"Learn to type.")


def chuck():
    try:
        request = "https://api.chucknorris.io/jokes/random"
        response = req.get(request).json()
        return response['value']
    except Exception as e:
        return None


def random_fact():
    try:
        request = "https://useless-facts.sameerkumar.website/api"
        response = req.get(request).json()
        return response['data']
    except Exception as e:
        return None


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
        print(f"Solution: {CF.LIGHTGREEN_EX}{solution}{CF.RESET}")
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


def calc_volume(length, width, height):
    try:
        length = float(length)
        width = float(width)
        height = float(height)

        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive.")

        volume = length * width * height
        return volume

    except ValueError as ve:
        return None
    except TypeError:
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
        print(f"{CF.LIGHTGREEN_EX}{row}{CF.RESET}")


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
        print("6. Calculate volume of an object.")
        print("7. Country info.")
        print("8. Random Chuck Norris joke.")
        print("9. Random fact for you ;).")
        print(f"{CF.RED}10. Exit the program{CF.RESET}")
        option = input(f"{CF.YELLOW}\nEnter your choice (1 / 2 / 3...):{CF.RESET} ")

        if option == '1':
            clear()
            rows = int(input("Enter the number of rows in the matrix: "))
            cols = int(input("Enter the number of columns in the matrix: "))

            while True:
                matrix = create_matrix(rows, cols)
                if check_matrix(matrix):
                    clear()
                    print("\nThe matrix: ")
                    print_matrix(matrix)

                    matrix_t = np.transpose(matrix)
                    print(f"\nTranspose =\n{CF.LIGHTGREEN_EX}{matrix_t}{CF.RESET}\n")

                    determinant = np.linalg.det(matrix)
                    print(f"Determinant = {CF.LIGHTGREEN_EX}{determinant:.1f}{CF.RESET}\n")

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
                    print(f"Binary representation: {CF.LIGHTGREEN_EX}{binary[2:]}{CF.RESET}")
                    hexadecimal = hex(int(decimal))[2:]
                    print(f"Corresponding hexadecimal: {CF.LIGHTGREEN_EX}{hexadecimal}{CF.RESET}")
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
                    print(f"Decimal representation: {CF.LIGHTGREEN_EX}{decimal}{CF.RESET}")
                    hexadecimal = hex(decimal)[2:]
                    print(f"Corresponding hexadecimal: {CF.LIGHTGREEN_EX}{hexadecimal}{CF.RESET}")
                    input("\nPress ENTER to continue: ")
                    break
                else:
                    print("Invalid input! Enter a valid binary.")

        elif option == "5":
            clear()
            while True:
                hexadecimal = input("Enter a hexadecimal number: ")
                binary = hex_to_binary(hexadecimal)
                if binary is not None:
                    clear()
                    print(f"Hexadecimal: {CF.LIGHTGREEN_EX}{hexadecimal}{CF.RESET}")
                    print(f"Binary representation: {CF.LIGHTGREEN_EX}{binary}{CF.RESET}")
                    decimal = int(binary, 2)
                    print(f"Corresponding decimal: {CF.LIGHTGREEN_EX}{decimal}{CF.RESET}")
                    input("\nPress ENTER to continue: ")
                    break
                else:
                    print("Invalid input! Enter a valid hexadecimal.")

        elif option == "6":
            clear()
            while True:
                length_str = input("Enter the length in cm: ")
                width_str = input("Enter the width in cm: ")
                height_str = input("Enter the height in cm: ")
                volume = calc_volume(length_str, width_str, height_str)
                if volume is not None:
                    clear()
                    print(f"Length: {length_str}, Width: {width_str}cm, Height: {height_str}")
                    print(f"Volume: {CF.LIGHTGREEN_EX}{volume}cm³{CF.RESET}")
                    input("\nPress ENTER to continue: ")
                    break
                else:
                    print("Invalid input. Enter valid dimensions.")

        elif option == "7":
            clear()
            country = input("Enter a country name: ")
            country_info(country)
            input("\nPress ENTER to continue.")

        elif option == "8":
            clear()
            joke = chuck()
            if joke is not None:
                print(f"{CF.LIGHTGREEN_EX}{joke}{CF.RESET}")
                input("\nPress ENTER to continue: ")
            else:
                print("Error bringing the joke to your face.")

        elif option == "9":
            clear()
            fact = random_fact()
            if fact is not None:
                print(f"{CF.LIGHTGREEN_EX}{fact}{CF.RESET}")
                input("\nPress ENTER to continue.")
            else:
                print("Error presenting a random fact :(")

        elif option == "10":
            print("Exiting program...")
            break

        else:
            print("Invalid input! Type in a number like '1' / '2' /...")

    except KeyboardInterrupt:
        print("\nUser interrupted the program. Exiting.")
        time.sleep(2)
        break
    except ValueError:
        print("\nInvalid input! Not a valid Integer")
    except Exception as e:
        print(f"\nError detected (Most likely solving the determinant): {e} ")
