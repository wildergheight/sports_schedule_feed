#Sports Schedule Feed
#Dylan Klein
#3/24/20
#
import requests
import numpy as np

rangers_url = 'https://statsapi.web.nhl.com/api/v1/schedule?teamId=3'         #Update depending on which leagues are currently active
mets_url = 'https://statsapi.mlb.com/'
#jets_schedule
#osufb_schedule

rangers_schedule = requests.get(rangers_url)
mets_url = requests.get(mets_url)

if rangers_schedule.status_code != 200:
    # This means something went wrong.
    raise ApiError('GET /tasks/ {}'.format(rangers_schedule.status_code))
for todo_item in rangers_schedule.json():
	#teamname = todo_item['school']
