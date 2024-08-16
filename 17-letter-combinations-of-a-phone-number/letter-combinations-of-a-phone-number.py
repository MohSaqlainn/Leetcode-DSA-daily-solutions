class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }


        res = []

        if not digits:
            return res

        def backtrack(indx, curr_res):
            if indx == len(digits):
                res.append("".join(curr_res))
                return

            digit = digits[indx]
            temp_array = phone[digit]

            for char in temp_array:
                curr_res.append(char)
                backtrack(indx+1, curr_res)
                curr_res.pop()
        
        backtrack(0, [])
        return res


            
        
