# Hospital Data Structures and Algorithms Project

## 1. Project Overview

This project demonstrates the application of Data Structures and Algorithms (DSA) to hospital-related problems using Python. It contains three modules: ICU patient monitoring using an AVL tree, hospital pipeline layout using Prim's algorithm, and patient record searching using Linear Search and Binary Search.

The project uses synthetic patient IDs, sample hospital locations, and sample connection costs for educational purposes. No real patient information is used.

## 2. Objectives

- Implement an AVL tree for efficient patient ID insertion, deletion, and searching.
- Apply Prim's algorithm to determine a minimum-cost connection layout.
- Implement and compare Linear Search and Binary Search.
- Count search comparisons for different input sizes.
- Analyze the time and space complexity of the algorithms.

## 3. Technologies Used

- Programming language: Python
- Development environment: Python IDLE
- Performance analysis: Python comparison counters and CSV output
- Graph plotting: Microsoft Excel

## 4. Project Modules

### Module 1: ICU Patient Monitoring — AVL Tree

The AVL tree stores patient IDs in a self-balancing binary search tree.

**Operations:**
- Insert a patient ID
- Delete a patient ID
- Search for a patient ID
- Display patient IDs in sorted order
- Display balance factors

**Time complexity:** O(log n) for search, insertion, and deletion in an AVL tree.

### Module 2: Hospital Pipeline Layout — Prim's Algorithm

This module models hospital locations as vertices and connections as weighted edges. Prim's algorithm finds a minimum spanning tree for the connected graph.

**Operations:**
- Display sample connections
- Calculate the minimum spanning tree
- Display selected connections and total cost

**Time complexity:** O(V²) using an adjacency matrix.

### Module 3: Patient Record Search

This module compares two searching algorithms using a sorted list of synthetic patient IDs.

**Operations:**
- Perform Linear Search
- Perform Binary Search
- Compare search results and comparison counts
- Run performance analysis for input sizes 5, 10, 15, and 20
- Display the patient ID list

**Time complexity:**
- Linear Search: O(n) worst case
- Binary Search: O(log n) worst case

## 5. Project Files

| File | Description |
|---|---|
| `main.py` | Main menu and module integration |
| `avl_module.py` | AVL tree implementation |
| `prim_module.py` | Prim's algorithm implementation |
| `search_module.py` | Linear Search, Binary Search, and performance analysis |
| `search_performance.csv` | Recorded search comparison counts |
| `test_log.txt` | Test cases and their results |
| `complexity_analysis.txt` | Time and space complexity analysis |

## 6. How to Run the Project

1. Install Python 3 if it is not already installed.
2. Place all four Python files in the same folder.
3. Open `main.py` using Python IDLE.
4. Select **Run → Run Module** or press **F5**.
5. Choose a module from the main menu.

**Main menu options:**
1. ICU Patient Monitoring (AVL Tree)
2. Hospital Pipeline Layout (Prim's Algorithm)
3. Patient Record Search
4. Exit

## 7. Testing

The modules were tested with normal operations, boundary inputs, missing records, duplicate IDs, and invalid menu choices.

The test log records the inputs, expected outcomes, and observed results. The search module also reports comparison counts for different input sizes.

## 8. Performance Analysis

The search algorithms are evaluated using comparison counts for input sizes 5, 10, 15, and 20. The results are stored in `search_performance.csv` and used to create a graph in Microsoft Excel.

The tested last-element search cases demonstrate that Linear Search requires more comparisons as the input size increases, while Binary Search uses fewer comparisons on the sorted dataset.

## 9. Limitations

- The data is synthetic and does not represent a live hospital information system.
- The pipeline model uses sample locations and connection costs.
- Search performance is evaluated using comparison counts rather than execution time.
- The project does not connect to a hospital database or real medical equipment.

## 10. Future Enhancements

- Integrate a database to store patient records.
- Add a graphical user interface.
- Use real-world pipeline layout data where appropriate.
- Evaluate algorithms with larger datasets.
- Add automated tests and more detailed performance graphs.

## 11. Conclusion

This project demonstrates how AVL trees, Prim's algorithm, Linear Search, and Binary Search can be applied to sample hospital-related problems. The implementation and comparison analysis highlight the importance of selecting suitable data structures and algorithms for efficient data management and network design.
