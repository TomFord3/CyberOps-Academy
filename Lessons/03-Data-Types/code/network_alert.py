######################################################################## 
# Lesson 3: Data Types and Networking
# Author: Tom Hagan III
# Date: 07/10/26
# 
# Purpose: This program collects and displays network alert information
# and stores them using different data types in Python.
########################################################################

source_ip = input("Enter the source IP address: ") # String
destination_ip = input("Enter the destination IP address: ") # String
destination_port = int(input("Enter the destination port: ")) # Integer
packet_count = int(input("Enter the packet count: ")) # Integer
risk_score = float(input("Enter the risk score (as a decimal): ")) # Float
connection_allowed = input("Is the connection allowed? (yes/no): ")

print()
print("========== Network Alert ==========")
print(f"Source IP:          {source_ip}")
print(f"Destination IP:     {destination_ip}")
print(f"Destination Port:   {destination_port}")
print(f"Packet Count:       {packet_count}")
print(f"Risk Score:         {risk_score}")
print(f"Connection Allowed: {connection_allowed}")