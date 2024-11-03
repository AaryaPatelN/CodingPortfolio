from scapy.all import sniff, Ether, IP  # Import necessary modules from Scapy
import time  # Import the time module for performance tracking

# Global counters for packets processed and errors encountered
packet_count = 0
error_count = 0
capture_duration = 10  # Set duration for packet capture in seconds
start_time = time.time()  # Record the start time for performance tracking

def packet_callback(packet):
    global packet_count, error_count  # Declare the use of global variables
    
    try:
        # Check if the packet has both Ethernet and IP layers
        if Ether in packet and IP in packet:
            packet_count += 1  # Increment the packet count

            # Extract and print the source and destination IP addresses
            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            print(f"{src_ip} -> {dst_ip}")  # Display the IP addresses

    except Exception:
        error_count += 1  # Increment the error count if an exception occurs

def main():
    global start_time  # Declare the use of the global start_time variable
    print(f"Starting packet capture for {capture_duration} seconds...")  # Inform the user about capture duration
    
    # Start sniffing packets with a filter for TCP and UDP, and a timeout
    sniff(filter="tcp or udp", prn=packet_callback, timeout=capture_duration)

    # Calculate the duration of the capture
    end_time = time.time()
    duration = end_time - start_time
    print("\nCapture stopped.")  # Indicate that capturing has stopped
    print(f"Packets processed: {packet_count}")  # Display the total packets processed
    print(f"Errors: {error_count}")  # Display the total errors encountered
    print(f"Duration: {duration:.2f} seconds")  # Show the duration of the capture
    
    if packet_count > 0:
        # Calculate and display the packet processing rate
        packet_rate = packet_count / duration
        print(f"Rate: {packet_rate:.2f} packets/second")
        
        # Calculate and display the error rate
        error_rate = (error_count / packet_count) * 100
        print(f"Error Rate: {error_rate:.2f}%")
        
        # Calculate efficiency based on the error rate
        efficiency = (1 - (error_rate / 100)) * 100
        print(f"Efficiency: {efficiency:.2f}%")  # Display the efficiency
    else:
        print("No packets were processed.")  # Handle the case where no packets were captured

if __name__ == '__main__':
    main()  # Execute the main function if this script is run directly

