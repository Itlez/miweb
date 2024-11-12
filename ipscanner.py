
import nmap
scanner = nmap.PortScanner()

ip = input("inserte una direccion IP")
print("Esta es la direccion ip que escribiste:", ip)
scanner.scan(ip)

print(scanner.all_hosts)