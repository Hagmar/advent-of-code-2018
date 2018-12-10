import sys

all_metadata = []
def process_node(i, line):
    global all_metadata
    children, metadata = line[i:i+2]
    i += 2
    child_values = []
    for child in range(children):
        i, c_value = process_node(i, line)
        child_values.append(c_value)

    metadata_list = line[i:i+metadata]
    value = 0
    if not children:
        value = sum(metadata_list)
    else:
        for meta in metadata_list:
            if meta-1 < children:
                value += child_values[meta-1]

    all_metadata += metadata_list
    i += metadata
    return i, value

line = list(map(int, input().split()))

_, value = process_node(0, line)
print(sum(all_metadata))
print(value)
