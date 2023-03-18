create strava developer account
enter your API Acces token into the python files
follow these instructions to allow access to your activities
https://stackoverflow.com/questions/52880434/problem-with-access-token-in-strava-api-v3-get-all-athlete-activities 

run getActivitys.py, this will get all your strava IDs and write them into a text file

run getData.py this will take the strava IDs and get all the data for them and store in another text file
    you can only do 100 activities at a time, you have to delete all but 100 ids from activityIds.txt before running
    
run plotMap.py this will take the data and plot it on a map. outputs a Map.html file, open in your browser, will be centered in evanston but you can move around
