import socket
import re
import time


def scan_port(network_address):
    popular_ports = {
        80: 'HTTP',
        443: 'HTTPS',
        22: 'SSH',
        21: 'FTP',
        25: 'SMTP',
        110: 'POP3',
        143: 'IMAP',
        53: 'DNS',
        23: 'Telnet',
        161: 'SNMP',
        389: 'LDAP',
        8443: 'HTTPS (alt)',
        3306: 'MySQL',
        5432: 'PostgreSQL',
        3389: 'RDP',
        5900: 'VNC'
    }
    base_network_address = re.search("\d+\.\d+\.\d+\.", network_address)
    start_index = base_network_address.end()
    for i in range(1, 254):
        start_time = time.time()
        ip_check = network_address[:start_index] + str(i)
        target = socket.gethostbyname(ip_check)
        print("Checking {} ...".format(target))
        for port in range(1, 65536):
            if port % 1000 == 0:
                print(port)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.001)
            check_open = connection.connect_ex((target, port))
            if check_open == 0:
                message = "Open port {} on ip {}".format(port, ip_check)
                if port in popular_ports.keys():
                    message += " with {}".format(popular_ports[port])
                print(message)
            connection.close()
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    scan_port("192.168.226.0")
    print("\n\nDone\n\n")
