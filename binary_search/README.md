Find the First True in a sorted Boolean array

An array of boolean values is divided into two sections: The left section consists of all `false`, and the right section consists of all `true`. Find the First True in a Sorted Boolean Array of the right section, i.e., **the index of the first `true` element**. If there is no `true` element, return -1.

Input: `arr = [false, false, true, true, true]`

Output: `2`

Explanation: The first `true`'s index is 2.


- Find the mid value in the array. The mid index is 2 which is the element True.
- This might be the index of the first True element or it might not be. There might be another true to the left. In this case we will keep a boundary_index variable that holds the index of the True element. Next we discard all elements right of the mid index and narrow our search to mid - 1. We will check to see if there is any other True and if so we will update the boundary index.
- In the case where the mid is False. We discard all elements left of the mid including the mid. We narrow our search to mid + 1. 

```other
from typing import List

def find_boundary(arr: List[bool]) -> int:
    left = 0
    right = len(arr) - 1
    
    boundary_index = -1
    
    while(left <= right):
        mid = (left + right) //2
        
        if arr[mid] == False:
            left = mid + 1
        elif arr[mid] == True:
            boundary_index = mid
            right = mid - 1
    return boundary_index
```


### When to use binary search


Binary search works beyond sorted arrays. You can use binary search **whenever you make a binary decision to shrink the search range**.

## Monotonic Function


A monotonic function is a function that is predictable either **decreasing** or **increasing**. 

A sorted array is monotonic because the value increases or stays the same as the index increases.

