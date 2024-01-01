import psutil
import time

def get_system_stats():
    cpu_usage = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    memory_avail = memory.available / (1024 * 1024 * 1024)
    net_io = psutil.net_io_counters()
    bytes_sent = net_io.bytes_sent / (1024 * 1024)
    bytes_received = net_io.bytes_recv / (1024 * 1024)

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Available Memory: {memory_avail:.2f} GB")
    print(f"Bytes Sent: {bytes_sent:.2f} MB")
    print(f"Bytes Received: {bytes_received:.2f} MB")
    print("-" * 20)

def main():
    while True:
        get_system_stats()
        time.sleep(5)

if __name__ == "__main__":
    main()
