# Binary Search
Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.

## Algorithm
* Begin with the mid element of the whole array as a search key.
* If the value of the search key is equal to the item then return an index of the search key.
* Or if the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half.
* Otherwise, narrow it to the upper half.
* Repeatedly check from the second point until the value is found or the interval is empty.

## PseudoCode
![image](https://user-images.githubusercontent.com/114591698/211823234-46242714-7362-4404-afdd-57859c0f8e54.png)

## Illustration
![image](https://user-images.githubusercontent.com/114591698/211823402-680078dd-eac0-4230-bbfe-0600ea0c1c87.png)
