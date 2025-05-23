X = True
Y = False
Z = False

result_a = not X or not Y or not Z

result_b = (not X or not Y) and (X or Y)

result_c = (X and Y) or (X and Z) or (not Z)

print("а)", result_a)  
print("б)", result_b)  
print("в)", result_c)  