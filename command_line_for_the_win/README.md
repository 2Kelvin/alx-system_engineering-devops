# Command line for the win challenge

## Steps to uploading screenshots (files) from your local machine to the sandbox (remote machine) using SFTP

- [x] On your side menu, click the sandbox icon
- [x] On the alx sandbox page click on the `SFTP` button
- [x] Open your terminal app and paste what you just copied from clicking the SFTP button above
- [x] Type `pwd` to check your current working directory on the sandbox
- [x] To access the screenshots you saved on your local machine, type `lpwd` to print the current working directory of your local machine and then navigate to where your screenshots are located
- [x] You can upload all the screenshots at once to your sandbox's current working directory by typing `put -r <folder-name>`. Where *folder-name* is the folder containing ONLY and all your project screenshots
- [x] If upload was successful, type *ls* again and you'll see a new directory *folder-name* in your sandbox containing all the screenshots for your project
- [x] And that's just about it, easy peesy.

Remember to move your screenshots to the sandbox directory `/root/alx-system_engineering-devops/command_line_for_the_win`

Checkout [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-use-sftp-to-securely-transfer-files-with-a-remote-server) for a quick tutorial on using **SFTP**
