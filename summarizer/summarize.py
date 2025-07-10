from summarizer.fetcher import Website
from summarizer.openai_client import get_summary

def summary_url(url):
    website = Website(url)
    summary = get_summary(website)
    return summary