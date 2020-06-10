# Sorting Algorithms

This directory has a number of sorting algorithms and their respective tests implemented.

##### Contents:
- [Complexity Table](#complexity-table)
- [Bubble Sort](#bubble-sort)
- [Insertion Sort](#insertion-sort)
- [Merge Sort](#merge-sort)
- [Selection Sort](#selection-sort)

## Complexity Table
Algorithm         | Best Case  | Average Case | Worst Case | Space Complexity
----------------- | ---------- | ------------ | -----------| ----------------
Bubble Sort       | Ω(N)       | Θ(N^2)       | Ο(N^2)     | Ο(1)
Insertion Sort    | Ω(N)       | Θ(N^2)       | Ο(N^2)     | Ο(1)
Merge Sort        | Ω(Nlog(N)) | Θ(Nlog(N))   | Ο(Nlog(N)  | O(N)
Selection Sort    | Ω(N^2)     | Θ(N^2)       | Ο(N^2)     | O(1)

## Bubble Sort
##### Also known as Sinking Sort.

This algorithm repeatedly steps through a given list, comparing adjacent elements and swapping them in
ascending order if they are in the wrong order. This repeats until there are no more swaps to be done.

## Insertion Sort
##### Also known as Linear Insertion Sort.

This algorithm sorts by repeatedly taking the next element and inserting it back into the list in its
proper order with respect to elements already inserted.

## Merge Sort

This algorithm divides the given, unsorted list into sub-lists, each containing one element. These
sub-lists are merged together to produce new, sorted sub-lists until there is only one sub-list remaining.
This is the completed, sorted list. This algorithm is commonly implemented using recursion.

## Selection Sort

This algorithm sorts a list of numbers in ascending order by repeatedly finding the minimum element
from the unsorted portion and placing it at the beginning. There are two sub-lists that are maintained
in this situation: 

1) the sub-list of sorted elements and
2) the sub-list that remains to be sorted.

In every iteration of the selection sort, the minimum element from the unsorted sub-list is chosen and
moved into the sub-list of sorted elements.
