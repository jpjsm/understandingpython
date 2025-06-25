# Enabling VSCode Remote Viewing of PIL img.show

***WARNING*** IT TAKES ABOUT 30 ~ 60 SECONDS TO SEND THE IMAGE

## On Windows Side

-  From: https://sourceforge.net/projects/xming/ install X-server
-  Once server is installed, start the server with `XLaunch`
  1. ![Xming_Launch1.png](./img/Xming_Launch1.png)
  1. ![Xming_Launch2.png](./img/Xming_Launch2.png)
  1. ![Xming_Launch3.png](./img/Xming_Launch3.png)
  1. ![Xming_Launch4.png](./img/Xming_Launch4.png)
- Find the log file in ***hidden icons***
  1. ![Xming_HiddenIcons1.png](./img/Xming_HiddenIcons1.png)
  1. ![Xming_HiddenIcons2.png](./img/Xming_HiddenIcons2.png)
  1. ![Xming_HiddenIcons3.png](./img/Xming_HiddenIcons3.png)
-  Update user environment with `DISPLAY=...` value as seen in the log file  
![Xming_log.png](./img/Xming_log.png)
  1. From ***Control Panel*** open *Allow remote access*, select *Advanced* tab, and click on **Environment Variables**:  
  ![Xming_DisplayVarSetup.png](./img/Xming_DisplayVarSetup.png)
- **Restart Windows** 

## On Linux side (Ubuntu 24)

- `sudo apt update && sudo apt -y upgrade`
- `sudo apt install libpng-dev libjpeg-dev libtiff-dev`
- `sudo apt install imagemagick`
- `convert --version`  
![Ubuntu_ImageMagickVerification.png](./img/Ubuntu_ImageMagickVerification.png)
- `sudo vi /etc/ssh/sshd_config`
  - Uncomment `X11Forwarding yes`, or if the line is not there add it to the end of the file.
- `sudo reboot now`

## On VSCode configuration

- ![VSCode_RemoteSettings1.png](./img/VSCode_RemoteSettings1.png)
- ![VSCode_RemoteSettings2.png](./img/VSCode_RemoteSettings2.png)
- ![VSCode_RemoteSettings3.png](./img/VSCode_RemoteSettings3.png)
- Close all instances of VSCode
- Reopen VSCode