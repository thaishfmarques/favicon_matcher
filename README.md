# favicon_matcher


Favicon Matcher is a Python script that fetches favicons from OWASP favicon database URL and matches a given MD5sum with the MD5sums of the fetched favicons. I created this script as a tool to identify potential frameworks of a webpage based on the MD5sum of the icons during a CTF.

Could I simply go to the OWASP link and see if the MD5sum is listed there? Yes, I could. But where's the fun in that?

## Usage

### Requirements

- Python 3.10+
- Required Python packages (install using `pip install -r requirements.txt`):
  - `requests`
  - `beautifulsoup4`

### Installation

1. Clone the repository:
  `$ git clone https://github.com/thaishfmarques/favicon-matcher.git`

2. Navigate to the project directory:
  `$ cd favicon_matcher`

3. Install the required Python packages:
  `$ pip3 install -r requirements.txt`

### Running the Script

Run the script with the following command:

Replace `<MD5sum>` with the MD5sum you want to match.

Example:
`python favicon_matcher.py -f 1f8c0b08fb6b556a6587517a8d5f290b`

## Options

- `-f, --favicon <MD5sum>`: Specify the MD5sum to match.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
