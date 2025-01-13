def twoSum(nums: list, target: int) -> list:
    sums = dict()

    for index, num in enumerate(nums):
        difference = target - num

        if num in sums.keys():
            print(sums, num)
            return [sums[num], index]

        sums[difference] = index


a = twoSum([1, 2, 3, 4, 5, 7], 55)
print(a)
