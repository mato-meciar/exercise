import sys
import nmap3

# check if argument is present
if len(sys.argv[1:]) != 1:
    exit(Exception('Missing argument, exiting...'))

nmap = nmap3.Nmap()
# since it wasn't specified if only open ports are of interest we'll take only the open ones into consideration
# results = nmap.scan_top_ports(sys.argv[1])
results = nmap.scan_top_ports(sys.argv[1], args='--open')

for ip in results.keys():
    if ip not in ['runtime', 'stats', 'task_results']:
        print(ip)
        for portsForIp in range(len(results[ip]['ports'])):
            port = results[ip]['ports'][portsForIp]['portid']
            protocol = results[ip]['ports'][portsForIp]['protocol']
            state = results[ip]['ports'][portsForIp]['state']
            print(f"* {port}/{protocol} {state}")
