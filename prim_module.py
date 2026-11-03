
# Module 2: Prim's Algorithm for Hospital Pipeline Layout

INF = float('inf')

# 20 hospital locations
locations = [
    "ICU", "Ward A", "Ward B", "Emergency", "OT",
    "Laboratory", "Pharmacy", "Radiology", "Reception", "OPD",
    "Blood Bank", "ICU Store", "Ward C", "Kitchen", "Laundry",
    "Admin", "Canteen", "Parking", "Generator", "Water Supply"
]

N = len(locations)

# Each connection: (location 1 index, location 2 index, cost)
# Cost represents the pipeline installation cost
edges = [
    (0, 1, 4), (0, 2, 6), (0, 3, 5), (0, 4, 7),
    (1, 2, 3), (1, 5, 6), (1, 8, 8),
    (2, 3, 4), (2, 6, 7), (2, 12, 5),
    (3, 4, 2), (3, 7, 6), (3, 9, 8),
    (4, 5, 4), (4, 7, 3), (4, 18, 9),
    (5, 6, 2), (5, 10, 5), (5, 15, 8),
    (6, 7, 4), (6, 10, 3), (6, 11, 6),
    (7, 8, 5), (7, 9, 4), (7, 14, 7),
    (8, 9, 3), (8, 15, 6), (8, 17, 8),
    (9, 12, 6), (9, 13, 7),
    (10, 11, 2), (10, 12, 5), (10, 19, 7),
    (11, 12, 4), (11, 18, 6),
    (12, 13, 3), (12, 14, 5),
    (13, 14, 2), (13, 16, 4),
    (14, 15, 5), (14, 16, 3),
    (15, 16, 2), (15, 17, 4),
    (16, 17, 3), (17, 18, 5),
    (18, 19, 4), (11, 19, 8)
]


def create_graph():
    graph = [[INF] * N for _ in range(N)]

    for i in range(N):
        graph[i][i] = 0

    for u, v, cost in edges:
        graph[u][v] = cost
        graph[v][u] = cost

    return graph


def prim(graph):
    selected = [False] * N
    selected[0] = True

    total_cost = 0
    edge_count = 0

    print("\nPrim's Algorithm Trace")
    print("Starting location:", locations[0])
    print("-" * 50)

    while edge_count < N - 1:
        minimum = INF
        start = -1
        end = -1

        # Find the minimum-cost edge connecting
        # a selected location to an unselected location
        for i in range(N):
            if selected[i]:
                for j in range(N):
                    if not selected[j] and graph[i][j] < minimum:
                        minimum = graph[i][j]
                        start = i
                        end = j

        if end == -1:
            print("Error: The graph is disconnected.")
            return

        selected[end] = True
        edge_count += 1
        total_cost += minimum

        print(
            locations[start], "->", locations[end],
            "| Cost:", minimum,
            "| Total:", total_cost
        )

    print("-" * 50)
    print("Total pipeline installation cost:", total_cost)
    print("Number of selected connections:", edge_count)


def show_connections():
    print("\nAvailable pipeline connections:")
    for u, v, cost in edges:
        print(locations[u], "<->", locations[v], "| Cost:", cost)


def main():
    graph = create_graph()

    while True:
        print("\n--- HOSPITAL PIPELINE LAYOUT ---")
        print("1. Display available connections")
        print("2. Run Prim's algorithm")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_connections()
        elif choice == "2":
            prim(graph)
        elif choice == "3":
            print("Exiting Prim's algorithm module.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
