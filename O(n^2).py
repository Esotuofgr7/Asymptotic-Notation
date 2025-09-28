def test(n):
    iteration = 0
    for i in range(n):
        for j in range(n):
            print("*", end="")
            iteration += 1
        print("")
    print("\nWhen n is", n, "iteration =", iteration)

# Run tests
test(5)
test(4)
test(3)

# Clarify the pattern
print("\nFor each value of n, the total iterations equal n squared (n^2).")
