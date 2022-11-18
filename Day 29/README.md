# Bubble Sort
Today, I learnt the Bubble Sort algorithm.

## Working of Bubble Sort
### Input:
arr[] = {5, 1, 4, 2, 8}

### First Pass: 

* Bubble sort starts with very first two elements, comparing them to check which one is greater.
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1. <br>
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4 <br>
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2 <br>
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.<br>

### Second Pass: 

* Now, during second iteration it should look like this:
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ) <br>
( 1 4 2 5 8 ) –> ( 1 2 4 5 8 ), Swap since 4 > 2 <br>
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) <br>
( 1 2 4 5 8 ) –>  ( 1 2 4 5 8 ) <br>

### Third Pass: 

* Now, the array is already sorted, but our algorithm does not know if it is completed.
* The algorithm needs one whole pass without any swap to know it is sorted.
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) <br>
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) <br>
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) <br>
( 1 2 4 5 8 ) –> ( 1 2 4 5 8 ) <br>

## Illustration
![bubble-sort1](https://user-images.githubusercontent.com/114591698/202614529-5432a7c9-c7c9-4305-8392-212d3b39179a.png)






