## File Description
### config.ini
- This file contains the configuration of the system and needs to be edited acordingli if the server IP or Web Server port or defaut image of ID of the device changes.

### utilities.py
- This file was created to store the working directory of the Project as when the service of the systemmd is running it needs absolute path and not relative path. so this file is needed to read the config.ini file

### display.py
- This file is to use tkinter to diplay the image and update the image and so on

### rabbitmqclient.py
- This file handles everything related to rabbitmq communication

### getimage.py
- This file deals with getting image and all from the HTTP Server and so on

### Log.py
- [Under Development] This file deals with initialising logger and chaining logging handler and so on

### oplclient.service
- This is the service file for systemmd that creates a service of this program in linux and enables to run on startup

### multiprocess.py
- This is the main executeable program which create two threads. One thread displays the program amd the other thread checks the rabbitmq and http for image update and stuff

### execute.sh
- This bash script execute the main program from within the environment

### debug.sh
- This script copyts the .service file in /etc/systemd/system and reloads the systemd so that our new service is registered and starts the service.

## Deplyment Strategy
- From Home -> Preference -> Raspberry pi Configuration -> SSH enable (or sudo systemctl enable ssh)
- Git clone this repository
- create a virtual environment(env is the virtual environment in this repository)[python -m venv env]
- activate the virtual env [source env/bin/activate]
- Pip install all the packages from requirements.txt
- Update **config.ini**
- Update **utilities.py**
- Update **execute.sh**
- update **debug.sh**
- Update **oplclient.service**
- change permission of debug.sh to +x
- execute execute.sh - To check if things are working properly
- If yes :- then execute debug.sh
- The enable the service to run on startup with
	- sudo systemctl enable oplclient.service.
- Reboot (shutdown and restart)

## System Drawback:-
- As of now all ther servers must be running(HTTP and RABBITMQ) before starting the client. Once the client service starts running then even if the servier disconnects we can recover, bu inilitally things must be without any roadblock

