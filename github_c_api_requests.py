import requests
import json
import plotly.express as px
import os

class OtherLanguagesAPICall:
    """Class to call an API for C."""

    def __init__(self):
        """Init method for class Other LanguagesAPICall."""

        token = os.getenv('GITHUB_TOKEN')

        if not token:
            raise ValueError("GITHUB_TOKEN environment variable not set")

        self.url = "https://api.github.com/search/repositories" # Url for the API call
        self.url += "?q=language:c+sort:stars+stars:>10000&per_page=100"
        self.url += "&page=1"

        self.header = {"Accept": "application/vnd.github.v3+json",
                       "Authorization": f"token {token}"} # header for the API call

        self.response_dict = None

    def request_data(self):
        """Method request data."""

        r = requests.get(self.url, headers=self.header) # Use requests to get the data from the URL API call
        self.response_dict = r.json() # Take the http response object r and convert its JSON body into a Python dictionary named: response_dict
        print(f"Status Code: {r.status_code}") # Print the status code to make sure that it is 200 - 200 means that we retrieved all of the data - Will remove when working

        if r.status_code == 403:
            print("Rate Limit Exceeded")
        
        if 'items' not in self.response_dict:
            print("GitHub API Error:", self.response_dict.get('message'))
            return False
        
        print(f"Complete Results: {not self.response_dict['incomplete_results']}") # Debugging code to make sure that the results are complete
        #print(f"{len(self.response_dict['items'])}") # Debugging code will remove when working

        #print(f"self.response_dict: {self.response_dict}") # Debugging code will remove when working
        
        return True # Return True on success

    def clean_print(self):
        """Method to clean up the data and print it."""

        response_string = json.dumps(self.response_dict, indent=4) # Clean up the data so it is more easily read by calling json dump string
        #print(f"Response String: {response_string}")

    def get_items(self):
        """Method to get the irems from self.response_dict."""

        repo_dicts = self.response_dict['items'] # Get the 'items' from self.response_dict and put into repo_dict
        #print(type(repo_dicts)) # Debugging code will remove when working.
        #print(f"repo_dict: {repo_dict}") # Debugging code will remove when working
        #print(len(repo_dicts)) # Debugging code will remove when working
        #print(f"repo_dicts: {repo_dicts}") # Debugging code will remove when working

        for repo_dict in repo_dicts[:30]:
            #print(type(repo_dict)) # Debugging code will remove when working
            print(f"Name: {repo_dict['name']}")
            print(f"Full Name: {repo_dict['full_name']}")
            print(f"HTML URL: {repo_dict['html_url']}\n")

    def graph(self):
        """Method to visualize the data."""

        repo_dicts = self.response_dict['items']

        names = [repo_dict['name'] for repo_dict in repo_dicts[:30]]
        stars = [repo_dict['stargazers_count'] for repo_dict in repo_dicts[:30]]

        fig = px.bar(x=names, y=stars)
        fig.update_layout(
            title={
                'text':'Top 30 C Repositories on GitHub',
                'x':0.5,
            })
        fig.show()



# If the program is ran from here
if __name__ == '__main__':
    ol = OtherLanguagesAPICall() # Make an instance of OtherLanguagesAPICall
    if ol.request_data(): # Call the method request data
        ol.clean_print() # Call the method clean_print() data 
        ol.get_items() # Call the method get_items()
        ol.graph() # Graph the data
