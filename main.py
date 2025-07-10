import argparse
from summarizer.summarize import summary_url

def main():
    parser = argparse.ArgumentParser(description="Summarize any website using OpenAI.")
    parser.add_argument("url", help="URL of the website to summarize")
    args = parser.parse_args()

    try:
        summary = summary_url(args.url)
        print("Summary:\n")
        print(summary)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()