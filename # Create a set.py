# Create a set
v = {"car","bus","train"}
# Print its content
print(v)

# Add bicycle
v.add("bicycle")
# Print it
print(v)

# use for loop to read data
for veh in v:
  print(veh)

# remove car and print
v.remove("car")
print(v)

# remove one item from the set randomly and print
print(v.pop())

# clear the set
v.clear()

# print set
print(v)
