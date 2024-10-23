numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

min_value = min(numbers)
print("Minimum value:", min_value)

max_value = max(numbers)
print("Maximum value:", max_value)

num_to_count = int(input("Enter the number to count: "))
count_num = numbers.count(num_to_count)
print("Occurrences of", num_to_count, ":", count_num)

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

total_sum = sum(numbers)
print("Sum of all elements:", total_sum)