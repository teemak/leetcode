var threeSum = function (nums) {
    if (!nums) return []
    let result = []
    nums.sort((a, b) => a - b)
    let i = 0

    while (i < nums.length - 2) {

        let left = i + 1
        let right = nums.length - 1

        while (left < right) {
            let currSum = nums[i] + nums[left] + nums[right] // -1

            if (currSum === 0) {
                result.push([nums[i], nums[left], nums[right]])
                if (nums[i] === nums[i + 1]) {
                    while (nums[i] === nums[i + 1]) {
                        i++
                    }
                }

                while (left < right && nums[left] === nums[left + 1]) {
                        left++
                    }
                while (left < right && nums[right] === nums[right - 1]) {
                    right--
                }
                left++
                right--
            } else if (currSum < 0) {
                if (nums[left] === nums[left + 1]) {
                    while (left < right && nums[left] === nums[left + 1]) {
                        left++
                    }
                } else {
                    left++
                }
                // left++
            } else {
                if (nums[right] === nums[right - 1]) {
                    while (left < right && nums[right] === nums[right - 1]) {
                        right--
                    }
                } else {
                    right--
                }
                // right--
            }
        }
        i++
    }

    return result
}