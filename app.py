import requests
from bs4 import BeautifulSoup
import json

# URL of the web page containing the table
url = 'https://csstats.gg/player/76561198287013865#/matches'

# Send a GET request to fetch the web page content
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find the table element by its HTML tag (e.g., <table>)
    table = soup.find('table')

    if table:
        # Extract table headers (assuming they are in <th> tags)
        headers = [header.text.strip() for header in table.find_all('th')]
        
        # Extract table rows (assuming each row is in <tr> tags)
        rows = []
        for row in table.find_all('tr')[1:]:  # Skip the first row if it contains headers
            row_data = [data.text.strip() for data in row.find_all('td')]
            rows.append(dict(zip(headers, row_data)))

        # Convert the table data to JSON format
        json_data = json.dumps(rows, indent=4)

        # Display the JSON data
        print(json_data)
    else:
        print("No table found on the page.")
else:
    print("Failed to fetch the web page. Status code:", response.status_code)
