# Heap
Heap data structure is mainly used to represent a priority queue. In Python, it is available using the “heapq” module. The property of this data structure in Python is that each time the smallest heap element is popped(min-heap). Whenever elements are pushed or popped, heap structure is maintained. The heap[0] element also returns the smallest element each time.

## Operations
* **The heapify(iterable):** This function is used to convert the iterable into a heap data structure. i.e. in heap order.
* **heappush(heap, ele):** This function is used to insert the element mentioned in its arguments into a heap. The order is adjusted, so that heap structure is maintained.
* **heappop(heap):** This function is used to remove and return the smallest element from the heap. The order is adjusted, so that heap structure is maintained.
* **heappushpop(heap, ele):** This function combines the functioning of both push and pop operations in one statement, increasing efficiency. Heap order is maintained after this operation.
* **heapreplace(heap, ele):** This function also inserts and pops elements in one statement, but it is different from the above function. In this, the element is first popped, then the element is pushed. i.e, the value larger than the pushed value can be returned. heapreplace() returns the smallest value originally in the heap regardless of the pushed element as opposed to heappushpop().
* **nlargest(k, iterable, key = fun):** This function is used to return the k largest elements from the iterable specified and satisfy the key if mentioned.
* **nsmallest(k, iterable, key = fun):** This function is used to return the k smallest elements from the iterable specified and satisfy the key if mentioned.

## Program Output
```
The created heap is : [1, 3, 9, 7, 5]
The modified heap after push is : [1, 3, 4, 7, 5, 9]
The popped and smallest element is : 1
```
