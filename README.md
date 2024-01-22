 ## Description

This code is designed to extract information about trending GitHub repositories and format it in a structured manner. It utilizes the 'requests' library to fetch the HTML content of GitHub's trending page, parses it using BeautifulSoup, and then extracts relevant data from the parsed HTML. The extracted data is transformed into a list of dictionaries, with each dictionary containing information about a specific repository, including the developer name, repository name, and number of stars. Finally, the data is formatted into a CSV string, which can be easily exported to a CSV file.

## Tasks

1. **Request GitHub Trending Page:**
   - Use the 'requests' library to send a GET request to GitHub's trending page.
   - Store the response in a variable.

2. **Extract HTML Elements:**
   - Parse the HTML content of the response using BeautifulSoup.
   - Extract all HTML elements that contain relevant information about trending repositories.
   - Store the extracted elements in a list.

3. **Transform Extracted Data:**
   - Iterate through the list of extracted HTML elements.
   - Use CSS selectors to extract the developer name, repository name, and number of stars for each repository.
   - Store the extracted data in a dictionary for each repository.
   - Append each dictionary to a list.

4. **Format Transformed Data:**
   - Convert the list of dictionaries into a CSV string.
   - The CSV string should include the following columns: Developer, Repository Name, Number of Stars.
   - Separate each field with a comma, and each row with a newline.

## Usage

To use this code, simply call the 'runner()' function. This function will execute all the necessary steps to extract, transform, and format data about trending repositories on GitHub. The formatted data will be displayed as a CSV string in the console.

## Team

This code is a collaborative effort by the following team members:

Qorahojayev Muhammadxo'ja
