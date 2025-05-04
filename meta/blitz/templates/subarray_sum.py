from typing import List

def subarray_sum(nums: List[int], k: int) -> int:
    # TODO: Implement the function
    pass


# -----------------------
# 🧪 Sample Test Cases
# -----------------------

def run_tests():
    print(subarray_sum([1, 1, 1], 2))    # Expected: 2
    print(subarray_sum([1, 2, 3], 3))     # Expected: 2
    print(subarray_sum([1, -1, 0], 0))    # Expected: 3
    print(subarray_sum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Expected: 4
    print(subarray_sum([1], 0))            # Expected: 0
    print(subarray_sum([], 0))             # Expected: 0
    print(subarray_sum([0,0,0,0,0], 0))    # Expected: 15  # (lots of zero subarrays)

if __name__ == "__main__":
    run_tests()

