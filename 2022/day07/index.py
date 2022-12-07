#%%
with open("input.txt", encoding="utf-8") as f:
    data = f.read().splitlines()

tree: dict = {"/": {}}
tree_pointer = tree
current_dir: list[str] = []

for o in data:
    if o.startswith("$"):
        # this is a command
        match o[2:4]:
            case "cd":
                # change directory
                new_dir = o.split(" cd ")[1]
                if new_dir == "..":
                    current_dir.pop()
                    tree_pointer = tree
                    for parent_dir in current_dir:
                        tree_pointer = tree_pointer[parent_dir]
                else:
                    current_dir.append(new_dir)
                    tree_pointer = tree_pointer[new_dir]
            case "ls":
                pass
            case _:
                raise Exception(f"cannot match {o[2:4]}")
    elif o.startswith("dir "):
        new_dir = o[4:]
        if new_dir in tree_pointer: 
            continue
        tree_pointer[new_dir] = dict()
    else:
        size, name = o.split(" ")
        tree_pointer[name] = int(size)  # type: ignore
size_below_threshold = 0
threshold = 100000
dir_sizes: list[int] = []
def get_size_of_dir(cur_dir: dict):
    global size_below_threshold
    size_of_dir = 0
    for name, value in cur_dir.items():
        if isinstance(value, dict):
            dir_size = get_size_of_dir(cur_dir[name])
            if dir_size <= threshold:
                size_below_threshold += dir_size
            size_of_dir += dir_size
            dir_sizes.append(dir_size)
        else:
            size_of_dir += value
    return size_of_dir

total_disk_space = 70000000
total_disk_space_needed = 30000000
current_disk_space_free = total_disk_space - get_size_of_dir(tree)
print("Part 1:", size_below_threshold)

space_to_be_freed = total_disk_space_needed - current_disk_space_free

smallest_dir: int = total_disk_space
for size in dir_sizes:
    if size < space_to_be_freed: 
        continue

    if size < smallest_dir:
        smallest_dir = size

print("Part 2:", smallest_dir)
