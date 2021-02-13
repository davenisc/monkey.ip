import pydnsbl


ip_checker = pydnsbl.DNSBLIpChecker()

with open('ips.txt') as file:
    ips = file.read().splitlines()

    for ip in ips:
        if ip_checker.check(ip).blacklisted:
            blacklist = ip_checker.check(f'{ip}')

            print(f"{ip} blacklisted")
            print(blacklist)
            print()
print()
print("thanks for using my script, visit www.davenisc.com")
