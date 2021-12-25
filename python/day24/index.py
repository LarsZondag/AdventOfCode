#%%
with open('input.txt') as f:
    data = [x.split() for x in f.read().splitlines()]
data
# %%

for largest_nr in reversed(range(10**14)):
    model_nr = [int(x) for x in str(largest_nr).zfill(14)]
    if 0 in model_nr: continue

    wxyz = dict(w=0, x=0, y=0, z=0)

    for instr, *vars in data:
        if instr == "inp":
            wxyz[vars[0]] = model_nr.pop(0)
            continue
        a, b = vars
        val_a = wxyz[a]
        try:
            val_b = wxyz[b]
        except:
            val_b = int(b)
        try:
            # Add the value of a to the value of b, then store the result in variable a.
            if instr == "add":
                wxyz[a] += val_b 
            # Multiply the value of a by the value of b, then store the result in variable a.
            elif instr == "mul":
                wxyz[a] *= val_b 
            # Divide the value of a by the value of b, truncate the result to an integer, then store the result in variable a. (Here, "truncate" means to round the value toward zero.)
            elif instr == "div":
                wxyz[a] //= val_b 
            # Divide the value of a by the value of b, then store the remainder in variable a. (This is also called the modulo operation.)
            elif instr == "mod":
                wxyz[a] %= val_b 
            # If the value of a and b are equal, then store the value 1 in variable a. Otherwise, store the value 0 in variable a.
            elif instr == "eql":
                wxyz[a] = int(val_a == val_b )
        except ZeroDivisionError:
            continue
    if wxyz['z'] == 0:
        break

print(largest_nr)

# %%
