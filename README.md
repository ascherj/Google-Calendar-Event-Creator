# Google Calendar Event Creator

This Python script automates the creation of multiple events in Google Calendar over a specified number of weeks.

## Features

- Automatically creates events in Google Calendar for a specified number of weeks
- Utilizes OAuth 2.0 for secure authentication with the Google Calendar API
- Configurable start date and number of weeks
- Creates all-day events

## Prerequisites

Before running this script, ensure you have:

1. Python 3.6 or higher installed
2. A Google Cloud project with the Calendar API enabled
3. OAuth 2.0 client credentials

## Installation

1. Clone this repository or download the script.
2. Install the required packages by running:

   ```sh
   pip install -r requirements.txt
   ```

3. Place your `credentials.json` file in the same directory as the script.

## Usage

1. Open `main.py` and modify the following variables as needed:
   - `start_date`: The date of the first event
   - `num_weeks`: The number of weeks to create events for
   - `event['summary']`: The name of your event

2. Run the script by executing:

   ```sh
   python main.py
   ```

3. The first time you run the script, a browser window will open for you to authenticate and authorize the application.

4. The script will create the events and print a confirmation message for each event created.

## Security Note

The `credentials.json` file contains sensitive information. It is included in the `.gitignore` file to prevent it from being accidentally committed to version control. Always keep your credentials secure and do not share them.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
