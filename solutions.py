## String Manipulation

# Alternating Characters
s1 = "BAAABBAABABA"
s2 = ""
counter = 0
for i in range(len(s1)):
  if i == 0:
    prev = s1[i]
    s2 += prev
  else:
    curr = s1[i]
    if curr == prev:
      counter += 1
    else:
      prev = curr
      s2 += curr

print("My original string was",s1)
print("My manipulated string is",s2)
print("The manipulation required",counter, "deletions")

# Compare Strings
s1 = 'abccea'
s2 = 'abcdea'
smaller = -1
i = 0
while i < len(s1) and i < len(s2):
  if s1[i] < s2[i]:
    smaller = s1 # s1 is the smaller one
    break
  elif s2[i] < s1[i]:
    smaller = s2 # s2 is the smaller one
    break
  else:
    # characters are the same, look at the following characters
    i += 1 # increment the indexing variable
if i == len(s1) and i == len(s2):
  # there are no other characters in s1 and s2, they should be the same strings
  smaller = -1 # equal
elif i == len(s1):
  # there are no other characters in s1, it should be smaller one
  smaller = s1
elif i == len(s2):
  # there are no other characters in s2, it should be smaller one
  smaller = s2

print('smaller string is', smaller)

# Merge Strings
s1 = 'aaaaaaa'
s2 = 'bbbbcccdddd'
out = ''
i = 0
while i < len(s1) and i < len(s2):
  out += s1[i] + s2[i]
  i += 1
while i < len(s1):
  out += s1[i]
  i += 1
while i < len(s2):
  out += s2[i]
  i+=1

print(out)

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
while i < max_iter:
  # calculate c as the midpoint of the interval 
  c = (a + b) / 2

  # calculate the function value at the midpoint
  f_c = c ** 3 - c - 2

  # stop if convergence is satisfactory
  if abs(f_c) < eps or c-a < eps:
    print('Solution is found at c =', c)
    print('After i =', i, 'number of iterations.')
    break

  # increment the number of iterations
  i += 1

  # update the search region
  if f_c < 0:
    a = c
  else:
    b = c

if i == max_iter:
  print('Solution is not found.')