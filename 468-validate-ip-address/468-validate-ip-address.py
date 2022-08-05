class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isValidIPv4(ip):
            ip = ip.split(".")
            for x in ip:
                if len(x) == 0 or len(x) > 3:
                    return False
                if x[0] == "0" and len(x) != 1 or \
                not x.isdigit() or int(x) > 255:
                    return False
            return True
        
        def isValidIPv6(ip):
            hexChars = "1234567890abcdefABCDEF"
            hexRange = set([x for x in hexChars])
            ip = ip.split(":")
            if len(ip) < 8:
                return False
            for block in ip:
                if not (1 <= len(block) <= 4):
                    return False
                for c in block:
                    if c not in hexRange:
                        return False
            return True
        
        
        if queryIP.count(".") == 3 and isValidIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(":") == 7 and isValidIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
        