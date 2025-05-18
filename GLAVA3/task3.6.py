from itertools import product

print("X\tY\tа) не (X или Y)\tб) не X и Y\tв) X и не Y")
print("-"*50)

for X, Y in product([True, False], repeat=2):
    expr_a = not (X or Y)
    expr_b = (not X) and Y
    expr_c = X and (not Y)
    
    print(f"{X}\t{Y}\t{expr_a}\t\t{expr_b}\t\t{expr_c}")