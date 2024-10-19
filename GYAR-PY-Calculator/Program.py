from Math import Math

if __name__ == "__main__":
    while True:
        exp = input("""Input format: val1 op val2, e.g., 2 * 4
Operators: +, -, *, /, ^
Enter a mathematical expression: """)
        print(Math.calculate(exp))
