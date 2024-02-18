target = int(input()) # Enter a number between 0 and 1000
# 0 is not an even number

even_sum = 0
for number in range (2, target+1, 2): #start, stop, step size
 even_sum += number
print(even_sum)

