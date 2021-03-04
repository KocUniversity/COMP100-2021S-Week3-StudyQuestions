## String Manipulation
### Alternating Characters

You are given a string containing characters **A** and **B** only. Your task is to change it into a string such that there are no matching adjacent characters. To do this, you are allowed to delete zero or more characters in the string.

Your task is to find the minimum number of required deletions.

**Example**
`s = AABAAB`
Remove an `A` at positions `0` and `3` to make `s = ABAB` in **2** deletions.

**Hint**
It would be useful to have a variable within your loop that stores the previous character, `prev`, and another variable to store the current character, `curr`. This lets you compare the two to see if they alternate. Then you can assign prev to be curr, `prev = curr`.


### Compare Strings

You are given two strings and you are expected to compare them. You should compare each character in the strings one by one. 

**Example**

Assume you are comparing strings, `s1 = 'abcde'` and `s2 = 'abbcd`, then, you should select the smaller one (appears earlier than the other one in the dictionary). In this case, you should select the second one.

**Explanation:** Assume we are using `i` as an indexing variable, which we will initialize to 0 and increment by one at each comparison we make.

i = 0, s1 and s2's first characters are both `'a'`, in this case, we should look at the following characters.

i = 1, s1 and s2's second characters are both `'b'`, in this case, we should look at the following characters.

i = 2, s1's third character is `'c' and s2's third character is `'b'`. Since `'b'` is smaller than  `'c'` (in python, you can directly compare `'b' < 'c'`), we will select the second string.

### Merge Strings

You are given two strings and you are expected to merge them into a new string. You should take one element from one string and one element from the other string, and then add them to the new string. You should apply this operation until the strings do not contain any other elements. What happens if the strings are not the same length?

**Example**

`s1 = 'aaaa'` and `s2 = 'bbbb'`, the output should be `'abababab'`. 


## Bisection Search

### Root-finding

In mathematics, [the bisection method](https://en.wikipedia.org/wiki/Bisection_method#Example:_Finding_the_root_of_a_polynomial) can be used for root-finding for any continuous function, i.e. where the function is zero. Initially, we need to define the search region as an interval in which the function changes sign, and therefore must contain a root. This corresponds to finding two values with opposite signs.

For example, for the function

`f(x) = x^3 - x - 2`

these two numbers can be `a = 1` and `b = 2` because `f(1) = -2` and `f(2) = 4`. Because the function is continuous, there must be a root within the interval `[1, 2]`.


For this continuous function `f` and the interval `[a, b]`, we will perform the following steps at each iteration to find the root approximately:

* Calculate `c` as the midpoint of the interval, `c = (a+b) / 2` 
* Calculate the function value at the midpoint, `f(c)`.
* If convergence is satisfactory (that is, `c - a` is sufficiently small, or `|f(c)|` is sufficiently small), report `c` as the solution and stop iterating.
* Otherwise, check the sign of `f(c)` and replace either `a` or `b` with `c` so that there is a zero crossing within the new interval. In other words, replace `a` with `c` if `f(c)` is negative, otherwise, replace `b` with `c`.

**Hint**: There can be problems with finite precision, so you might need additional convergence tests or limits to the number of iterations. For this purpose, count the number of iterations and stop when a pre-defined maximum number of iterations is reached, e.g. something like 10000.