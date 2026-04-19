import pdb


print("Debugging Demonstration Program")

def print_pattern(rows):
    for i in range(rows):
        pdb.set_trace()
        for j in range(i + 1):
            print("*", end="")
        print()

print_pattern(5)