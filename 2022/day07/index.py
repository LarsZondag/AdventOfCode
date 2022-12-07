#%%
with open("input.txt", encoding="utf-8") as f:
    data = f.read().splitlines()

# Parse data into tree structure
tree: dict = {"/": {}}
tree_pointer: dict = tree
current_dir: list[str] = []

for line in data:
    if line.startswith("$ cd "):
        # change directory
        new_dir = line[len("$ cd "):]
        if new_dir == "..":
            # Go up one level
            current_dir.pop()
            tree_pointer = tree
            for parent_dir in current_dir:
                tree_pointer = tree_pointer[parent_dir]
        else:
            # Go one level deeper (into `new_dir`)
            current_dir.append(new_dir)
            tree_pointer = tree_pointer[new_dir]
    elif line.startswith("dir "):
        new_dir = line[4:]
        if new_dir in tree_pointer: 
            continue
        tree_pointer[new_dir] = dict()
    elif line == "$ ls":
        continue
    else:
        size, name = line.split(" ")
        tree_pointer[name] = int(size) # type: ignore

# Traverse the tree structure to get size information
dir_sizes: list[int] = []

def get_size_of_dir(cur_tree: dict):
    size_of_dir = 0
    for name, value in cur_tree.items():
        if isinstance(value, dict):
            dir_size = get_size_of_dir(cur_tree[name])
            size_of_dir += dir_size
        else:
            size_of_dir += value
    
    dir_sizes.append(size_of_dir)
    return size_of_dir
get_size_of_dir(tree)

threshold: int = 100000
total_size_below_threshold: int = 0
for size in dir_sizes:
    if size <= threshold:
        total_size_below_threshold += size

print("Part 1: ", total_size_below_threshold)

#%%
total_disk_space = 70000000
total_disk_space_needed = 30000000
current_disk_space_free = total_disk_space - get_size_of_dir(tree)

space_to_be_freed = total_disk_space_needed - current_disk_space_free

smallest_dir: int = total_disk_space
for size in dir_sizes:
    if size < space_to_be_freed: 
        continue

    if size < smallest_dir:
        smallest_dir = size

print("Part 2:", smallest_dir)
