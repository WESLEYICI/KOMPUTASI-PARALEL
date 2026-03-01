# misd_voting.py
# MISD - N Version Programming Example

# Input data (same input for all algorithms)
D = 5

# Algorithm A
def algorithmA(D):
    return D * D   # kuadrat

# Algorithm B
def algorithmB(D):
    return pow(D, 2)   # kuadrat dengan cara lain

# Algorithm C
def algorithmC(D):
    return D ** 2   # kuadrat dengan operator lain

# Run multiple programs
result1 = algorithmA(D)
result2 = algorithmB(D)
result3 = algorithmC(D)

print("Result A =", result1)
print("Result B =", result2)
print("Result C =", result3)

# Majority voting
if result1 == result2 or result1 == result3:
    final_result = result1
elif result2 == result3:
    final_result = result2
else:
    final_result = "ERROR - No consensus"

print("Final Result =", final_result)