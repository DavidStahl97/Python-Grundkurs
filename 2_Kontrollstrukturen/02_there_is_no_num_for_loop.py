# There is no such concept in Python:

# data = [1, 7, 11]
# for i = 0; i<len(data); i++:
#     print("Now i is " + i)
#     print("The value is {}".format(data[i]))

# Often new comers attempt to build one:

data = [1, 7, 11]

# NOT pythonic: faking it with a while


########################################################
print("########################################################")
########################################################
# but sometimes, fairly rarely, you really need just an
# increasing number of integers.



# think of the above as:
# for i = 0; i<10; i++:
#     print(i, end=', ')

# So, use range to model for int loops

########################################################
print("########################################################")
########################################################
# More often, you need the index and the value.

# How would you actually accomplish this? With range? No.
# for idx = 0; idx<len(data); idx++:
#     val = data[idx]
#     print(" {} --> {}".format(idx, val))


