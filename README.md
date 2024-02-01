Kleopatra for Windows works fine: it recognises my YubiKey as a smart-card and is able to encrypt/sign/decrypt and verify without issue. Kleopatra for Fedora Silverblue on the other hand:

1. Fedora Silverblue often did not recognise the YubiKey (upon boot it seems to hog the YubiKey and does not let go). I had to manually reset the pcscd service on the command line to get gpg --card-status to recognise the card; and
2. Kleopatra was working only after first manually decrypting and encrypting a file on the commmand line. Even this functionality ran into problems at some point with an inappropriate ioctl for device failure. Deleting the flatpak from registry.fedoraproject.org and installing the flatpak from dl.flathub.org restored functionality with the added bonus that the UI was now in dark mode to reflect the rest of GNOME. The working flatpak version is 3.1.28.230804. The broken flatpak from registry.fedoraproject.org was 2 months old instead of 1 month old (but now seems to have been updated–I have not tried it out).

Rather than copy/pasting a whole series of commands on the command line, I created a tiny python program to do everything so that I could use Kleopatra normally. **You need to encrypt a junk file and call it test.gpg (and modify the code below the reflect the file type so that a pdf would be .pdf, a text file would be .txt for example).**

At the command line “python kleopatra.py” will now do all the prep to enable Kleopatra to work in Fedora Silverblue. Make sure you have a encrypted junk file named “test.gpg” in the same directory as your python file. The python program:

-restarts the pcscd service so the YubiKey is recognised in Fedora Silverblue (I needed to authenticate via fingerprint);
-decrypts a test file (I encrypted a pdf file so the decrypted file is named test.pdf–you will need to adjust the file type to suit your test file type) during which a popup will ask for the YubiKey PIN; and
-encrypts by echo test during which the YubiKey PIN will be asked again.


Blog post: https://felixquinihildebet.wordpress.com/2024/02/01/kleopatra-for-fedora-silverblue-one-solution/
