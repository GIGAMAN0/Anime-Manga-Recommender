
# Anime Chooser-Selector

## Project Overview

The Anime Chooser-Selector project is a Python-based tool designed to assist users in discovering new anime and manga recommendations based on their watched items and selected genres. It leverages the MyAnimeList API to retrieve details about anime and manga titles and employs a recommendation system using TF-IDF vectorization and cosine similarity to suggest relevant titles. Users can input their watched anime and manga, select preferred genres, and receive personalized recommendations tailored to their interests.

## Recent Update (Version 2.0)

In the recent update (Version 2.0), several new features and improvements have been introduced to enhance the functionality and user experience of the Anime Chooser-Selector tool:

### New Features

- **Enhanced Recommendation System**: The recommendation system has been improved to provide more accurate and relevant suggestions based on user input and preferences.
- **Interactive User Interface**: The script now features an interactive user interface with prompts and options for entering watched anime and manga, selecting favorite genres, and receiving recommendations.
- **Continuous Recommendations**: After receiving a recommendation, users now have the option to request additional suggestions without restarting the script.
- **Improved Error Handling**: Robust error handling has been implemented to gracefully handle cases where API requests fail or anime/manga details are not found.

### User Interface Enhancements

- **Simplified Input Process**: The input process for entering watched items and selecting genres has been streamlined for a more intuitive user experience.
- **Clearer Prompts and Messages**: Prompts and messages displayed during script execution have been refined to provide clearer instructions and feedback to the user.

## Getting Started

To use this tool, follow these steps:

### Prerequisites

- Python 3.x installed on your machine
- Requests library installed. You can install it via pip:
  ```
  pip install requests
  ```

### Installation

1. Clone this repository or download the script file.
2. Open a terminal or command prompt and navigate to the directory where the script is located.
3. Run the script using the command:
   ```
   python 'Project V2.0.py'
   ```

## Usage

1. Run the script and follow the prompts to enter the names of anime and manga you have watched and finished.
2. Select your favorite genres from the provided list.
3. Choose whether you want a recommendation for anime or manga.
4. The script will then provide a personalized recommendation based on your input.

## Features

- Fetch details of anime and manga from MyAnimeList API.
- Allow users to input their watched anime and manga.
- Support selection of favorite genres.
- Provide personalized recommendations based on user input.

## Libraries Used

- **Requests**: A library for making HTTP requests in Python. It is used to send requests to the MyAnimeList API.

## Suggestions for Improvement

- Error Handling: Implement robust error handling to gracefully handle cases where API requests fail or anime/manga details are not found.
- User Interface: Consider developing a graphical user interface (GUI) to enhance user experience and ease of use.
- Testing: Write comprehensive unit tests to ensure the functionality of the script across different scenarios.
- Documentation: Enhance inline comments in the code for better code readability and maintainability. Additionally, consider creating a detailed documentation file using tools like Sphinx to explain the project structure, usage, and advanced features.

## Contributing

Contributions to this project are welcome! Please open an issue first to discuss any major changes or features you plan to add. Remember to update tests as necessary

## Acknowledgments

- This project utilizes the MyAnimeList API to fetch anime and manga details.
