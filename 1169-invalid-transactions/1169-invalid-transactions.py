class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        N = len(transactions)
        res = list()
        invalid = [False] * N
        parsed_transactions = [x.split(",") for x in transactions]
        
        for i in range(N):
            if int(parsed_transactions[i][2]) > 1000:
                invalid[i] = True
        
        
        for i in range(N):
            for j in range(i + 1, N):
                name1, time1, city1 = parsed_transactions[i][0], int(parsed_transactions[i][1]), parsed_transactions[i][3]
                name2, time2, city2 = parsed_transactions[j][0], int(parsed_transactions[j][1]), parsed_transactions[j][3]
                if name1 == name2 and 0 <= abs(time1 - time2) <= 60 and city1 != city2:
                    invalid[i] = True
                    invalid[j] = True
        
        for i in range(N):
            if invalid[i]:
                res.append(transactions[i])
                
        return res