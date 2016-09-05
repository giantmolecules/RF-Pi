# Setup

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

