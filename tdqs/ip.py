class IP4:
    def validIPAddress(self, IP):
        ip4 = IP.split(".")
        if len(ip4) == 4:
            for num in ip4:
                try: 
                    # if not (num[0].isdigit() and int(num) < 256 and (num[0] != "0" or num == "0") and num[-1].isdigit()):
                    if not (str(num).isdigit() and int(num)<256 and int(num) >= 0):
                        return False
                except: 
                    return False
            return True
        return False

    #
    def ip2num(self, ip):
        return sum([int(j) << ((3 - i) * 8) for i, j in enumerate(ip.split('.'))])

    def validIP(self, s: str):
        t = s.split('-')
        if len(t) == 1:
            return self.validIPAddress(t[0])
        else:
            if self.validIPAddress(t[0]) and self.validIPAddress(t[1]):
                print(self.ip2num(t[0]) , self.ip2num(t[1]))
                return self.ip2num(t[0]) < self.ip2num(t[1])
            return False

print(IP4().validIP("0.254.0.0"))
print(IP4().validIP("10.0.0.0-10.255.255.255"))
print(IP4().validIP("172.32.0.0-172.31.255.255"))
print(IP4().validIP("255.0.0.0-192.192.255.255"))
print(IP4().validIP("255.0.0.0-254.255.255.255"))
# 1.1.1.1 > 000100100010001
