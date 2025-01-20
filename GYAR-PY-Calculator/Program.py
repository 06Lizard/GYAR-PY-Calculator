from Math import Math
import time

if __name__ == "__main__":
    while True:
        exp = input("""Input format: val1 op val2, e.g., 2 * 4
Operators: +, -, *, /, ^
Enter a mathematical expression: """)
        start_time = time.perf_counter()
        ans = Math.calculate(exp)
        end_time = time.perf_counter()
        duration = (end_time - start_time) * 1_000_000 # convert to micro sec
        print(f"\t{exp} = {ans}\n\t{duration:.2f} microseconds\n")
