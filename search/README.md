# Search Algorithms

This directory contains search algorithms and their respective implemented tests.

#### Contents:
- [Complexity Table](#complexity-table)
- [Linear Search](#linear-search)
- [Binary Search](#binary-search)

## Complexity Table
Algorithm     | Best Case | Average Case | Worst Case | Space Complexity
------------- | --------- | ------------ | ---------- | ----------------
Linear Search | Ω(1)      | Θ(N)         | Ο(N)       | Ο(1)
Binary Search | Ω(1)      | Θ(log(N))    | Ο(log(N))  | Ο(1)


## Linear Search

This algorithm steps through the entirety of a list until it either finds the given value to search
for or reaches the end of the list. This is not nearly as effecient as the
[Binary Search](#binary-search) due to the fact it evaluates each part of the list. It does not rely
 on the list to be sorted.

## Binary Search

This algorithm searches through a sorted list for a given value. This relies on the list to be
sorted. It splits the list it searches into sub-lists, guaging each middle-position's value against
the one it's searching for. If the value it is searching for is lower than the list's middle value,
it searches the left half of the list. If it is higher, it searches the right. When the list becomes
one value long and the value to search for is not it, the search ends unsuccessfully. Due to how
massive the search lists can be, it is commonly implemented recursively.
