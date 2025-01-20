from math import nan
import operator

class Math:
    @staticmethod
    def add(addend, addend2):
        return addend + addend2

    @staticmethod
    def sub(minuend, subtrahend):
        return minuend - subtrahend

    @staticmethod
    def multi(multiplicand, multiplicator):
        return multiplicand * multiplicator

    @staticmethod
    def divi(dividend, divisor):
        if divisor == 0:
            return nan
        return dividend / divisor

    @staticmethod
    def pow(base, power):
        return base**power

    @staticmethod
    def sqrt(radicand):
        if (radicand < 0):
            return nan
        return radicand**0.5

    @staticmethod
    def root(radicand, index):
        if radicand < 0 and index % 2 == 0:
            return nan
        return radicand**(1/index)

    @staticmethod
    def abs(value):
        if (value < 0):
            return 0-value
        return value

    @staticmethod
    def calculate(exp):
        exp = exp.replace(" ", "")
        operators = '+-*/^'
        
        try:
            for op in operators:
                if op in exp:
                    parts = exp.split(op)
                    if len(parts) != 2:
                        return "Invalid expression"
                    
                    operand1 = float(parts[0])
                    operand2 = float(parts[1])

                    operations = {
                        '+': Math.add,
                        '-': Math.sub,
                        '*': Math.multi,
                        '/': Math.divi,
                        '^': Math.pow,
                    }

                    return operations[op](operand1, operand2)
        except Exception as e:
            return float('nan')