from sets import Set

'''
Given an number array ([1, 2, 3, 4, 4])
Find a pair that summed resolves to a value (i.e. 8)
@see pair_sum_test.py
'''
def has_pair_with_sum(data, sum):
	set = Set()

	for value in data:
		if (value in set):
			return True

		set.add(sum - value)

	return False