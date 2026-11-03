
# Module 1: AVL Tree for ICU Patient Monitoring

class Node:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if node is None:
        return 0
    return node.height


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


# Right rotation (LL case)
def right_rotate(y):
    x = y.left
    temp = x.right

    x.right = y
    y.left = temp

    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))

    return x


# Left rotation (RR case)
def left_rotate(x):
    y = x.right
    temp = y.left

    y.left = x
    x.right = temp

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y


# Insert a patient ID into the AVL tree
def insert(root, patient_id):
    if root is None:
        return Node(patient_id)

    if patient_id < root.patient_id:
        root.left = insert(root.left, patient_id)
    elif patient_id > root.patient_id:
        root.right = insert(root.right, patient_id)
    else:
        print("Patient ID already exists!")
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    balance = balance_factor(root)

    # LL case
    if balance > 1 and patient_id < root.left.patient_id:
        return right_rotate(root)

    # RR case
    if balance < -1 and patient_id > root.right.patient_id:
        return left_rotate(root)

    # LR case
    if balance > 1 and patient_id > root.left.patient_id:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RL case
    if balance < -1 and patient_id < root.right.patient_id:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


# Find the smallest ID in a subtree
def min_value_node(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


# Delete a patient ID and rebalance the AVL tree
def delete_node(root, patient_id):
    if root is None:
        return root

    if patient_id < root.patient_id:
        root.left = delete_node(root.left, patient_id)

    elif patient_id > root.patient_id:
        root.right = delete_node(root.right, patient_id)

    else:
        # Case 1 and 2: zero or one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: two children
        temp = min_value_node(root.right)
        root.patient_id = temp.patient_id
        root.right = delete_node(root.right, temp.patient_id)

    # Update height
    root.height = 1 + max(height(root.left), height(root.right))

    balance = balance_factor(root)

    # LL case
    if balance > 1 and balance_factor(root.left) >= 0:
        return right_rotate(root)

    # LR case
    if balance > 1 and balance_factor(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # RR case
    if balance < -1 and balance_factor(root.right) <= 0:
        return left_rotate(root)

    # RL case
    if balance < -1 and balance_factor(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

# Search for a patient ID
def search_patient(root, patient_id):
    if root is None:
        return False

    if root.patient_id == patient_id:
        return True

    if patient_id < root.patient_id:
        return search_patient(root.left, patient_id)

    return search_patient(root.right, patient_id)

# Display patient IDs in sorted order
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.patient_id, end=" ")
        inorder(root.right)


# Display each patient's ID and balance factor
def display_balance(root):
    if root is not None:
        display_balance(root.left)
        print("Patient ID:", root.patient_id,
              "| Balance Factor:", balance_factor(root))
        display_balance(root.right)



# Menu-driven AVL Tree program
if __name__ == "__main__":
    root = None

    # Insert 20 sample patient IDs
    patient_ids = [30, 20, 10, 40, 50, 25, 5, 35, 45, 60,
                   15, 27, 3, 8, 33, 37, 55, 65, 70, 1]

    for patient_id in patient_ids:
        root = insert(root, patient_id)

    while True:
        print("\n--- ICU PATIENT AVL TREE ---")
        print("1. Insert patient ID")
        print("2. Delete patient ID")
        print("3. Search patient ID")
        print("4. Display sorted patient IDs")
        print("5. Display balance factors")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_id = int(input("Enter patient ID: "))
            if search_patient(root, patient_id):
                print("Patient ID already exists!")
            else:
                root = insert(root, patient_id)
                print("Patient ID inserted successfully.")

        elif choice == "2":
            patient_id = int(input("Enter patient ID: "))
            if search_patient(root, patient_id):
                root = delete_node(root, patient_id)
                print("Patient ID deleted successfully.")
            else:
                print("Patient ID not found.")

        elif choice == "3":
            patient_id = int(input("Enter patient ID: "))
            if search_patient(root, patient_id):
                print("Patient ID found.")
            else:
                print("Patient ID not found.")

        elif choice == "4":
            print("Patient IDs in sorted order:")
            inorder(root)
            print()

        elif choice == "5":
            print("Patient balance factors:")
            display_balance(root)

        elif choice == "6":
            print("Exiting AVL module.")
            break

        else:
            print("Invalid choice. Please try again.")
