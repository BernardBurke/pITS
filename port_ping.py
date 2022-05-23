import helpers
import asyncio


def test_a_port(ipAddress,port):
    loop = asyncio.get_event_loop()
    status = loop.run_until_complete(helpers.wait_host_port(ipAddress,port,1,1))
    print(f"status {status} ip {ipAddress}")


ipList = helpers.get_subnet_addresses('172.23.16.1','20')



for ip in ipList:
#    print(f"testing {ip}")
    test_a_port(ip,80)

exit()

