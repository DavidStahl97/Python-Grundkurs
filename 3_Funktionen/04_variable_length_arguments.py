def biggest(x, y):
    if x > y:
        return x, y
    else:
        return y, x


print(biggest(1, 7))
first, second = biggest(2,3)    # Tuple
print("The biggest number is {}. The second number is {}".format(first, second))


# what about more than 2?
