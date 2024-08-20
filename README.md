# R-DLD: Robotic-supported Data Loss Detection
Automatically Revealing Data Loss Bugs in Android Apps using a robot.

![R-DLD](build%20robot/robot/robot.jpg)

This repository is a companion page for the following publication:

> Davi Freitas, Breno Miranda, and Juliano Iyoda. 2024. Robotic-supported Data Loss Detection in Android Applications. SBES’24, September 30 – October 04, 2024, Curitiba, PR.


It includes all the necessary materials to replicate our experiments, such as: detailed steps for constructing the robot, implementing the robot on an Arduino board, the implementation of R-DLD, the applications used in the experiment, data loss alerts generated during the experiment, the bug report for data loss alerts, classification tables of the alerts, sub-classification tables of data loss, issue grouping tables, links to open issues, and their current status.

## Build Robot
[Robot parts](build%20robot/README.MD)


## Architecture
[Architecture](application/README.md)


## Install python 2.7
* wget https://www.python.org/ftp/python/2.7.18/Python-2.7.18.tgz
* tar xzf Python-2.7.18.tgz
* cd Python-2.7.18
* sudo ./configure --enable-optimizations
* sudo make altinstall
* sudo apt  install curl
* curl https://bootstrap.pypa.io/pip/2.7/get-pip.py -o get-pip.py
* sudo apt-get install libssl-dev
* sudo apt-get install --reinstall libpython2.7-stdlib libpython2.7-minimal libpython2.7
* sudo python2.7 get-pip.py
* python2.7 -m pip install virtualenv

## Install R-DLD
To install R-DLD follow these steps:
* git clone https://github.com/replication-papers/R-DLD.git
* cd cd R-DLD/application/R-DLD-Arduino/
* python2.7 -m virtualenv venv
* source venv/bin/activate
* cd droidbot-tool
* pip install -e .
* cd ..
* pip install -e .


### How to use the tool
R-DLD works via command line and requires only the apk file of the app to be tested. It is not necessary to be inside the R-DLD folder to start the tool. It is possible to set the execution time in terms of either time in seconds or number of events to be generated. 
1) Make sure you have an Android device opened and connected via ADB (check it out by typing **adb devices**)
2) Launch R-DLD by typing **dld -a <appname.apk> -o <output_folder>**. This is the most basic command to start R-DLD using the default settings. 
It is possible to add one or more customized settings:
   - **-robot**: parameter to enable rotation functionality using a robot
   - **-is_emulator**: add this option if you are using an Android Virtual Device
   - **-scroll_full_down_y \<number\>**: the y coordinate on the screen from which R-DLD starts to swipe up (1600 by default)
   - **-main_activity <activity_name>**: the activity used by R-DLD to start the app. Sometimes, R-DLD fails to get the correct main activity from the manifest.xml of the app. For example, in the "Bee Count" app, it uses *com.knirirr.beecount..WelcomeActivity* (with two dots) instead of *com.knirirr.beecount.WelcomeActivity* (with one dot).
As a result, R-DLD will not be able to start the app. If this happens, specify the correct main activity with the **-main_activity** option. For example, *-main_activity com.knirirr.beecount.WelcomeActivity*
   - **-epsilon \<number\>**: a value between 0.0 to 1.0 (0.1 by default). 0.0 implies a pure systematic exploration while 1.0 
   implies a pure random exploration
   - **-timeout \<number\>**: the time in seconds to be allocated for the execution
   - **-count \<number\>**: the number of events to be generated (2250 by default)
   - **-interval \<number\>**: the sleep time among the events (3 seconds by default). Increase this value if your Android device works slowly
   - **-script <your_script.json>**: specify the json script to force R-DLD to execute specific actions. It is useful if the app requires, for example, a login
   - **-grant_perm**: it grants all the permissions the app requires (recommanded)
   - **-keep_app**: it does not uninstall the app after the execution of R-DLD
   - type **dld --help** or **dld -h** for more details

### Exemple
A running instance can be located in the application directory. If needed, modify the run.sh file to execute it without the --robot parameter.
* cd application/
* ./run.sh

### Permissions
Linux's permissions to access the Arduino board.
* chmod a+rw /dev/ttyUSB0


## Evaluation

[Evaluation](evaluation/README.md)

Directory Structure
---------------
This is the root directory of the repository. The directory is structured as follows:

    R-DLD
     .
     |
     |--- application/ 
     |		|
     |		|--- R-DLD-Arduino/	R-DLD: Robotic-supported Data Loss Detection 
     |		|--- run.sh		Script to run a data loss test on a test application. 
     |
     |
     |--- build robot/
     |		|
     |		|--- app/	Application in C to be installed on the Arduino.
     |		|
     |		|--- robot/	Parts of the robot construction.
     |
     |
     |--- evaluation/
     |		|
     |		|--- apks77/                            Applications evaluated in the experiment
     |		|
     |		|--- classification_of_reports/		Manual classification of all alerts from the applications evaluated in the experiment.
     |		|
     |		|--- data_loss_analysis/		All inputs generated by R-DLD (screenshots, interactions with the application and logs).
     |		|
     |		|--- issues/				All issues open to developers grouped projects, number of reported failures, status and comments from developers.
     |
     |
     |--- scripts/	Script used to generate the database of application and repository URLs.
     |		|
     |		|--- files2023/		            Files generated by the fdroid.py script containing detailed information about the applications.
     |		|
     |		|--- fdroid.py		            Script that accesses the F-Droid store and generates CSV files containing information about applications, categorized by type.
     |		|
     |		|--- last_commit.py	            Script to list GitHub projects with updates in the current year.
     |		|
     |		|--- report_manifest_apps.ods       Analysis of app manifests to identify orientation lock settings. Generated by process_files_apk.py
     |		|
     |		|--- download_apps.py               Script to download all applications and organize them by categories.
     |		|
     |		|--- process_files_apk.py           Script to generate report on app rotation