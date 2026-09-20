target, *nums = map(int, input().split())
lo, hi = 0, len(nums) - 1
answer = -1
while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] == target:
        answer = mid
        break
    if nums[mid] < target:
        lo = mid + 1
    else:
        hi = mid - 1
print(answer)
