# Python Set Cheat Sheet

In Python, a `set` is an unordered collection of unique elements. It is highly optimized for membership testing—checking if an item exists in a set is $O(1)$, whereas checking in a list is $O(n)$.

---

## 1. Modifying Elements
These methods change the set in place.

| Method | Description | Example |
| :--- | :--- | :--- |
| `add(x)` | Adds element `x` to the set. | `s.add(5)` |
| `update(iterable)` | Adds multiple elements from another collection. | `s.update([1, 2, 3])` |
| `remove(x)` | Removes `x`; raises **KeyError** if `x` is missing. | `s.remove(10)` |
| `discard(x)` | Removes `x`; **does nothing** if `x` is missing. | `s.discard(10)` |
| `pop()` | Removes and returns a random element. | `val = s.pop()` |
| `clear()` | Removes all elements. | `s.clear()` |

---

## 2. Mathematical Operations
Sets excel at finding relationships between groups of data.



[Image of Venn diagrams showing set union, intersection, and difference]


| Operation | Method | Operator | Result |
| :--- | :--- | :--- | :--- |
| **Union** | `s1.union(s2)` | `s1 \| s2` | All items from both sets. |
| **Intersection** | `s1.intersection(s2)` | `s1 & s2` | Items common to both. |
| **Difference** | `s1.difference(s2)` | `s1 - s2` | Items in `s1` but not `s2`. |
| **Sym. Difference** | `s1.symmetric_difference(s2)` | `s1 ^ s2` | Items in one or the other, but not both. |

---

## 3. Comparison Methods (Booleans)
| Method | Operator | Description |
| :--- | :--- | :--- |
| `issubset(other)` | `s1 <= s2` | Returns `True` if `s2` contains all items of `s1`. |
| `issuperset(other)` | `s1 >= s2` | Returns `True` if `s1` contains all items of `s2`. |
| `isdisjoint(other)` | (none) | Returns `True` if the sets have **zero** common items. |

---

## 4. Key Differences: Set vs. Dictionary
Since you asked about the difference earlier, here is a quick visual breakdown:

| Feature | Set (`s = {1, 2}`) | Dictionary (`d = {1: "a"}`) |
| :--- | :--- | :--- |
| **Structure** | Keys only. | Key-Value pairs. |
| **Duplicates** | Not allowed. | Duplicate keys not allowed (values can be). |
| **Indexing** | No (unordered). | By Key. |
| **Common Use** | Membership tests, removing duplicates. | Mapping data, counting, databases. |



---

## 5. Performance (Big O)
Sets use a **Hash Table** under the hood, making them incredibly fast for large datasets.

* **Add/Remove/Lookup:** $O(1)$ average.
* **Space:** $O(n)$ where $n$ is the number of elements.
