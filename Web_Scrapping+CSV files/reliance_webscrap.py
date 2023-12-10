from bs4 import BeautifulSoup

# Read the contents of the input HTML file
with open("reliance_data_(1990-2023).html", "r") as file:
    data = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(data, "html.parser")

# Find the table body (tbody) in the HTML
tbody = soup.find("tbody")

# Find all the rows (tr) in the table
rows = tbody.find_all("tr")

# Open the CSV file for writing
with open("reliance_stock_data_(1990-2023).csv", "w") as file:
    # Write the column headers to the CSV file
    file.write("Date, Price, Open, High, Low, Volume, Change%\n")

    for row in rows:
        # Find all the columns (td) in the row
        columns = row.find_all("td")

        # Create a list to store the data for each row
        row_data = []

        for column in columns:
            # Replace commas with semicolons in the data and append it to row_data
            cell_data = column.get_text(strip=True).replace(",", "")
            #The strip=True argument indicates that leading and trailing whitespace should be removed from the retrieved text.
            row_data.append(cell_data)

        # Write the row data to the CSV file
        file.write(",".join(row_data) + "\n")

print("Data has been saved to 'reliance_stock_data_(1990-2023).csv'")
