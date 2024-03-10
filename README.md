# Raspberry Pi 4 USB LED controller
![image](https://github.com/maxwalks/rpiLed/assets/78441835/732e9f2c-cf65-46b0-9574-282196d7b9df)
Control a USB LED strip with a Raspberry Pi 4 using Apache, Flask and uhubctl

## Installation

### Clone Repository
```
sudo git clone https://github.com/maxwalks/rpiLed
```
### Install rpiLed
```
sudo bash run.sh
```

## autostart Chromium webpage
Install Chromium:
```
sudo apt install chromium-browser -y
```
```
cd .config
```
Make the following file:
```
sudo mkdir -p lxsession/LXDE-pi
```
Edit the following file:
```
sudo nano lxsession/LXDE-pi/autostart
```
Add this configuration:
```
@lxpanel --profile LXDE-pi
@pcmanfm --desktop --profile LXDE-pi
#@xscreensaver -no-splash
point-rpi
@chromium-browser --start-fullscreen --start-maximized http://{Ip address of the pi}
```
Reboot for changes to take effect.
