# Table of Contents #

## ranwall ##
* Uses `feh` to change desktop wallpaper to a randomly chosen image
  
## ranwall_time ##
* Meant to be run as a daemon
* Uses the aforementioned `ranwall` script to automatically change desktop
  wallpaper at a given interval (minutes)
* Outputs any given errors to notification center

## ucvpn ##
* Uses `openconnect` to connect to the University of Chicago VPN network with
  the given username and password
* Sends success/failure messages to notification center
