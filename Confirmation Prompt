def self_destruct(drive_letter):
    # Safety confirmation
    confirmation = input("Are you sure you want to activate the self-destruct? (yes/no): ")
    if confirmation.lower() == "yes":
        print(f"Initiating self-destruct on {drive_letter}:")
        os.system(f"del /f /q {drive_letter}:\\*.*")
        os.system(f"format {drive_letter}: /Q /Y")
    else:
        print("Self-destruct canceled.")
