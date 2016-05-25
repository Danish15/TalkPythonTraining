def fibonacci(limit):
	nums = []

	current= 0
	next = 1


	while current < limit:
		current, next = next, next + current
		nums.append(current)

	return nums



print(fibonacci(100)):
	print(n, end=', ')