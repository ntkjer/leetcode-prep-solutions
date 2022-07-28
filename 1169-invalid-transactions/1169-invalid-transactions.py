class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        people = []
        time = []
        amount = []
        location = []
        
        
        for transaction in transactions:
            person, t, amt, city = transaction.split(',')
            people.append(person)
            time.append(t)
            amount.append(amt)
            location.append(city)
            
        n = len(transactions)
        invalid = [False] * n
        
        for i in range(n):
            for j in range(i + 1, n):
                if int(amount[j]) > 1000:
                    invalid[j] = True
                if int(amount[i]) > 1000:
                    invalid[i] = True
                if people[i] == people[j]:
                    time_diff = abs(int(time[j]) - int(time[i]))
                    if time_diff <= 60 and location[i] != location[j]:
                        invalid[i] = True
                        invalid[j] = True
                        
        res = list()        
        for i in range(n):
            if invalid[i]:
                res.append(transactions[i])
                        
        return res