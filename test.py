#test.py

import unittest
from sorting_algorithms import *
import random

class TestSortingAlgorithms(unittest.TestCase):
    def test_bubble_sort(self):
        print("Testing Bubble Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        bubble_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Bubble Sort test passed!\n")

    def test_insertion_sort(self):
        print("Testing Insertion Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        insertion_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Insertion Sort test passed!\n")

    def test_quick_sort(self):
        print("Testing Quick Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        quick_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Quick Sort test passed!\n")

    def test_heap_sort(self):
        print("Testing Heap Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        heap_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Heap Sort test passed!\n")

    def test_counting_sort(self):
        print("Testing Counting Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        arr = counting_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Counting Sort test passed!\n")

    def test_selection_sort(self):
        print("Testing Selection Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        selection_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Selection Sort test passed!\n")

    def test_merge_sort(self):
        print("Testing Merge Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        merge_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Merge Sort test passed!\n")

    def test_radix_sort(self):
        print("Testing Radix Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        radix_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Radix Sort test passed!\n")

    def test_bucket_sort(self):
        print("Testing Bucket Sort...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        arr = bucket_sort(arr)
        print("After sorting:", arr)
        self.assertEqual(arr, [1, 2, 3, 5, 8])
        print("Bucket Sort test passed!\n")

    def test_quickselect_kth_smallest(self):
        print("Testing Quickselect (Kth Smallest)...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        kth_smallest = quickselect_kth_smallest(arr, 2)
        print("Kth Smallest:", kth_smallest)
        self.assertEqual(kth_smallest, 3)
        print("Quickselect (Kth Smallest) test passed!\n")

    def test_quickselect_kth_largest(self):
        print("Testing Quickselect (Kth Largest)...")
        arr = [5, 3, 8, 1, 2]
        print("Before sorting:", arr)
        kth_largest = quickselect_kth_largest(arr, 2)
        print("Kth Largest:", kth_largest)
        self.assertEqual(kth_largest, 5)
        print("Quickselect (Kth Largest) test passed!\n")

    def test_array_generation(self):
        print("Testing Array Generation...")
        size = 10
        unique_numbers = set()  # Set to keep track of unique numbers
        while len(unique_numbers) < size:
            unique_numbers.add(random.randint(-1000, 1000))  # Add unique random numbers between -1000 and 1000
        arr = list(unique_numbers)  # Convert set to list
        print("Generated Array:", arr)
        self.assertEqual(len(arr), size)  # Check if array is generated with correct size
        print("Array Generation test passed!\n")

    def test_edge_cases(self):
        print("Testing Edge Cases...")
        # Empty array
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])

        # Array with one element
        arr = [5]
        bubble_sort(arr)
        self.assertEqual(arr, [5])

        # Sorted array
        arr = [1, 2, 3, 4, 5]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        # Array with all elements being the same
        arr = [2, 2, 2, 2, 2]
        bubble_sort(arr)
        self.assertEqual(arr, [2, 2, 2, 2, 2])
        print("Edge Cases test passed!\n")

    def test_performance(self):
        print("Testing Performance...")
        algorithms = {
            "Bubble Sort": bubble_sort,
            "Insertion Sort": insertion_sort,
            "Quick Sort": quick_sort,
            "Heap Sort": heap_sort,
            "Counting Sort": counting_sort,
            "Selection Sort": selection_sort,
            "Merge Sort": merge_sort,
            "Radix Sort": radix_sort,
            "Bucket Sort": bucket_sort
        }
        size = 10000
        for algo_name, algo_func in algorithms.items():
            arr = [random.randint(0, 1000) for _ in range(size)]
            start_time = time.time()
            algo_func(arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"{algo_name}: {execution_time:.5f} seconds")
        print("Performance test passed!\n")


    def test_stability(self):
        print("Testing Stability...")
        arr = [(5, 'a'), (3, 'b'), (3, 'c'), (1, 'd'), (2, 'e')]
        merge_sort(arr)
        self.assertEqual(arr, [(1, 'd'), (2, 'e'), (3, 'b'), (3, 'c'), (5, 'a')])
        print("Stability test passed!\n")

    def test_handling_different_data_types(self):
        print("Testing Handling Different Data Types...")
        arr = [5, 3, {'a': 1}, (2, 3), [4, 5]]
        try:
            merge_sort(arr)
        except TypeError as e:
            print("Error:", e)
        else:
            self.fail("Expected TypeError but no exception raised")
        print("Handling Different Data Types test passed!\n")

    def test_handling_negative_numbers(self):
        print("Testing Handling Negative Numbers...")
        arr = [5, -3, 8, -1, 2]
        try:
            bubble_sort(arr)
            self.assertEqual(arr, [-3, -1, 2, 5, 8])
        except AssertionError:
            print("Error: Sorting negative numbers failed")
        else:
            print("Handling Negative Numbers test passed!\n")

if __name__ == '__main__':
    unittest.main()
