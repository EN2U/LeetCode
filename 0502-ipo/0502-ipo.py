class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        new_list = [(i, capital[i], profits[i]) for i in range(len(profits))]

        new_list.sort(key=lambda tuple: tuple[1])

        tmp_list = []

        idx = 0
        while k != 0 and idx < len(new_list):
            if w >= new_list[idx][1]:
                tmp_list.append((idx, new_list[idx][1], new_list[idx][2]))
            elif not tmp_list:
                return w
            else:
                tmp_list.sort(key=lambda tuple: tuple[2])
                w += tmp_list.pop(-1)[2]
                k -= 1
                continue

            idx += 1

                
        if tmp_list and k != 0:
            tmp_list.sort(key=lambda tuple: tuple[2])
            while tmp_list:
                if k  == 0:
                    break
                w += tmp_list.pop(-1)[2]
                k -= 1

        return w