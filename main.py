import requests
from bs4 import BeautifulSoup

# The URL of the page
url = 'https://kantorpengacara-ram.com/daftar-nama-kabupaten-kota-di-pulau-jawa/'

# Send a GET request to the webpage
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Select the container that holds all tables you're interested in
    container = soup.select_one('#post-357 > div.entry-content')

    # Now, find all tables within that container
    tables = container.select('table')

    # Initialize an empty set to store unique names from all tables
    unique_names = set()

    for table in tables:
        # For each table, find all rows and skip the header row
        for row in table.find_all('tr')[1:]:  # Assuming the first row is the header
            columns = row.find_all('td')
            # Target the second column for "Kabupaten/Kota" names
            if len(columns) > 1:  # Ensure there is at least a second column
                # Remove "Kabupaten" and "Kota" from the name and add to the set
                name = columns[1].text.strip().replace("Kabupaten ", "").replace("Kota ", "")
                unique_names.add(name)

    # Convert the set back to a list if you need to sort or perform list operations
    unique_names_list = list(unique_names)

    # Optional: Sort the list alphabetically
    unique_names_list.sort()

    # Print the unique, sorted names from all tables
    for name in unique_names_list:
        print(name)
else:
    print(f"Failed to retrieve webpage, status code: {response.status_code}")
