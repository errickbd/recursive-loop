#count down
def count_down(n):
    if n == -1:
        return
    print(n)
    return count_down(n-1)

#count up
def count_up(n, counter = 0):
    if counter == n + 1:
        return
    print(counter)
    return count_up(n, counter + 1)



print(count_down(6))
print(count_up(6, counter = 0))
