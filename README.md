# Raspberry Pi 4 USB LED controller
![image](https://github.com/maxwalks/rpiLed/assets/78441835/732e9f2c-cf65-46b0-9574-282196d7b9df)
Control a USB LED strip with a Raspberry Pi 4 using Apache, Flask and uhubctl

## Preparations
### Set permissions for uhubctl:
```
sudo nano /etc/udev/rules.d/52-usb.rules
```
```
SUBSYSTEM=="usb", DRIVER=="usb", MODE="0666"
# Linux 6.0 or later (its ok to have this block present for older Linux kernels):
SUBSYSTEM=="usb", DRIVER=="usb", \
  RUN="/bin/sh -c \"chmod -f 666 $sys$devpath/*-port*/disable || true\""
SUBSYSTEM=="usb", DRIVER=="usb", MODE="0666"
SUBSYSTEM=="usb", DRIVER=="usb", MODE="0666"
```
### Add permitted users to dialout group:
```
sudo usermod -a -G dialout $USER
```
Reboot for the changes to take effect.

## Installation

### Install necessary tools
```
sudo apt install git apache2 libapache2-mod-wsgi-py3 pip virtualenv
```
Change configuration:
```
sudo nano /etc/apache2/sites-available/000-default.conf
```
Comment out ServerAdmin webmaster@localhost and Documentroot
This is how it should look like:
```
        #ServerAdmin webmaster@localhost
        #DocumentRoot /var/www/html

        WSGIScriptAlias / /var/www/html/rpiLed/app.wsgi
        <Directory /var/www/html/rpiLed>
          Order allow,deny
          Allow from all
        </Directory>
```
### Install rpiLed
```
cd /var/www/html && sudo rm index.html && sudo pip install flask && sudo git clone https://github.com/maxwalks/rpiLed.git && cd rpiLed && sudo virtualenv venv
```
