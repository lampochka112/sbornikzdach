from itertools import product

print("X\tY\tа) ¬X ∧ ¬Y\tб) X ∨ (¬X ∧ Y)\tв) (¬X ∧ Y) ∨ Y")
print("-" * 60)

for X, Y in product([True, False], repeat=2):
    expr_a = (not X) and (not Y)
    expr_b = X or ((not X) and Y)
    expr_c = ((not X) and Y) or Y
    
    print(f"{X}\t{Y}\t{expr_a}\t\t{expr_b}\t\t\t{expr_c}")