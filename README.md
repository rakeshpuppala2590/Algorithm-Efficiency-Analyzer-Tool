# Algorithm-Efficiency-Analyzer-Tool

This project is a Sorting Algorithm Visualizer implemented in Python using the Tkinter library for the graphical user interface (GUI). It allows users to visualize the performance of various sorting algorithms on randomly generated or user-defined arrays of numbers.

Link to Video Demo :  https://drive.google.com/drive/folders/1Y9G-C-UZ_3kXUhMwEdxE5lfrNmYeKo1P 

# Features

Supports multiple sorting algorithms, including Bubble Sort, Insertion Sort, Quick Sort, Heap Sort, Counting Sort, Selection Sort, Merge Sort, Radix Sort, and Bucket Sort.
Users can input numbers manually or use randomly generated numbers for sorting.
Provides visualization of sorting algorithm performance through a bar chart, displaying execution times in seconds.
Additional information displayed includes the median of the sorted array and the kth smallest element after sorting.
Customizable plot parameters such as colors, bar width, opacity, and bar spacing.
Algorithm selection feature allows users to choose which sorting algorithms to include in the visualization.


# Usage

1. Clone the repository to your local machine:

   
   
git clone https://github.com/abhinavkarthik2023/Algorithm-Efficiency-Analyzer-Tool.git



2. Navigate to the project directory:

cd sorting-algorithm-visualizer

3. Install the required dependencies:

pip install -r requirements.txt

Required Libraries
   
tkinter: Used for building the GUI.


matplotlib: Used for plotting the visualization.

4. Run the application:

python GUI.py

5. Use the GUI interface to select sorting algorithms, input array size and numbers, and initiate visualization.



# How to Use


Selecting Sorting Algorithms: Check the checkboxes corresponding to the sorting algorithms you want to visualize.




Input Methods:


Manual Input: Select the "Input Numbers Manually" option and enter space-separated numbers in the text box provided.


Generated Numbers: Select the "Use Generated Numbers" option and specify the array size.



Generating Array: Click the "Generate Array" button to generate the array based on the selected input method and size.


Visualizing: Click the "Visualize" button to initiate the visualization process. A new window will open displaying the bar chart representing the execution times of the selected sorting algorithms.


Customization

Plot Parameters: You can customize various plot parameters such as colors, bar width, opacity, and bar spacing by modifying the corresponding variables in the GUI.py file.


# License

This project is licensed under the MIT License. See the LICENSE file for details.


# Disclaimer

This project is developed for educational purposes and should not be used for critical or production-level applications without thorough testing and validation.
