# Weather App 

The project is a web application that allows you to determine the current weather in a specific location based on the public api OpenWeatherMap.<br>
It also implements functionality for saving and viewing the history of queries stored in a PostgreSQL database.<br>
Application stack - FastApi, PostgreSQL, Docker.

## Technologies

- Python (FastApi)
- PostgreSQL
- Docker

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Sayrexxx/Weather-app-test-task.git
   ```
1. Create an .env file in the root of the project and add variables to it (see .env_example)

## Usage

1. Install Docker on your computer if it is not already installed
1. Navigate to the root directory of the project
1. Make sure that ports `5432` (PostgreSQL) and `8000` (App core) are free for usage on your host
1. Run app by the executing the following command:
   ```bash
   docker-compose up --build
   ```
1. See application on `127.0.0.1:8000` adress
