def extract_parts(filename, identifier):
    with open(filename, 'r') as file:
        lines = file.readlines()

    for line in lines:
        parts = line.split()
        if parts[0] == identifier:
            return parts[1], parts[2], parts[3]

    return None, None, None

# Example usage
filename = 'address.txt'
identifier = 'n1'
part2, part3, part4 = extract_parts(filename, identifier)

if part2 and part3 and part4:
    print(f"Identifier: {identifier}")
    print(f"Part 2: {part2}")
    print(f"Part 3: {part3}")
    print(f"Part 4: {part4}")
else:
    print(f"Identifier {identifier} not found in file.")
