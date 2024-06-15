class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profit_capital = [(capital[i], profits[i]) for i in range(len(profits))]

        profit_capital.sort(key=lambda tuple: tuple[0])

        valid_capital_candidates = []

        idx = 0

        while k != 0 and idx < len(profit_capital):
            if w >= profit_capital[idx][0]:
                valid_capital_candidates.append((profit_capital[idx][0], profit_capital[idx][1]))
                idx += 1
                continue
            
            if not valid_capital_candidates:
                return w
            
            valid_capital_candidates.sort(key=lambda tuple: tuple[1])
            w += valid_capital_candidates.pop(-1)[1]
            k -= 1

    
        if valid_capital_candidates and k != 0:
            valid_capital_candidates.sort(key=lambda tuple: tuple[1])
            while valid_capital_candidates and k != 0:
                w += valid_capital_candidates.pop(-1)[1]
                k -= 1

        return w