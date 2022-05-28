def Fibonacci(NthTerm):
    if (NthTerm == 1 or NthTerm == 2):
        return 1 # Challenge defines 1st and 2nd term as == 1
    else:  # recursive definition of Fib term
        return Fibonacci(NthTerm-1) + Fibonacci(NthTerm-2)

FirstTerm = 0 # For scope to include Term in scope of print on line 13
for Term in range(1, 1000): # Arbitrary range
    FibValue = str(Fibonacci(Term)) # Convert integer to string for len()
    if len(FibValue) == 7:
        FirstTerm = Term
        break # Stop there
    else:
        continue # Go to next number
print("The first term in the\nFibonacci sequence to\ncontain 7 digits\nis the", str(FirstTerm)+".", "term")
    
    
