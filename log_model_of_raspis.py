import os
import re
import subprocess

# Update these variables with your actual SSH credentials and folder path
username_for_host = None
password_for_host = None
folder = None

def get_tf_files(folder):
    return [
        os.path.join(folder, f) for
        f in os.listdir(folder) if f.endswith(".tf")
        ]


def extract_hostnames(tf_file):
    hostnames = set()
    with open(tf_file, "r") as f:
        content = f.read()
        # Find lines containing 'host_name' and extract the value
        for line in content.splitlines():
            match = re.search(r'host_name\s*=\s*"([^"]+)"', line)
            if match:
                hostnames.add(match.group(1))
    return hostnames


def connect_and_execute(hostname, command) -> str:
    putty_cmd = f"plink.exe -batch -ssh {username_for_host}@{hostname} -pw {password_for_host} -m temp_cmd.txt"
    # Write command to temp file
    with open("temp_cmd.txt", "w") as f:
        f.write(command)
    result = subprocess.run(putty_cmd, capture_output=True, text=True)
    os.remove("temp_cmd.txt")
    # Save the result to a file named after the hostname
    with open(f"{hostname}_result.txt", "w") as out_file:
        out_file.write(result.stdout)
    return result.stdout


def main(folder):
    tf_files = get_tf_files(folder)
    all_hostnames = set()
    for tf_file in tf_files:
        all_hostnames.update(extract_hostnames(tf_file))
    command = "cat /proc/device-tree/model"
    model_names_file = "model_names.txt"
    if os.path.exists(model_names_file):
        os.remove(model_names_file)
    just_model_names_file = "just_model_names.txt"
    if os.path.exists(model_names_file):
        os.remove(model_names_file)
    if os.path.exists(just_model_names_file):
        os.remove(just_model_names_file)
    for hostname in all_hostnames:
        print(f"Connecting to {hostname}...")
        model = connect_and_execute(hostname, command)
        with open(model_names_file, "a") as f:
            f.write(f"{hostname}: {model.strip()}\n")
        with open(just_model_names_file, "a") as f:
            f.write(model.strip() + "\n")


if __name__ == "__main__":    
    main(folder)
    print("Script executed successfully.")
