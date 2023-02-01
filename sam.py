# Python3 code to demonstrate working
# of Extract string between 2 substrings
# Using loop + index()

# initializing string
test_str = "Gfg is best for geeks and CS"

# printing original string
print("The original string is : " + str(test_str))

# initializing substrings
sub1 = "is"
sub2 = "and"

# getting index of substrings
idx1 = test_str.index(sub1)
idx2 = test_str.index(sub2)
res = ''
# getting elements in between
for idx in range(idx1 + len(sub1) + 1, idx2):
	res = res + test_str[idx]

# printing result
print("The extracted string : " + res)