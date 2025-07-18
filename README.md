-> Website Summarizer (CLI)
     This is a simple Python command-line tool that lets you quickly get a summary of any website using OpenAI’s GPT. 

-> What’s this?
    You give it a website URL, and it fetches the page, cleans out the clutter (like ads and scripts), 
    and then asks OpenAI to create a neat summary for you. Perfect for getting the highlights without the noise.

-> What do you need?
    - Python (3.7 or newer)
    - An OpenAI API key (you can get one from [OpenAI](https://platform.openai.com/account/api-keys))
    - A few Python packages (we’ll get to that)

-> How to set it up
    Clone this repo:
    ```bash
    git clone https://github.com/varsharaodevaraj/summarizer.git
    cd summarizer
    
-> Create and activate a virtual environment:
    python -m venv venv
    - On Windows:
        venv\Scripts\activate
    - On Mac/Linux:
        source venv/bin/activate
    
-> Install dependencies:
    pip install -r requirements.txt
    
-> Create a .env file in the project folder with your OpenAI API key:
    OPENAI_API_KEY=your_openai_api_key_here

-> Usage:
    Run the script with the URL you want to summarize:
    python main.py "https://example.com"
