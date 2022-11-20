# Merge Sort
Today, I learnt about the merge sort algorithm.

## Working of merge sort:
To know the functioning of merge sort, lets consider an array arr[] = {38, 27, 43, 3, 9, 82, 10}
* At first, check if the left index of array is less than the right index, if yes then calculate its mid point<br>
![1](https://user-images.githubusercontent.com/114591698/202891930-c67a2bfd-b28c-406a-a354-0109e0fc35ee.jpg)

* Now, as we already know that merge sort first divides the whole array iteratively into equal halves, unless the atomic values are achieved. <br>
* Here, we see that an array of 7 items is divided into two arrays of size 4 and 3 respectively.<br>
![2](https://user-images.githubusercontent.com/114591698/202891950-8cbf53a4-9aec-495e-969b-2f66eeca2287.jpg)

* Now, again find that is left index is less than the right index for both arrays, if found yes, then again calculate mid points for both the arrays.<br>
![3](https://user-images.githubusercontent.com/114591698/202891965-f863aefe-d156-4a7a-b1cc-c0d4b87313a4.jpg)

* Now, further divide these two arrays into further halves, until the atomic units of the array is reached and further division is not possible.<br>
![4](https://user-images.githubusercontent.com/114591698/202891977-00078091-799e-4f2c-9ac4-86426fa2449f.jpg)

* After dividing the array into smallest units, start merging the elements again based on comparison of size of elements<br>
* Firstly, compare the element for each list and then combine them into another list in a sorted manner.<br>
![5](https://user-images.githubusercontent.com/114591698/202892015-ccec34ec-d821-4374-b96b-e4491e785719.jpg)

* After the final merging, the list looks like this:<br>
![6](https://user-images.githubusercontent.com/114591698/202892031-f6c84ed4-bf04-4ad9-af21-e995704e81a4.jpg)

