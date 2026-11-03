
# Module 3: Linear Search vs Binary Search

# 20 synthetic patient IDs in sorted order
patient_ids = [
    1001, 1002, 1003, 1004, 1005,
    1006, 1007, 1008, 1009, 1010,
    1011, 1012, 1013, 1014, 1015,
    1016, 1017, 1018, 1019, 1020
]


# Linear Search
def linear_search(data, key):
    comparisons = 0

    for i in range(len(data)):
        comparisons += 1

        if data[i] == key:
            return i, comparisons

    return -1, comparisons


# Binary Search
def binary_search(data, key):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if data[mid] == key:
            return mid, comparisons
        elif data[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1, comparisons


# Compare both searching methods
def compare_search(key):
    linear_result, linear_count = linear_search(patient_ids, key)
    binary_result, binary_count = binary_search(patient_ids, key)

    print("\n--- SEARCH RESULTS ---")

    if linear_result != -1:
        print("Patient ID found at position:", linear_result + 1)
    else:
        print("Patient ID not found.")

    print("Linear Search comparisons:", linear_count)
    print("Binary Search comparisons:", binary_count)


# Measure comparisons for different input sizes


def performance_test():
    import csv

    sizes = [5, 10, 15, 20]
    rows = []

    print("\nSEARCH PERFORMANCE ANALYSIS")
    print("-" * 65)
    print(f"{'Size':<8}{'Case':<12}{'Linear':<15}{'Binary':<15}")
    print("-" * 65)

    for size in sizes:
        data = patient_ids[:size]

        test_cases = [
            ("First", data[0]),
            ("Middle", data[size // 2]),
            ("Last", data[-1])
        ]

        for case, target in test_cases:
            _, linear_count = linear_search(data, target)
            _, binary_count = binary_search(data, target)

            print(
                f"{size:<8}{case:<12}"
                f"{linear_count:<15}{binary_count:<15}"
            )

            rows.append([
                size, case, linear_count, binary_count
            ])

    with open("search_performance.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Input Size", "Search Case",
            "Linear Comparisons", "Binary Comparisons"
        ])
        writer.writerows(rows)

    print("-" * 65)
    print("Performance data saved to search_performance.csv")


# Menu
def main():
    while True:
        print("\n--- PATIENT RECORD SEARCH ---")
        print("1. Linear Search")
        print("2. Binary Search")
        print("3. Compare both algorithms")
        print("4. Performance analysis")
        print("5. Display patient IDs")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3"]:
            try:
                key = int(input("Enter patient ID to search: "))
            except ValueError:
                print("Invalid input. Enter a numeric patient ID.")
                continue

            if choice == "1":
                index, count = linear_search(patient_ids, key)
                print("Linear Search comparisons:", count)

                if index != -1:
                    print("Patient ID found at position:", index + 1)
                else:
                    print("Patient ID not found.")

            elif choice == "2":
                index, count = binary_search(patient_ids, key)
                print("Binary Search comparisons:", count)

                if index != -1:
                    print("Patient ID found at position:", index + 1)
                else:
                    print("Patient ID not found.")

            else:
                compare_search(key)

        elif choice == "4":
            performance_test()

        elif choice == "5":
            print("Patient IDs:", patient_ids)

        elif choice == "6":
            print("Exiting search module.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
