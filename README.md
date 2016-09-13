gmail-force-check
=================

Script to force gmail to refresh more often. As described here: http://rakowski.pro/how-to-force-gmail-to-check-your-pop3-account-as-often-as-possible/

Add this to crontab to send the email every 5 minutes from 0900-2200 and every 15 from 2300 to 0800: 

```bash
*/5 9-22 * * * /usr/bin/python /home/pi/scripts/email-ping.py
*/15 23,0-8 * * * /usr/bin/python /home/pi/scripts/email-ping.py
```
