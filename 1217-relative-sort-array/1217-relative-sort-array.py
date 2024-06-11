class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hashmap = {value: 0  for value in arr2}

        last_elements = []
        for value in arr1:
            if value in hashmap:
                hashmap[value] += 1
            else:
                last_elements.append(value)

        final_list = []

        for key, value in hashmap.items():
            final_list.extend([key]*value)

        final_list.extend(sorted(last_elements))

        return final_list