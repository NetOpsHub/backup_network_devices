
from p3_network_library import *;

def main():
    with open('hosts', 'r') as hosts_file_instance:
        for host in hosts_file_instance:
            telnet_client_instance = p3_telnetlib_library('cisco', host.strip(), 23, 'adm1n', '', '');
            if telnet_client_instance.connect() != False:
                with open('files/%s_%s' % (host.strip(),time_now()), 'w') as backup_file_instance:
                    backup_file_instance.write(telnet_client_instance.exec_configuration_file('network_device_backup_commands'));
                
main();
