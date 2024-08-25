import time
from button_matrix import ButtonMatrix
from calculator import Calculator

row_pins = [7, 8, 9, 10]
col_pins = [11, 12, 13]

matrix = ButtonMatrix(row_pins, col_pins)
calc = Calculator()

def get_key_from_matrix(matrix):
    key_map = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['C', '0', '=']
    ]
    result = matrix.scan()
    for r in range(len(result)):
        for c in range(len(result[r])):
            if result[r][c] == 1:
                return key_map[r][c]
    return None

def main():
    while True:
        key = get_key_from_matrix(matrix)
        if key:
            calc.update(key)
            print(calc.get_display())
        time.sleep(0.1)

if __name__ == "__main__":
    main()
