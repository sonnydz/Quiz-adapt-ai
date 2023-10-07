import csv

data = [
    ["question", "choice_A", "choice_B", "choice_C", "choice_D", "correct_answer", "difficulty_level"],
    ["What is the sum of 2 + 2?", 3, 4, 5, 6, 4, "easy"],
    ["Solve the equation 3x - 7 = 8.", 5, 6, 7, 8, 5, "medium"],
    ["What is the square root of 25?", 4, 5, 6, 7, 5, "medium"],
    ["Calculate the area of a rectangle with length 8 and width 5.", 30, 35, 40, 45, 40, "hard"],
    ["Factorize the expression 2x^2 + 6x + 4.", "(x + 2)(2x + 2)", "(x + 1)(2x + 4)", "(2x + 1)(x + 2)", "(2x + 2)(x + 2)", "(x + 2)(2x + 2)", "hard"]
]

csv_file_path = "questions.csv"

with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f'Data has been written to {csv_file_path}')
