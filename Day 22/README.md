# Arrays
Today, I learnt about the concept of sub arrays.

## Task
Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.<br>
Note: There may be more than one subarray with sum as the given sum, print first such subarray. 

## Example
```
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Output: Sum found between indexes 2 and 4
Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33
```

## Input Format
An integer n to tell the length of array, A array of length n and an integer sum to find the sum in subarray.

## Test Cases
* **Case 1**

Input
```
Enter the number of elements in the array: 7
Enter the elements: 
1
4
0
0
3
10
5
Enter the sum to be found: 7
```
Output
```
Sum found between indexes 1 and 4
```

* **Case 2**

Input
```
Enter the number of elements in the array: 2
Enter the elements: 
1
4
Enter the sum to be found: 0
```
Output
```
No subarray found
```
