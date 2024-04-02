#GUI.py

import tkinter as tk
from tkinter import ttk
import random
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Import your sorting algorithms
from sorting_algorithms import *


class SortingVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithm Visualizer")

        self.algorithms = {
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

# Load the background image
        background_image = tk.PhotoImage(file="bg_image.png")

        # Create a label to hold the background image
        background_label = tk.Label(self.root, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        # Set the label as a background layer
        background_label.image = background_image
        self.selected_algorithms = []
        self.array_size = tk.IntVar(value=50)
        self.manual_input_var = tk.BooleanVar()
        self.user_input_var = tk.StringVar(value=True)
        self.array = []  # Initialize the array attribute

        # Frame to hold array display
        self.array_frame = ttk.Frame(self.root)
        self.array_frame.pack(pady=10)

        ttk.Label(self.array_frame, text="Generated Array:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.array_text = tk.Text(self.array_frame, height=5, width=40)
        self.array_text.grid(row=1, column=0, padx=5, pady=5)

        # Frame to select input method
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.manual_input_button = ttk.Radiobutton(self.input_frame, text="Input Numbers Manually", variable=self.manual_input_var, value=True, command=self.toggle_input_entry)
        self.manual_input_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.random_generate_button = ttk.Radiobutton(self.input_frame, text="Use Generated Numbers", variable=self.manual_input_var, value=False, command=self.toggle_input_entry)
        self.random_generate_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        # Entry for manual user input
        self.user_input_entry = ttk.Entry(self.input_frame, textvariable=self.user_input_var, width=40, state=tk.DISABLED)
        self.user_input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Label for array size entry
        ttk.Label(self.input_frame, text="Enter Array Size Here:").grid(row=2, column=0, padx=5, pady=5, sticky="w")

        # Entry for array size
        self.array_size_entry = ttk.Entry(self.input_frame, textvariable=self.array_size, width=10, state=tk.DISABLED)
        self.array_size_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame to hold algorithm selection
        self.algo_frame = ttk.Frame(self.root)
        self.algo_frame.pack(pady=10)

        ttk.Label(self.algo_frame, text="Select Sorting Algorithms:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.algo_vars = {}
        for idx, algo_name in enumerate(self.algorithms.keys()):
            self.algo_vars[algo_name] = tk.BooleanVar(value=True)
            ttk.Checkbutton(self.algo_frame, text=algo_name, variable=self.algo_vars[algo_name]).grid(row=idx + 1, column=0, padx=5, pady=5, sticky="w")

        # Frame to hold array size selection and buttons
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(pady=10)

        self.generate_button = ttk.Button(self.control_frame, text="Submit / Generate Array", command=self.generate_array)
        self.generate_button.grid(row=0, column=0, padx=5, pady=5)

        self.visualize_button = ttk.Button(self.control_frame, text="Visualize", command=self.open_visualization)
        self.visualize_button.grid(row=0, column=1, padx=5, pady=5)

    def toggle_input_entry(self):
        if self.manual_input_var.get():
            self.user_input_entry.config(state=tk.NORMAL)
            self.array_size_entry.config(state=tk.DISABLED)
        else:
            self.user_input_entry.config(state=tk.DISABLED)
            self.array_size_entry.config(state=tk.NORMAL)

    def generate_array(self):
        if not self.manual_input_var.get():
            size = self.array_size.get()
            unique_numbers = set()  # Set to keep track of unique numbers
            while len(unique_numbers) < size:
                unique_numbers.add(random.randint(-100, 1000))  # Add unique random numbers between -100 and 1000
            self.array = list(unique_numbers)  # Convert set to list
            self.array_text.delete('1.0', tk.END)
            self.array_text.insert(tk.END, ', '.join(map(str, self.array)))
        else:
            input_numbers = self.user_input_var.get().split(',')
            self.array = [int(num) for num in input_numbers]

    def open_visualization(self):
        window = tk.Toplevel(self.root)
        window.title("Sorting Algorithm Visualization")

        fig, ax = plt.subplots(figsize=(12, 8))  # Increase the figure size for better visibility

        execution_times = {}
        for algo_name, algo_func in self.algorithms.items():
            if self.algo_vars[algo_name].get():
                arr_copy = self.array.copy()
                start_time = time.time()
                algo_func(arr_copy)
                end_time = time.time()
                execution_time = end_time - start_time
                execution_times[algo_name] = execution_time

        colors = ['lightblue', 'lightcoral', 'lightgreen', 'lightgrey', 'lightpink', 'lightyellow', 'lightcyan', 'lightgoldenrodyellow', 'lightsteelblue', 'lightskyblue']
        bar_width = 0.5
        opacity = 0.8
        bar_spacing = 1
        bar_positions = range(len(execution_times))

        # Plot bars for each algorithm
        for idx, (algo_name, exec_time) in enumerate(execution_times.items()):
            ax.bar(idx * bar_spacing, exec_time, bar_width, alpha=opacity, color=colors[idx % len(colors)], label=algo_name)

        # Customize labels and title
        ax.set_xlabel('Sorting Algorithms')
        ax.set_ylabel('Execution Time (s)')
        ax.set_title('Sorting Algorithm Execution Time')

        # Customize ticks and legend
        ax.set_xticks([idx * bar_spacing for idx in range(len(execution_times))])
        ax.set_xticklabels(execution_times.keys(), rotation=45, ha='right', fontsize=10)  # Adjust rotation and fontsize for better visibility
        ax.legend(loc='upper right')  # Move the legend to the upper right corner

        # Display the plot
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().pack()

        # Print median after sorting
        sorted_array = sorted(self.array)
        median = find_median(sorted_array)
        ttk.Label(window, text=f"Median after Sorting: {median}").pack()

        # Print kth smallest after sorting
        kth_smallest = quickselect_kth_smallest(sorted_array, 3)  # Change '3' to any desired 'k' value
        ttk.Label(window, text=f"Kth Smallest after Sorting: {kth_smallest}").pack()

        # Print sorted array
        ttk.Label(window, text=f"Sorted Array: {sorted_array}").pack()


if __name__ == "__main__":
    root = tk.Tk()
    app = SortingVisualizerApp(root)
    root.mainloop()
