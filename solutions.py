## String Manipulation

# Alternating Characters
s1 = "BAAABBAABABA"
s2 = ""
counter = 0


print("My original string was", s1)
print("My manipulated string is", s2)
print("The manipulation required", counter, "deletions")

#####################################
# Compare Strings
s1 = 'abccea'
s2 = 'abcdea'
smaller = -1
i = 0


print('smaller string is', smaller)

#####################################
# Merge Strings
s1 = 'aaaaaaa'
s2 = 'bbbbcccdddd'
out = ''
i = 0


print(out)

#####################################
# Bisection Search for Root-finding
eps = 1e-5
max_iter = 10000

# define the search region as an interval in which the function changes sign
a = 1
b = 2
f_a = a ** 3 - a - 2
f_b = b ** 3 - b - 2
print('This needs to be negative f_a =', f_a)
print('This needs to be positive f_b =', f_b)

i = 0


if i == max_iter:
  print('Solution is not found.')
