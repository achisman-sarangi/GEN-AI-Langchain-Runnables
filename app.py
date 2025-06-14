import requests

# Base URL
base_url = "https://coverage.cms.gov/api/v1/coverage"

# Optional: Add query parameters (e.g., filter by coverage type)
params = {
    "coverageType": "National",  # Filter for National Coverage Determinations
    "pageSize": 10  # Limit to first 10 records for example
}

# Make the API call
response = requests.get(base_url, params=params)

# Check for successful response
if response.status_code == 200:
    data = response.json()
    print("Coverage Data:")
    for coverage in data.get('results', []):
        print(f"- {coverage['title']}: {coverage['description']}")
else:
    print("Error fetching data:", response.status_code)
