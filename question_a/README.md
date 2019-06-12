# Question A


>Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8). 

My implementation of a solution for this problem is version_compare(str1, str2),
str1 and str2 are two tuples that contains two strings or numbers that can be converted to a float using float(n)
The function will return a boolean depending if the two lines overlap or not,
and will throw a value error if it is unable to decipher the numbers or if the inputs are not of the class tuple.

To run the test, run the command
>python -m unittest test_question_a.py