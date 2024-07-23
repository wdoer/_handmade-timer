# Handmade Pomodoro Timer (MacOS only)

Easy to programmer use that timer for self-job

Steps to need knows:

- start_time & end_time - is a value what explained start you work day and end it
- work_period - set a time how many time u want working
- rest_period - the same of up but rest time
- in cycles you can change text what is showed
- of course u need set own crontab in terminal
- libs install after env and add self, just look imports

`crontab -e`

`*/30 * * * 1-5 sh /Users/{PATH_TO_YOUR_FOLDER}/handmade-timer/startup.sh >> /Users/{PATH_TO_YOUR_FOLDER}/handmade-timer/logs_startup.log 2>&1` - thats my cron now
