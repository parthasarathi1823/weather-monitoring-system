Weather Monitoring System (API-based)

Project Overview :

The Weather Monitoring System is a Python-based project that fetches real-time weather data from a public weather API.
It securely stores the API key using environment variables and allows users to request weather information for any city.

This project is designed to practice:

1.API handling using requests
2.JSON data extraction
3.Environment variable security
4.Modular Python programming
5.logging of files
6.importing modules
7.error handling for invalid cities

How Program works(work flow):

    User Input (City Name)
            ↓
    main.py
            ↓
    fetch.py (calls API)
            ↓
    config.py (loads API key from .env)
            ↓
    Weather API
            ↓
    JSON Response
            ↓
    Displayed to User

Step-by-step:

- User enters a city name.
- main.py sends the city to fetch_weather() in fetch.py.
- fetch.py builds the API request using:
- Base URL
- City name
- API key (from config.py)
- config.py loads the API key from .env using python-dotenv.
- API returns weather data in JSON format.
- JSON data is parsed and shown to the user.    

Project Structure:
Weather-monitoring-system
│
├── main.py        # Program entry point
├── fetch.py       # API request logic
├── config.py      # Loads API key securely
├── .env           # Stores API key (ignored by Git)
├── .gitignore     # Prevents pushing .env
└── README.md      # Project documentation

Tech Stack :
- Language --> Python
Libraries:
- requests – API calls
- python-dotenv – environment variable handling
- os – system environment access
- Data Format: JSON
API: 
- Free Weather API (e.g., WeatherAPI / OpenWeatherMap)

Future Improvements:
- Build CLI menu system
- Add forecast support