![image](https://res.craft.do/user/full/34de0a68-4b4d-ecb0-6c1b-0c3cfda2286e/doc/B14B0840-4108-4CB0-8FBF-FB4889E0EF0D/78433653-FF07-4DBE-97CD-D7099F7D1391_2/w851EclQtJu46y0aB7BIFWHhDaZbkgXG4VZbQwyJKq4z/Image.png)

The precondition for binary search is to find a monotonic function `f(x)` that either returns True or False

We will call the function feasible to signify the element at the current index is feasible(True) or not (False to meet the problem constraints.

In our case above the feasible function would be `arr[mid] == True`

## First Element Not Smaller than Target


Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is *larger than or equal* to the target. Assume that it is guaranteed to find a satisfying number.

The feasible function is `arr[mid] >= target`

![](https://res.craft.do/user/preview/34de0a68-4b4d-ecb0-6c1b-0c3cfda2286e/doc/B14B0840-4108-4CB0-8FBF-FB4889E0EF0D/E4F5DD61-EB73-40B2-BCA4-9C54314CA5FD_1/pCc2rUToB5DFkxrdxoF35x76KPlxyEziRm8OmxmGb80z/Drawing.jpg)



```other
from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    boundary_index = -1
    
    while(left <= right):
        mid = (left + right) // 2
        
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index
```


## Find the Minimum in Rotated Sorted Array


A sorted array of **unique** integers was rotated at an unknown pivot. For example, `[10, 20, 30, 40, 50]` becomes `[30, 40, 50, 10, 20]`. Find the index of the minimum element in this array.

Input: `[30, 40, 50, 10, 20]`

Output: `3`

Explanation: The smallest element is 10, and its index is 3.

At first glance, it seems there no way to do it in less than linear time because the array is not sorted. But remember binary search can work beyond sorted arrays, **as long as there is a binary decision we can use to shrink the search range.**

In the figure below we can notice a pattern. Numbers are divided into two sections: numbers larger than the last element and numbers less than the last element.

![image](https://res.craft.do/user/full/34de0a68-4b4d-ecb0-6c1b-0c3cfda2286e/doc/B14B0840-4108-4CB0-8FBF-FB4889E0EF0D/D5A5A442-83CF-4996-96BF-9A11FECFBAA2_2/y9K8zmedXU5VY9pxvhMbovRrDOCdUlgI2z5FUOkA1i4z/Image.png)

We can apply a feasible function of < the last element and get the boolean array that characterized the two sections

![image](https://res.craft.do/user/full/34de0a68-4b4d-ecb0-6c1b-0c3cfda2286e/doc/B14B0840-4108-4CB0-8FBF-FB4889E0EF0D/C2CD62DD-953A-4C1C-B1BE-8BE411836790_2/gErzwX123tcenhRldcrKXgWWcGKQrydCTBSKbieCgJ0z/Image.png)

Now the problem is reduced to finding the first True element in a boolean array. If midpoint is element 50 than we know that 50 < 20 is False. Thus we disregard all elements left of the mid and focus on elements right of mid.

![](https://res.craft.do/user/preview/34de0a68-4b4d-ecb0-6c1b-0c3cfda2286e/doc/B14B0840-4108-4CB0-8FBF-FB4889E0EF0D/BC8DB1B8-9B0F-4460-946D-8E0C08569C21_1/lcROOxEZCvXa0pEIdKJl8wHeK0ScxXw0zxygE3chPF0z/Drawing.jpg)



## Peak of a Mountain Array


A mountain array is defined as an array that


- has at least 3 elements
- has an element with the largest value called "peak", with index `k`. The array elements strictly increase from the first element to `A[k]`, and then strictly decrease from `A[k + 1]` to the last element of the array. Thus creating a "mountain" of numbers.

Find the index of the peak element. Assume there is only one peak element.

Input: `0 1 2 3 2 1 0`

Output: `3`

Explanation: The largest element is 3, and its index is 3.

The array strictly increases until the peak element and then strictly decreases. The monotonicity is a strong sign that we can use binary search to find the peak element.

To use binary search we need to find a feasible function that returns false for elements up until the peak and true from the peak to the end.

We already know the array strictly decreases from the peak element to the last element. We can try to use a feasible function of `arr[i] > arr[i+1]` to return True for elements from the peak to the last element. Also it returns False from the first element to the peak element.

![image](https://res.craft.do/user/full/34de0a68-4b4d-ecb0-6c1b-0c3cfda2286e/doc/B14B0840-4108-4CB0-8FBF-FB4889E0EF0D/E430DE1A-5876-457C-AA25-93066AE0D361_2/5HzG43vYxeVrvZRXkpAddnrHtpBQhnPXDANgwfynGVsz/Image.png)

```other
from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    boundary_index = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid+1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index
```


## Newspapers


You've begun your new job to organize newspapers. Each morning, you are to separate the newspapers into smaller piles and assign each pile to a co-worker. This way, your co-workers can read through the newspapers and examine their contents simultaneously.

Each newspaper is marked with a read time to finish all its contents. A worker can read one newspaper at a time, and, when they finish one, they can start reading the next. Your goal is to minimize the amount of time needed for your co-workers to finish all newspapers. Additionally, the newspapers came in a particular order, and you must not disarrange the original ordering when distributing the newspapers. In other words, you cannot pick and choose newspapers randomly from the whole pile to assign to a co-worker, but rather you must take a subsection of consecutive newspapers from the whole pile.

What is the minimum amount of time it would take to have your coworkers go through all the newspapers? That is, if you optimize the distribution of newspapers, what is the longest reading time among all piles?

### Examples


#### Example 1:


#### Input: `newspapers_read_times = [7,2,5,10,8], num_coworkers = 2`


#### Output: `18`


#### Explanation:


Assign first `3` newspapers to one coworker then assign the rest to another. The time it takes for the first `3` newspapers is `7 + 2 + 5 = 14` and for the last `2` is `10 + 8 = 18`.

#### Example 2:


#### Input: `newspapers_read_times = [2,3,5,7], num_coworkers = 3`


#### Output: `7`


#### Explanation:


Assign `[2, 3]`, `[5]`, and `[7]` separately to workers. The minimum time is `7`.

The reason binary search is applicable is because of the monotonic nature of the problem. What do we mean by monotonic here? If a given time t is feasible for num_coworkers to finish all the newspapers, then any time greater than t will be feasible. This is because if coworkers can complete reading in a shorter amount of time, they can obviously also complete it if given more time. This forms a monotonic relationship, which is a crucial characteristic for binary search applicability.

Essentially, our problem exhibits two sequences:


1. A sequence of infeasible times, followed by
2. A sequence of feasible times.

The transition between these two times is what we ain for find using binary search.

### Observations

- The smallest time any coworker would take is equal to the time taken to read the longest newspaper
- The largest time would be if only one person reads all the newspapers
- The optimal time lies between these two values

### Feasibility Check: Intuitive Explanation


The feasibility check is how we would distribute the  newspapers to coworkers under a hypothetical maximum reading time, mid. Each co-worker reads for mid amount of time. Once their reading time mid is completed the next coworker steps in and reads the remaining papers for mid amount of time. If all newspapers are completed before we reach the end of the coworkers than that means that mid time is feasible, otherwise it is not feasible.

![image](https://res.craft.do/user/full/34de0a68-4b4d-ecb0-6c1b-0c3cfda2286e/doc/B14B0840-4108-4CB0-8FBF-FB4889E0EF0D/775DBFF0-F07E-4EB1-8BC9-8E83D91F2A08_2/Rny1P2LRCabwdEKeRctbtK37ntutyxKxrCjoiQVx2qAz/Image.png)

## Binary Search Speedrun


You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return *the single element that appears only once*.

Your solution must run in `O(log n)` time and `O(1)` space.

**Example 1:**

**Input:** nums = [1,1,2,3,3,4,4,8,8] **Output:** 2

**Example 2:**

**Input:** nums = [3,3,7,7,10,11,11] **Output:** 10

What do we know about the pairs of elements appearing twice? Let's analyze the pattern. Let's denote **s** as the non-duplicate pair. If we look at the array [1,1,2,3,3,4,4,8,8]. What do we notice about the pairs before **s** and the pairs after **s**. Looking at the pair before s we see that the first part of the pair is an even index lets denote it as **e**. The second part of the pair is **e + 1** which is odd. Examining the pair after s, its the reverse. The first part is odd lets denote it as **o** and the second is **o+1** which is even.

Now what would be the feasible function here? Assuming we want to check the left side of s


- if the mid is even. We check if `nums[idx] != nums[idx+1]` 
	- Remember if we land at an even that means that it is the first part of the pair. We would compare it to the second part of the pair
- if mid is odd we check if `nums[idx] != nums[idx-1]` 
	- Remember if we land at an odd index this means its the second part of the pair and we compare to the first part of the pair.
- These two conditional checks will tell us if the non-duplicate values exists at mid or to the left of it. How? If either of the above conditionals returns true meaning the pairs aren't matching this means somewhere on the left there is a non-duplicate that is disrupting the pattern.

Let's walk through an example: `[1,1,2,3,3,4,4,8,8]`


- mid = 4. This is an even index. Check nums[mid] != nums[mid+1]. 3 != 4. Feasible function returns true
- This means the non-duplicate element is mid or to the left of mid. Let's save mid to a variable called ans. mid is potentially the non-duplicate we just don't know for sure yet. 
- Now since we know that non-duplicate must exist on the left. We disregard everything on the right.
- `[1, 1, 2, 3]` is the what we now need to look at. The mid here is index 1. Since index 1 is an odd index. We check if nums[mid] != nums[mid-1]. 1 != 1. It returns false. This means the non-duplicate element is not on the left. We have to now check the right.
- `[2,3]`
