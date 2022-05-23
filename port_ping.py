import helpers
import asyncio


ipList = helpers.get_subnet_addresses('172.23.16.1','24')

for ip in ipList:
    print(ip)

exit()

loop = asyncio.get_event_loop()
status = loop.run_until_complete(helpers.wait_host_port("www.google.com",80,1,1))

print("status", status)
