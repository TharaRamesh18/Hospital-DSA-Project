
# Hospital DSA Project
# Main Menu to Run All Three Modules

import runpy


def main():
    while True:
        print("\n===================================")
        print("       HOSPITAL DSA PROJECT")
        print("===================================")
        print("1. ICU Patient Monitoring (AVL Tree)")
        print("2. Hospital Pipeline Layout (Prim's Algorithm)")
        print("3. Patient Record Search")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            runpy.run_module("avl_module", run_name="__main__")

        elif choice == "2":
            runpy.run_module("prim_module", run_name="__main__")

        elif choice == "3":
            runpy.run_module("search_module", run_name="__main__")

        elif choice == "4":
            print("Thank you for using Hospital DSA Project!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
