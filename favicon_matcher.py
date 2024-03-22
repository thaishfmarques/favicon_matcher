import requests
from bs4 import BeautifulSoup
import argparse

def fetch_favicons(url):
    with requests.Session() as session:
        page = session.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.content, 'html.parser')
        favicons = soup.find('pre')
        return [line.split(':', 1) for line in favicons.text.split('\n') if line]
    return []

def main():
    parser = argparse.ArgumentParser(description='Identify frameworks')
    parser.add_argument('-f', '--favicon', type=str, help='MD5sum of the favicon')
    args = parser.parse_args()

    favicons_data = fetch_favicons('https://wiki.owasp.org/index.php/OWASP_favicon_database')

    for favicon_data in favicons_data:
        if len(favicon_data) == 2:
            md5sum, favicon = favicon_data
            if args.favicon in md5sum:
                print(f"{favicon.strip()} - is a match for {args.favicon}")
        else:
            print(f"Invalid data: {favicon_data}")

if __name__ == "__main__":
    main()
