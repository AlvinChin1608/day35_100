# day35_100
I am currently engaged in a 100-day Python Bootcamp, which I am documenting and sharing my progress on GitHub. The boot camp is designed to progressively intensify, allowing me to deepen my understanding and proficiency in Python programming.

Additionally, I have chosen to include the beginner, intermediate and advanced in my documentation to provide a valuable reference for my future growth and development.

--------------
# Weather Notification Project
## Overview
In this project, I developed a weather notification system using the OpenWeatherMap API and Twilio's messaging service. This system checks the weather forecast and sends a WhatsApp/SMS message if rain is expected at 7am every day by running the code using PythonAnyWhere cloud services. 

## What I Learned
1. __Environment Variables and dotenv__
To keep sensitive information secure, such as API keys and authentication tokens, I learned to use environment variables with the dotenv package. This method is more secure than hardcoding sensitive information directly in the script.

or 

Get on the IDE terminal and type export API="123" and then simply type env to check. Import the OS module and to call it simply type in os.environ.get("API"). Be aware that GitHub will automatically decline the upload to prevent your secret key being leak. 

3. __Making API Requests with requests__
I used the requests library to make API calls to the OpenWeatherMap API. By sending parameters such as latitude, longitude, and API key, I retrieved weather data in JSON format.

4. __Parsing JSON Data__
I learned to parse JSON data to extract specific weather conditions. I checked if the weather condition codes indicated rain within the next 12 hours.

5. __Sending Messages with Twilio__
I utilized Twilio's API to send WhatsApp/SMS messages. By integrating Twilio's messaging service, I automated notifications for weather conditions.
