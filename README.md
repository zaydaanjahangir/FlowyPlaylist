# Flowy Playlist Generator

This Flask application utilizes the Spotify Web API to create playlists filled with songs that transition smoothly between tracks based on their danceability.

## Features

- **Spotify OAuth Integration**: Securely authenticates users with Spotify to access their saved tracks and create new playlists.
- **Flowy Playlist Creation**: Analyzes song features (specifically danceability) to curate a playlist with a smooth flow.
- **Configurable**: Adjust the number of saved tracks used and customize playlist descriptions.

## Requirements

- Python 3.x
- Flask (install with `pip install Flask`)
- spotipy (install with `pip install spotipy`)

## Installation

1. Create a Spotify developer account and obtain your Client ID and Secret.
2. Clone or download this repository.
3. Create three separate text files:
    - `client_id.txt`: Paste your Spotify Client ID here.
    - `secret.txt`: Paste your Spotify Client Secret here.
    - `app_secret.txt`: Generate a random string to be used as your Flask app secret key.

## Usage

1. Update the text files as mentioned above.
2. Install dependencies: `pip install -r requirements.txt` (if a requirements.txt file is included)
3. Run the application: `python app.py`

## Authentication Flow

1. Accessing the application in your browser will redirect you to Spotify's login page.
2. Grant the application access to your Spotify account.
3. Upon successful login, the application will build a "Flowy Playlist" based on your saved tracks.

## Notes

- This application uses session cookies to store user tokens.
- The `debug=True` flag in `app.run` is for development purposes and should be disabled in production environments.
- Consider adding error handling for potential issues during the Spotify API interaction.

## Contributing

Feel free to submit pull requests with improvements or bug fixes. We appreciate your help!

## License

This project is licensed under the MIT License (see LICENSE file).
