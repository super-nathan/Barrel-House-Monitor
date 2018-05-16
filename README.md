## Monitor the Barrelhouse

Here at Burial Beer we have over 200 bourbon, rum, and wine barrels in our barrel aged beer program. The barrels need to be kept at a precise temperature and humity not only for the beer that is in the barrels but for the health of the barrels themselves. This is a collection of scripts that run on a Raspberry Pi that is permantently installed in in the barrelhouse. While this is not _(yet)_ a stand alone distro to spin up new monitors, this collection of scripts is pretty read and run.


### spreadsheet.py

This is the meat and potoatos of the barrel monitor. This script is ran by either cron, or manually through the web interface. It querries all the sensors, records the results to Google Sheets and makes the data available to the rest of the system. Yes this could be cleaned up and streamlined a lot, but for the sake of simplicity and the ability to have anyone be able to work on this script im going to keep it pretty caveman for now.


### watchtemps.sh

This program is a holdover from another project and is only kept here because it will be implemented in the future.