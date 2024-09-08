#unconditional statement
#break
i = 10
while i > 0:
    if i == 5:
        break  # Exit the loop when i is 5
    print(i)
    i -= 1


# continue

i = 10
while i > 0:
    i -= 1
    if i == 5:
        continue  # Skip the iteration when i is 5
    print(i)



#pass
i = 10
while i > 0:
    if i == 5:
        pass  # Do nothing when i is 5
    print(i)
    i -= 1

