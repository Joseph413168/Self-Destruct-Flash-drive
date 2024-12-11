import logging

logging.basicConfig(filename='usb_self_destruct.log', level=logging.INFO)

def log_action(action):
    logging.info(f"{time.ctime()}: {action}")

# Example of logging self-destruct action
log_action(f"Self-destruct initiated on {usb_drive_letter}")
