class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def validateIPv4(ip):
            data = ip.split(".")
            for block in data:
                if not (1 <= len(block) <= 4):
                    return "Neither"
                if len(block) > 1 and block[0] == "0":
                    return "Neither"
                if not(block.isdigit()):
                    return "Neither"
                if not(0 <= int(block) <= 255):
                    return "Neither"
            return "IPv4"
        
        def validateIPv6(ip):
            hexChars = "abcdefABCDEF0123456789"
            hexCheck = set([char for char in hexChars])
            
            data = ip.split(":")
            for block in data:
                if not (1 <= len(block) <= 4): 
                    return "Neither"
                for x in block:
                    if x not in hexCheck: 
                        return "Neither"
                    
            return "IPv6"
        
        if queryIP.count(".") == 3:
            return validateIPv4(queryIP)
        elif queryIP.count(":") == 7:
            return validateIPv6(queryIP)
        else:
            return "Neither"
        
        