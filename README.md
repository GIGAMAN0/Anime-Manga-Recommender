# Anime_Chooser-Selector
CS50P Project
# Anime Details Fetcher

This is a Python script that fetches details of anime from the Kitsu API. It allows users to enter anime titles or get a random suggestion, and retrieves information such as the English and Japanese titles, synopsis, rating, and episode count.

## Usage

1. Make sure you have Python installed on your system.
2. Clone this repository or download the script file.
3. Install the required libraries by running the following command: `pip install requests`
4. Open a terminal or command prompt and navigate to the directory where the script is located.
5. Run the script using the command: `python anime_details_fetcher.py`
6. Follow the prompts to enter anime titles or get a random suggestion.

## Libraries Used

- [Requests](https://docs.python-requests.org/en/latest/): A library for making HTTP requests in Python. It is used in this script to send requests to the Kitsu API.

## Features

- Fetch details of anime by entering titles.
- Get a random anime suggestion.
- Display details such as English and Japanese titles, synopsis, rating, and episode count.

## Suggestions for Improvement

- Error Handling: Implement error handling to handle cases where the API request fails or the anime details are not found.
- User Interface: Consider building a graphical user interface (GUI) for the script to make it more user-friendly.
- Testing: Write unit tests to ensure the script functions correctly and handles different scenarios.
- Documentation: Provide inline comments in the code to explain the purpose of each function and section. Additionally, consider writing a more detailed documentation file (e.g., using Sphinx) to explain the project structure, usage, and any additional features.

## Acknowledgments

- This script uses the Kitsu API to fetch anime details. (https://kitsu.io/api/edge/anime)
- The script is inspired by the Anime Details Fetcher project on GitHub. (https://github.com/example/anime-details-fetcher)
