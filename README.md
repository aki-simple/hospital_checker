1. Install python from company portal

2. Activate your platform (ex: windsurf) with the help of company portal and FAQs

3. Install github development community from company portal
    3.1. Identify where git bash is installed and add the path to the environment variable PATH
    3.2. Create a github account with the company email id

4. Clone this repository: In the terminal in your platform(ex: windsurf), enter below commands one-by-one
    4.1. git clone https://github.com/your-username/hospital-checker.git
    4.2. cd hospital-checker

5. Create and activate a virtual environment: In the terminal in your platform(ex: windsurf), enter below commands one-by-one
    5.1. python -m venv .venv
    5.2. venv\Scripts\activate

6. Install dependencies: In the terminal in your platform(ex: windsurf), enter below commands one-by-one
    6.1. pip install -r requirements.txt

7. Run the app: In the terminal in your platform(ex: windsurf), enter below commands one-by-one
    7.1. streamlit run app.py


Project Structure
    app.py: The main application file
    data: Directory containing the raw and cleaned hospital data
    utils: Directory containing utility functions for geocoding and data preprocessing
