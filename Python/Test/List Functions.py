
# Create empty list
friends = []
# Add value
friends.append("Oscar")
friends.append("Angela")
# Add kevin to index position 1
friends.insert(1, "Kevin")
friends.append("Sam")
friends.append("Sam")
# get angela index numbers
print(friends.index("Oscar"))
# get count how many angela
print(friends.count("Sam"))

# friends.remove("Kevin")
print( friends )
# Get oscar index number
print( friends.index("Oscar") )
# get how many angela in the list
print( friends.count("Angela") )
# get rid of last element in this case remove sam from the list
friends.pop()
# start to print alphabetical order or use reverse instead of sort it'll do reverse
friends.sort()
print( friends )
# get rid of all element from list
friends.clear()
print( friends )

# u can combine to list another list
friends = [ "Abdul", "Helena"]
lucky_numbers = [3, "twenty", 7 , 16, 24, 49.0]
friends.extend(lucky_numbers)
print(friends)

# create another list make it copy
friend2 = friends.copy()
print(friend2)
