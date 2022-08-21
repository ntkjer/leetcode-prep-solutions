class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        
        people = []
        time = []
        location = []
        amount = []
        
        for i in range(len(transactions)):
            transaction = transactions[i]
            name, t, amt, city = transaction.split(",")
            people.append(name)
            time.append(int(t))
            location.append(city)
            amount.append(int(amt))
        
        
        n = len(transactions)
        invalid = [False] * n
        
        for i in range(n):
            for j in range(i + 1, n):
                if amount[i] > 1000:
                    invalid[i] = True
                if amount[j] > 1000:
                    invalid[j] = True
                if people[i] == people[j]:
                    time_diff = abs(time[j] - time[i])
                    if time_diff <= 60 and location[i] != location[j]:
                        invalid[i] = True
                        invalid[j] = True
                        
        
        res = list()
        for i in range(n):
            if invalid[i]:
                res.append(transactions[i])
        
        return res