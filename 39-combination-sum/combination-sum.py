class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Sorting enables early stopping (pruning)

        def backtrack(remaining: int, combo: list[int], start_index: int):
            if remaining == 0:
                res.append(list(combo))
                return

            for i in range(start_index, len(candidates)):
                # If the candidate exceeds remaining target, break early since array is sorted
                if candidates[i] > remaining:
                    break

                combo.append(candidates[i])
                # Pass 'i' instead of 'i + 1' to allow reusing the same element
                backtrack(remaining - candidates[i], combo, i)
                combo.pop()

        backtrack(target, [], 0)
        return res