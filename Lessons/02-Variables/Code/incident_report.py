##############################################
# Project: Incident Report Generator
# Lesson: 02 - Variables
# Author: Tom Hagan III
# Date: 07/9/26
# Purpose: This program generates an incident report based on user input.
# Practice storing and collecting cybersecurity incident information in variables and printing them to the console.
##############################################


# Store incident information in variables
# These variables simulate information collected during a SOC investigation after a firewall alert.
ip_address = input("Enter the IP address: ")
domain = input("Enter the domain: ")
timestamp = input("Enter the timestamp: ")
username = input("Enter the username: ")
hostname = input("Enter the hostname: ")
severity = input("Enter the severity: ")
case_id = input("Enter the case ID: ")
alert = input("Enter the alert: ")

# Display the incident report
print("========== Incident Report ==========")
print()

print(f"Case ID:     {case_id}")
print(f"IP Address:  {ip_address}")
print(f"Username:    {username}")
print(f"Hostname:    {hostname}")
print()

print(f"Severity:    {severity}")
print(f"Alert:       {alert}")
print()

print(f"Domain:      {domain}")
print(f"Timestamp:   {timestamp}")

print()
print("=========== End of Report ===========")