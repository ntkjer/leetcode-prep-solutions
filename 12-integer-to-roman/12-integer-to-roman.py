class Solution:
    def intToRoman(self, num: int) -> str:
        
        digits = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), 
                  ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)]
        
        roman = []
        for symbol, digit in digits:
            if num == 0:
                break
                
            freq = 0
            while num >= digit:
                freq += 1
                num = num - digit
                
            if freq:
                roman.append(freq * symbol)
            
            
        return "".join(roman)