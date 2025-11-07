from guitar import Guitar


guitars = []
# Open the file for reading
in_file = open('guitars.csv', 'r')
in_file.readline()
for line in in_file:
    parts = line.strip().split(',')
    name = parts[0]
    year = parts[1]
    cost = parts[2]
    guitar_attributes = Guitar(name, year, float(cost))
    guitars.append(guitar_attributes)
in_file.close()

print("\nBefore Sorting\n")
for guitar_attributes in guitars:
    print(guitar_attributes)

guitars.sort()

print("\nAfter Sorting\n")
for guitar_attributes in guitars:
    print(guitar_attributes)