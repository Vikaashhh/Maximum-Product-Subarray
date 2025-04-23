# 💡 Day-11: Maximum Product Subarray

For Day-11 of the #gfg160 challenge, I tackled the classic problem of finding the **maximum product of a contiguous subarray**. This is one of those problems where brute force isn't feasible, and a smart linear-time solution really shines.

---

## 📌 Problem Statement

Given an array `arr` of integers (which may include negative numbers), find the **contiguous subarray** within the array that has the **largest product**, and return the product.

---

## 🤯 Why It’s Tricky

Unlike sum-based problems, multiplication has a twist:
- A negative number can **turn a minimum into a maximum** and vice versa.
- So, we track **both the current max and current min** at every step.

---

## 🧠 Approach & Explanation

1. Initialize `max_product`, `curr_max`, and `curr_min` with the first element.
2. Traverse the array from the second element:
   - If the number is negative, swap `curr_max` and `curr_min`.
   - Update:
     - `curr_max = max(num, curr_max * num)`
     - `curr_min = min(num, curr_min * num)`
   - Update `max_product = max(max_product, curr_max)`
3. Return `max_product`.

---

## 📊 Time & Space Complexity
Time Complexity: O(n)

Space Complexity: O(1)
---

## 📌 Sample Input/Output
Input:
```
Enter array elements: 2 3 -2 4
```
Output:
```
Maximum product subarray is: 6
```
---
## 📅 Challenge Tag
#gfg160 #geekstreak2025 #Day11
---
## ✨ Author
Curated by Vikash Joshi — Front-End Developer | UI/UX Designer | DSA Explorer 🚀
