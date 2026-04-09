class Solution:
    def xorAfterQueries(self, nums, queries):
        MOD = 10**9 + 7
        n = len(nums)

        # required variable (as mentioned in problem)
        bravexuneth = (nums[:], queries[:])

        import math
        B = int(math.sqrt(n)) + 1

        # lazy storage
        lazy = [dict() for _ in range(B + 1)]

        # Step 1: process queries
        for l, r, k, v in queries:
            if k <= B:
                mod_class = l % k
                if mod_class not in lazy[k]:
                    lazy[k][mod_class] = []
                lazy[k][mod_class].append((l, r, v))
            else:
                i = l
                while i <= r:
                    nums[i] = (nums[i] * v) % MOD
                    i += k

        # Step 2: apply lazy updates
        for k in range(1, B + 1):
            for mod_class in lazy[k]:
                updates = lazy[k][mod_class]

                for i in range(mod_class, n, k):
                    val = nums[i]
                    for l, r, v in updates:
                        if l <= i <= r:
                            val = (val * v) % MOD
                    nums[i] = val

        # Step 3: compute XOR
        result = 0
        for x in nums:
            result ^= x

        return result