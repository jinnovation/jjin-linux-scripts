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

## unzip_dir ##
* `unzip` to directory of same name as archive
* Really just a convenience script; no unique/complicated logic

## timec ##
* Library of Python functions focused around automating: 
	* The compilation of C source code and 
	* The collection of a large sample size of execution times of the resulting
      executable
* Was written to facilitate data collection for my final project for `CMSC 22200
  Computer Architecture`
* When executed by itself, returns mean and standard deviation information
  regarding execution time sampling of the program

## timec_stats ##
* Python script that:
	* Compiles C source code,
	* Executes the resulting executable a user-specified number of times,
      recording the execution time of each trial,
	* Outputs relevant metrics (mean, standard deviation, and a fancy Normal
      plot of the resulting distribution), and finally
	* "Garbage collects" (by which I really mean it just deletes the executable)
* Was written to facilitate data collection for my final project for `CMSC
  22200 Computer Architecture`
* Uses the functions from `timec`
* **Work in progress**. The implementation is still very hacky and tied into
  the specific needs of my project at the time; it uses a multitude of
  hard-coded values that probably would render this script unuseable outside of
  my directory tree. As such, *I would not recommend using this right now.* Of
  course, feel free to take it and modify it to suit your needs; sharing is
  caring. 
