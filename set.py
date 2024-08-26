#Creating sets
colors = {"red", "green", "blue", "yellow"}
colors.add("purple")
print(colors)

#Sets operations
primary_colors = {"red", "blue", "yellow"}
intersection_set = colors.intersection(primary_colors)
print(intersection_set)

union_set = colors.union(primary_colors)
print(union_set)

difference_set = colors.difference(primary_colors)
print(difference_set)

#set membership
greenprimary = "green" in primary_colors
print(greenprimary)

orangecolors = "orange" in colors
print(orangecolors)
