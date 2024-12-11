import os
import time

# Function to check if the USB device is plugged in
def detect_usb(drive_letter):
    while True:
        if os.path.exists(drive_letter + ':'):
            print(f"USB detected at {drive_letter}:")
            break
        time.sleep(1)

# Monitor the USB drive
def monitor_usb():
    usb_drive_letter = 'E'  # Replace this with the correct drive letter for your USB
    print("Monitoring USB drive...")
    detect_usb(usb_drive_letter)
    # Once USB is detected, call the trigger function or wait for remote activation

if __name__ == "__main__":
    monitor_usb()
