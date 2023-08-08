def print_towers(n, state):
    for i in range(n-1, -1, -1):
        for j in range(3):
            if len(state[j]) > i:
                print((" " * (n - int(state[j][i]))) + ("#" * int(state[j][i])) + (" " * (n - int(state[j][i]))), end="\t")
            else:
                print((" " * (n+1)), end="\t")
        print("\n")
    print("-" * (4*(n+1)) + "\n")

def tower_of_hanoi_recursive(n, from_rod, to_rod, aux_rod, state):
    if n == 1:
        disk = state[from_rod].pop()
        state[to_rod].append(disk)
        print_towers(len(state[0]), state)
    else:
        tower_of_hanoi_recursive(n-1, from_rod, aux_rod, to_rod, state)
        disk = state[from_rod].pop()
        state[to_rod].append(disk)
        print_towers(len(state[0]), state)
        tower_of_hanoi_recursive(n-1, aux_rod, to_rod, from_rod, state)

# Example usage
num_disks = 3
initial_state = [["3", "2", "1"], [], []]
print_towers(num_disks, initial_state)
tower_of_hanoi_recursive(num_disks, 0, 2, 1, initial_state)
