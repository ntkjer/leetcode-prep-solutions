from ipaddress import ip_address, IPv6Address

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def validate_ipv4(ip):
            nums = ip.split('.')
            for x in nums:
                if len(x) == 0 or len(x) > 3:
                    return "Neither"
                if x[0] == '0' and len(x) != 1 or not x.isdigit() or int(x) > 255:
                    return "Neither"
            return "IPv4"
        
        def validate_ipv6(ip):
            nums = ip.split(':')
            if len(nums) < 8:
                return "Neither"
            hexadigits = "0123456789abcdefABCDEF"
            hexa = set(digit for digit in hexadigits)
            for x in nums:
                if len(x) == 0 or len(x) > 4:
                    return "Neither"
                for c in x:
                    if c not in hexa: return "Neither"
            return "IPv6"
        
        if queryIP.count('.') == 3:
            return validate_ipv4(queryIP)
        elif queryIP.count(':') == 7:
            return validate_ipv6(queryIP)
        else:
            return "Neither"