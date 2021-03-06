# Software / Hardware Setup

## Install OS

Raspbian Jessie

//Install to SDHC card

## Prepare

//Change Password

$ passwd

// Get package updates

$ sudo apt-get update

## Install Aircrack-NG

$ sudo apt-get install aircrack-ng

// kill processes that might interfere with putting interface in monitor mode

*This will kill processes for ALL adapters*

$ sudo airmon-ng check kill

// put wlan1 into monitor mode

$ sudo airmon-ng start wlan1

// check to see if mon0 exists

$ iwconfig

## [Install RTL-SDR](http://www.rs-online.com/designspark/electronics/eng/blog/taking-the-raspberry-pi-2-for-a-test-drive-with-gnu-radio-2)

Edit the file /etc/modprobe.d/raspi-blacklist.conf and add the line:

blacklist dvb_usb_rtl28xxu

Install the rtl-sdr software and GNU Radio support:

$ sudo apt-get install rtl-sdr gr-osmosdr

In order to access the device as a non-root user we need to set up a new udev rule, but first we need to ascertain the USB ID. Ensure that the tuner is plugged in and type:

$ lsusb
This gave me:

Bus 001 Device 004: ID 0bda:2832 Realtek Semiconductor Corp. RTL2832U DVB-T

Next we create the file /etc/udev/rules.d/20.rtlsdr.rules, with the line:

SUBSYSTEM=="usb", ATTRS{idVendor}=="0bda", ATTRS{idProduct}=="2832", GROUP="adm", MODE="0666", SYMLINK+="rtl_sdr"

We could restart udev at this point, but since we also blacklisted a kernel module it's probably just easiest to reboot.

$ sudo reboot

## Install python-scapy

$ sudo apt-get install python-scapy

[get this python script...](https://gist.github.com/giantmolecules/6da12e05c8e5b059215b04b7e577b8d5)

$ git clone https://github.com/giantmolecules/RF-Pi.git

$ cd 

## Test Scanning

$ sudo airmon-ng check kill

$ sudo airmon-ng start wlan1

$ sudo python scan.py mon0

## Install multimon

$ sudo reboot

$ sudo apt-get install multimon

## Build multimon -ng

# Install dependencies

$ sudo apt-get update

$ sudo apt-get -y install git cmake build-essential libusb-1.0 qt4-qmake libpulse-dev libx11-dev

## [Fetch and compile multimonNG](https://www.raspberrypi.org/forums/viewtopic.php?t=45142)

$ git clone https://github.com/EliasOenal/multimonNG.git

$ cd multimonNG

$ mkdir build

$ cd build

$ qmake ../multimon-ng.pro

$ make

$ sudo make install

## To get osmocom_fft to run

$ sudo nano /boot/config.txt

and add
framebuffer_depth=32
framebuffer_ignore_alpha=1

## X-Session over SSH

from OSX

$ ssh -X pi@192.168.#.#

once logged into pi

$ lxsession

*If no audio, change config.txt to hdmi_drive=2*
