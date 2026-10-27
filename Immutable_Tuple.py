# Define the Immutable Tuple
# RAW SOC SYSTEM LOGS
# Format: [SEVERITY] | IP_ADDRESS | USERNAME | PORT | EVENT_STATUS
secure_ports=(22,80,443,3389)

raw_forensic_logs = [
"[critical] |  192.168.1.105 | Admin_User | 22 | failed_login",
   "[WARNING] |   10.0.0.50  | root | 443 | MALWARE_SIGNATURE_DETECTED ",
    "[CRITICAL] | 172.16.254.1  | unknown_user | 80 | SQL_INJECTION_ATTEMPT ",
    "[ALERT] | 192.168.1.200  | SYS_ADMIN | 3389 | UNAUTHORIZED_ACCESS ",
    "[WARNING] | 10.0.0.12  | test_acc | 8080 | brute_force_suspected "
]
#raw_ip = " 10.198.79.202 "

#print(raw_forensic_logs)
#count = 0 used to test how many times parts are printed.
for log in raw_forensic_logs:
    parts = log.strip().split(" | ")
    #severity = parts[0]
    #ip = parts[1]
    #username = parts[2]
    #port = parts[3]
    #event = parts[4]

    print(f"Attacker username: {parts[2]}, Attacker IP: {parts[1]}, Severity: {parts[0]}")

number = int(input("enter a port number: "))
#count = 0

if number in secure_ports:
    if number  == 22:
            print("port recognized")
            print("SSH - Secure remote login and administration of Linux/Unix systems")
            #count +=1
    elif number == 443:
            print("port recognized")
            print("HTTPS - Secure encrypted web traffic")
            #count+=1
    elif number == 80:
            print("port recognized")
            print("HTTP - Regular web traffic (not encrypted)")
            #count+=1
    elif number == 3389:
            print("port recognized")
            print("RDP - Remote Desktop Protocol for remotely controlling Windows computers")
            #count+=1
else:
    print(f" {number} is port is not secure")
    #count+=1

    
print("hello")
