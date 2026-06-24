import time
import random

class NetworkSimulator:
    def __init__(self, technology):
        self.technology = technology
        if technology == "LTE":
            self.max_speed = 100  # Mbps
            self.latency = 50     # ms
            self.reliability = 0.98 # 98%
        elif technology == "5G":
            self.max_speed = 1000 # Mbps
            self.latency = 5      # ms
            self.reliability = 0.999 # 99.9%
        else:
            raise ValueError("Unsupported technology")

    def simulate_connection(self, data_size_mb):
        # Simulate network conditions based on technology
        actual_speed = self.max_speed * random.uniform(0.5, 1.0) # Simulate variable speed
        simulated_latency = self.latency * random.uniform(0.8, 1.2) # Simulate variable latency
        
        # Check reliability
        if random.random() > self.reliability:
            print(f"[{self.technology}] Connection failed due to instability.")
            return None, None

        # Calculate download time
        data_size_bits = data_size_mb * 8 * 1024 * 1024 # Convert MB to bits
        speed_bits_per_sec = actual_speed * 1000 * 1000 # Convert Mbps to bits/sec
        download_time_sec = data_size_bits / speed_bits_per_sec

        # Total time is download time + latency
        total_time_sec = download_time_sec + (simulated_latency / 1000) # Convert ms to sec

        return total_time_sec, simulated_latency

# --- Demonstration ---

print("Simulating network performance for LTE and 5G...")

# Initialize simulators
console_lte = NetworkSimulator("LTE")
console_5g = NetworkSimulator("5G")

# Data size to download (e.g., a large video file)
data_to_download = 500 # MB

print(f"\n--- Downloading {data_to_download} MB ---")

# Simulate LTE connection
print(f"\nSimulating LTE...")
lte_time, lte_latency = console_lte.simulate_connection(data_to_download)
if lte_time is not None:
    print(f"LTE Download Time: {lte_time:.2f} seconds")
    print(f"LTE Simulated Latency: {lte_latency:.2f} ms")

# Simulate 5G connection
print(f"\nSimulating 5G...")
five_g_time, five_g_latency = console_5g.simulate_connection(data_to_download)
if five_g_time is not None:
    print(f"5G Download Time: {five_g_time:.2f} seconds")
    print(f"5G Simulated Latency: {five_g_latency:.2f} ms")

print("\nLTE remains crucial for broad coverage and as a fallback, even as 5G offers superior speed and lower latency for specific use cases.")
