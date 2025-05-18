from itertools import product

print("A\tB\tа) не A ∨ не B\tб) A ∧ (A ∨ не B)\tв) (не A ∨ B) ∧ B")
print("-" * 60)

for A, B in product([True, False], repeat=2):
    expr_a = (not A) or (not B)
    expr_b = A and (A or (not B))
    expr_c = ((not A) or B) and B
    
    print(f"{A}\t{B}\t{expr_a}\t\t{expr_b}\t\t\t{expr_c}")