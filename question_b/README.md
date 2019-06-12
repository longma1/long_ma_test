# Question B

>The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.

I'm assuming the version string is not limited to 2 integers, this implementation accepts any number of integers
separated by periods as periods strings, but expect the two version string to be consistent in number of integers.
IE comparing 8.8.1.3 and 8.2.3.1 will work, but 1.2 and 2.3.1 will result in the function throwing an exception.

The function first converts strings to list of integers, and then looks through the list of version integers
until it finds which string is greater than or returns they are equal if it finished traversing the list. Worse case runtime of O(n)


To run the test, run the command
>python -m unittest test_question_b.py