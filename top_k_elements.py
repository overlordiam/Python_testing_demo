from typing import List


class TopKElements:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1

        # Sort items by frequency in descending order
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1], reverse=True)

        # Extract the first k elements' keys
        top_k_elements = [item[0] for item in sorted_items[:k]]

        return top_k_elements
