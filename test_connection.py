import subprocess
import socket

def test_ping(host):
    try:
        # Try to ping the host
        result = subprocess.run(['ping', '-n', '1', host], 
                             capture_output=True, 
                             text=True)
        print("Ping test results:")
        print(result.stdout)
        return result.returncode == 0
    except Exception as e:
        print(f"Error during ping: {e}")
        return False

def test_port(host, port):
    try:
        # Try to establish a TCP connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(3)
        result = sock.connect_ex((host, port))
        sock.close()
        
        if result == 0:
            print(f"Port {port} is open")
            return True
        else:
            print(f"Port {port} is closed")
            return False
    except Exception as e:
        print(f"Error testing port: {e}")
        return False

if __name__ == "__main__":
    server = "192.168.19.214"
    sql_port = 1433  # Default SQL Server port
    
    print(f"\nTesting connectivity to {server}:")
    print("-" * 50)
    
    # Test ping
    print("\n1. Testing ping...")
    ping_result = test_ping(server)
    
    # Test SQL Server port
    print("\n2. Testing SQL Server port...")
    port_result = test_port(server, sql_port)
    
    if not ping_result and not port_result:
        print("\nNo connectivity to the server. Please check:")
        print("1. The server IP address is correct")
        print("2. The server is running")
        print("3. Your network can reach the server")
        print("4. Firewall settings allow the connection")
    elif not port_result:
        print("\nServer is reachable but SQL port is closed. Please check:")
        print("1. SQL Server is running")
        print("2. SQL Server is configured to accept remote connections")
        print("3. Firewall allows SQL Server port (default 1433)")
    else:
        print("\nServer appears to be accessible.")