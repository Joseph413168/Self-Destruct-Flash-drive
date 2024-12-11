import os

def disable_usb(drive_letter):
    os.system(f"diskpart /s disable_usb.txt")  # This can be an automated diskpart script
