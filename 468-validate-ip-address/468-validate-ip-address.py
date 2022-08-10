class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def validIPv4(ip):
            ip = ip.split(".")
            for x in ip:
                if len(x) == 0 or len(x) > 3:
                    return False
                if x[0] == "0" and len(x) != 1 or not x.isdigit() or int(x) > 255:
                    return False
            return True
        
        def validIPv6(ip):
            hexChars = "abcdefABCDEF0123456789"
            hexSet = set([c for c in hexChars])
            ip = ip.split(":")
            
            if len(ip) < 8:
                return False
            for block in ip:
                if not (1 <= len(block) <= 4):
                    return False
                for c in block:
                    if c not in hexSet:
                        return False
            return True
        
        if queryIP.count('.') == 3 and validIPv4(queryIP):
            return "IPv4"
        elif queryIP.count(':') == 7 and validIPv6(queryIP):
            return "IPv6"
        else:
            return "Neither"