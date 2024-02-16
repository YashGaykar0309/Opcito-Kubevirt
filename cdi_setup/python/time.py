import subprocess
import time

def ping_ip(ip_address):
    try:
        start_time = time.time()

        while True:
            # Ping the IP address
            result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)

            # Check the result
            if "1 packets transmitted, 1 packets received" in result.stdout.decode('utf-8'):
                print(f"Successfully pinged {ip_address} in {time.time() - start_time:.2f} seconds.")
                break
            else:
                # Print the result for unsuccessful pings
                print(result.stdout.decode('utf-8'))

            # Wait for one minute before the next ping attempt
            time.sleep(60)

    except KeyboardInterrupt:
        print("Ping script terminated by user.")

if __name__ == "__main__":
    target_ip = "10.244.0.18"

    print(f"Pinging {target_ip} until successful...")
    ping_ip(target_ip)

