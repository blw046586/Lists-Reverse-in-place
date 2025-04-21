# Lists-Reverse-in-place
Reversing a list is a common task. One approach copies to a second list in reverse, then copies the second list back to the first. However, to save space, reversing a list without using a second list is sometimes preferable. Write a function that reverses a given list, without using a second list. The program's input is the length of the list, followed by the list itself.

Ex: If the input is

4
2
5
9
7
The output is

7 9 5 2
Hints:

Use this approach: Swap the first and last elements, then swap the second and second-to-last elements, etc.

Stop when you reach the middle; else, you'll reverse the list twice, ending with the original order.

Think about the case when the number of elements is even, and when odd. Make sure your code handles both cases.
