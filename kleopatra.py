import subprocess

# reset YubiKey to recognise card, enable decryption and encryption on command line so
# Kleopatra can perform operations
commands = [
    'systemctl restart pcscd',
    'gpg --card-status',
    'gpg --output test.pdf --decrypt test.gpg',         # the file type will depend on 
                                                        # what test file you encrypted
    'echo "test" | gpg --clearsign'
]

for command in commands:
    try:
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error {e.returncode}.")

print("You should now be able to start up Kleopatra and encrypt/sign/decrypt/verify and recognise the YubiKey as a smart-card.")
