import subprocess


def detect():
    lsof_output = subprocess.check_output(["lsof", "-i", "4UDP"]).decode().split("\n")
    zoom_rows = [row for row in lsof_output if "zoom" in row]

    current_state = int(len(zoom_rows) > 1)  # 1 zoom process isn't a meeting
    device_state = None

    with open("/Volumes/CIRCUITPY/state", "r") as state_file:
        device_state = int(state_file.read())

    if device_state != current_state:
        with open("/Volumes/CIRCUITPY/state", "w") as state_file:
            state_file.write(str(current_state))


if __name__ == "__main__":
    detect()
