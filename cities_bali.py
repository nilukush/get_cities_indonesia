import requests
from bs4 import BeautifulSoup

# The URL of the Wikipedia page
url = 'https://id.wikipedia.org/wiki/Daftar_kabupaten_dan_kota_di_Bali'

# Send a GET request to the webpage
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table by its class 'wikitable'
    # Note: Wikipedia tables often have this class, but you may need to adjust based on the specific table
    table = soup.find('table', {'class': 'wikitable'})

    # Initialize an empty set to store unique names
    unique_names = set()

    if table:
        # For each row in the table, excluding the header
        for row in table.find_all('tr')[1:]:
            columns = row.find_all('td')
            # The second column contains the "Kabupaten/Kota" names
            if len(columns) > 1:
                # Remove "Kabupaten" and "Kota" from the name and add to the set
                name = columns[1].text.strip().replace("Kabupaten ", "").replace("Kota ", "")
                unique_names.add(name)

    # Convert the set to a list and sort it
    unique_names_list = sorted(list(unique_names))

    # Print the unique, sorted names
    for name in unique_names_list:
        print(name)
else:
    print(f"Failed to retrieve webpage, status code: {response.status_code}")
