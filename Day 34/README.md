# Counting Sort
Today, I learnt the concept of Counting Sort Algorithm.

## Illustration
![1](https://user-images.githubusercontent.com/114591698/204099333-1710645c-dc63-46bf-8f36-6a966bec192c.jpg)
* Now, store the count of each unique element in the count array
* If any element repeats itself, simply increase its count.

![2](https://user-images.githubusercontent.com/114591698/204099404-37bebc63-6e5d-407e-a95c-db53ef967e95.jpg)
* Here, the count of each unique element in the count array is as shown:
Index: 0 1 2 3 4 5 6 7 8 9<br>
Count: 0 2 2 0 1 1 0 1 0 0<br>
![3](https://user-images.githubusercontent.com/114591698/204099464-e0eadf8b-5097-45dd-8679-2b64aa688cb1.jpg)
* Modify the count array such that each element at each index stores the sum of previous counts.
Index:   0  1  2  3  4  5  6  7  8  9<br>
Count:  0  2  4  4  5  6  6  7  7  7<br>
* The modified count array indicates the position of each object in the output sequence.
* Find the index of each element of the original array in the count array. This gives the cumulative count.
![4](https://user-images.githubusercontent.com/114591698/204099501-d48888f1-db22-49ef-b557-3a215bf0c949.jpg)<br>

![5](https://user-images.githubusercontent.com/114591698/204099518-9e8176dd-b49c-419f-8e2f-ba781d93350e.jpg)
* Rotate the array clockwise for one time.
Index:  0 1 2 3 4 5 6 7 8 9 <br>
Count: 0 0 2 4 4 5 6 6 7 7<br>
![6](https://user-images.githubusercontent.com/114591698/204099537-b31081d2-cb2f-424b-9d1d-cc054a5d0ff9.jpg)
* Output each object from the input sequence followed by increasing its count by 1.
* Process the input data: {1, 4, 1, 2, 7, 5, 2}. The position of 1 is 0.
* Put data 1 at index 0 in output. Increase count by 1 to place next data 1 at an index 1 greater than this index.
![7](https://user-images.githubusercontent.com/114591698/204099551-6179f793-8d82-491b-be0a-ffc8b45c4958.jpg)
* After placing each element in its correct position, decrease its count by one.
