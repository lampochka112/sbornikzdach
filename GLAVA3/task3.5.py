
from itertools import product

for A, B in product([True, False], repeat=2):
    expr_a = not (A and B)
    expr_b = not A or B
    expr_c = A or not B

    print(f"A = {A}, B = {B}:")
    print(f"а) не (A и B) = {expr_a}")
    print(f"б) не A или B = {expr_b}")
    print(f"в) A или не B = {expr_c}")
    print("-" * 30)