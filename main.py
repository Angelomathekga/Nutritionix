import requests
from datetime import datetime

APP_ID = "ff1ee008"
API_KEY = "b84d438117b47436b31bc61e957c698c"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/399c231225db4386009df1e79670c37f/workoutTracker/workouts"

exercise_body = {
    "query": input("What exercise did you do today")
}

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

response = requests.post(url=exercise_endpoint, json=exercise_body, headers=header)
result = response.json()

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEETY_ENDPOINT, json=sheet_inputs)

    print(sheet_response.text)