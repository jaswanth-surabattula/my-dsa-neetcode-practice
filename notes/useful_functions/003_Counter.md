# Python `Counter` Class (collections)

The `Counter` is a specialized dictionary subclass used for counting hashable objects. It is an unordered collection where elements are stored as **dictionary keys** and their counts are stored as **dictionary values**.

---

## 1. Syntax & Initialization
To use it, you must import it from the `collections` module.
```python
from collections import Counter

# From an iterable
c = Counter(['a', 'b', 'c', 'a', 'b', 'a']) 
# Output: Counter({'a': 3, 'b': 2, 'c': 1})

# From a string
c = Counter("gallad") 
# Output: Counter({'a': 2, 'l': 2, 'g': 1, 'd': 1})

# From keyword arguments
c = Counter(cats=4, dogs=8)
```

---

## 2. Key Features

### A. Missing Keys
Unlike a standard dictionary, `Counter` does not raise a `KeyError`. If an item is not found, it returns `0`.
```python
c = Counter(['apple', 'apple'])
print(c['orange']) # Output: 0
```

### B. `most_common(n)`
Returns a list of the `n` most common elements and their counts from the most common to the least.
```python
c = Counter('abracadabra')
print(c.most_common(3))
# Output: [('a', 5), ('b', 2), ('r', 2)]
```

### C. `elements()`
Returns an iterator over elements repeating each as many times as its count.
```python
c = Counter(a=2, b=1)
print(list(c.elements())) 
# Output: ['a', 'a', 'b']
```

---

## 3. Mathematical Operations
`Counter` objects support addition, subtraction, and set operations (intersection and union).

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)

print(c + d) # Addition: Counter({'a': 4, 'b': 3})
print(c - d) # Subtraction (keeps only positive results): Counter({'a': 2})
print(c & d) # Intersection (min of counts): Counter({'a': 1, 'b': 1})
print(c | d) # Union (max of counts): Counter({'a': 3, 'b': 2})
```

---

## 4. Common Use Cases
* **Frequency Analysis**: Finding the most repeated word in a text.
* **Anagram Detection**: Two strings are anagrams if `Counter(str1) == Counter(str2)`.
* **Inventory Tracking**: Easily adding and removing quantities from a list of items.

---

## 5. Summary Table

| Method | Description |
| :--- | :--- |
| `c.update(iterable)` | Adds counts from another iterable. |
| `c.subtract(iterable)` | Subtracts counts from another iterable. |
| `c.total()` | Returns the sum of all counts (Python 3.10+). |
| `c.clear()` | Resets all counts to zero. |

---

> **Tip:** `Counter` is significantly faster than manually looping through a list to build a frequency dictionary.
