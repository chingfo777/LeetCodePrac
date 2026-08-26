class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()  # Sorting is required to handle duplicates and prune branches

        def backtrack(remaining: int, combo: list[int], start_index: int):
            if remaining == 0:
                res.append(list(combo))
                return

            for i in range(start_index, len(candidates)):
                # Skip duplicate elements at the same tree level to avoid duplicate combinations
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue

                # Early stop since the candidates array is sorted
                if candidates[i] > remaining:
                    break

                combo.append(candidates[i])
                # Move to i + 1 since each number can only be used once
                backtrack(remaining - candidates[i], combo, i + 1)
                combo.pop()

        backtrack(target, [], 0)
        return res