# Top-30-C-Repositories-on-GitHub-API-Data-Visualization
This project uses the GitHub REST API to fetch the most‑starred C repositories and visualize them using Plotly. It demonstrates:  API authentication  JSON parsing  error handling  rate‑limit awareness  data extraction  interactive visualization

**Features:**
Secure GitHub token via environment variable
Fetches top C repositories sorted by stars
Handles API errors and rate limits
Extracts repository names and star counts
Displays an interactive Plotly bar chart

**Technologies Used:**
Python
requests
Plotly Express
GitHub REST API
Environment variables

Author: Craig Kindel
Date: 5-25-2026

I created this for my own personal Python project to fine-tune my skills.

1. Clone the repository
bash
git clone https://github.com/DocDMB2004/Top-30-C-Repositories-on-GitHub-API-Data-Visualization.git
cd Top-30-C-Repositories-on-GitHub-API-Data-Visualization.git

2. Install dependencies
Make sure you have Python 3.10+ installed, then run:

bash
pip install -r requirements.txt
Your requirements.txt should include:
requests
plotly

3. Set your GitHub token
setx GITHUB_TOKEN "your_token_here"

4. Run the program
python github_c_api_requests.py
   
5. View the output
The terminal will print the top repositories
A Plotly bar chart will open showing the top 30 C repositories by stars
