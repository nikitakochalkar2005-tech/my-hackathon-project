import requests

def fetch_hacktoberfest_info():
    print("Welcome to Hacktoberfest Project!")
    # Example API endpoint
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        print("API Hit Successful! GitHub API is active.")
    else:
        print("Failed to fetch API data.")

if __name__ == "__main__":
    fetch_hacktoberfest_info()
