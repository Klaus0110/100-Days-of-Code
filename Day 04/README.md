# Recursion [factorial of a number]

Today, we are learning about an algorithmic concept called recursion.

## Task
Calculate the factorial of the number 

## Example

Consider the following steps. After the recursive calls from step 1 to 3, results are accumulated from step 3 to 1.

* _factorial_(3) = 3 x _factorial_(2) = 3 x 2 = 6
* _factorial_(2) = 2 x _factorial_(1) = 2 x 1 = 2
* _factorial_(1) = 1
  

### Input Format
  
  A single integer, _n_ (the argument to pass to factorial).

### Constraints
  * 0 < n < 10 <sup>3</sup>
  
### Test Cases
_ _ _ _

* **Case 1**

Input
```bash
  Enter any number : 75
```
Output
```bash
  24809140811395398091946477116594033660926243886570122837795894512655842677572867409443815424000000000000000000
```


* **Case 2**

_Input_
```zsh
  Enter any number : -1
```

_Output_

```bash
  Invalid Number
```
