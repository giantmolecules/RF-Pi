Raspbian Jessie

//Install to SDHC card

# Software / Hardware Setup

//Change Password
> passwd

// Get package updates
> sudo apt-get update


// Install Aircrack-NG
> sudo apt-get install aircrack-ng

## Test
// kill processes that might interfere with putting interface in monitor mode
>sudo airmon-ng check kill

// put wlan1 into monitor mode
>sudo airmon-ng start wlan1

// check to see if mon0 exists
>iwconfig

## Install RTL-SDR

Edit the file /etc/modprobe.d/raspi-blacklist.conf and add the line:

blacklist dvb_usb_rtl28xxu

Install the rtl-sdr software and GNU Radio support:

$ sudo apt-get install rtl-sdr gr-osmosdr

