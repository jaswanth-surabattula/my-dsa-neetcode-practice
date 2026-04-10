# Python `sorted()` Function

The `sorted()` function returns a new sorted list from the items in any iterable (list, tuple, dict, string, etc.). Unlike `.sort()`, which modifies the original list in place, `sorted()` leaves the original data untouched.

---

## 1. Syntax
```python
sorted(iterable, key=None, reverse=False)
```
* **iterable**: The sequence (list, tuple, string) or collection (dictionary, set) to be sorted.
* **key** (Optional): A function that serves as a key for the sort comparison (e.g., `len`, `str.lower`).
* **reverse** (Optional): A boolean value. If `True`, the list is sorted in descending order.

---

## 2. Basic Usage

### A. Numbers and Strings
```python
nums = [4, 1, 3, 2]
print(sorted(nums)) 
# Output: [1, 2, 3, 4]

chars = "python"
print(sorted(chars))
# Output: ['h', 'n', 'o', 'p', 't', 'y']
```

### B. Descending Order
```python
nums = [1, 10, 5, 20]
print(sorted(nums, reverse=True))
# Output: [20, 10, 5, 1]
```

---

## 3. Advanced Sorting with `key`
The `key` parameter is extremely powerful for sorting complex data or using custom logic.

### A. Sorting by Length
```python
words = ['banana', 'pie', 'apple', 'strawberry']
print(sorted(words, key=len))
# Output: ['pie', 'apple', 'banana', 'strawberry']
```

### B. Sorting a List of Tuples/Objects
Useful for sorting data based on a specific attribute.
```python
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]

# Sort by age (the second element in the tuple)
sorted_students = sorted(students, key=lambda x: x[1])
# Output: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
```

---

## 4. `sorted()` vs `.sort()`

| Feature | `sorted(list)` | `list.sort()` |
| :--- | :--- | :--- |
| **Return Value** | Returns a **new** list. | Returns `None`. |
| **Original List** | Remains **unchanged**. | Modified **in-place**. |
| **Flexibility** | Works on **any iterable**. | Only works on **lists**. |

---

## 5. Performance Note
Python uses an algorithm called **Timsort** for `sorted()`. 
* **Time Complexity**: $O(n \log n)$ in the worst case.
* **Stability**: It is a "stable" sort, meaning if two records have equal keys, their original order is preserved.

---

> **Tip:** When sorting dictionaries, `sorted(my_dict)` returns a sorted list of the **keys**. To sort by values, use `sorted(my_dict.items(), key=lambda item: item[1])`.
