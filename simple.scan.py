import pydnsbl

ip = str(input("insert an ip: "))
print()
ip_checker = pydnsbl.DNSBLIpChecker()
blacklist = ip_checker.check(f'{ip}')
print(blacklist)
print()
print("thanks for using my script, visit www.davenisc.com")
