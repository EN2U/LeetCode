class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()

        invalid = False
        while hand and not invalid:
            current_value = hand[0]
            hand.pop(0)
            for value in range(groupSize - 1):
                current_value += 1

                try:
                    next_idx = hand.index(current_value)
                except ValueError:
                    invalid = True
                    break
                
                hand.pop(next_idx)
            
        return not bool(hand)