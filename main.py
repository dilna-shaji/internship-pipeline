from src.scrapers.greenhouse_scraper import scrape_greenhouse
from src.database import save_internships

def run_pipeline():
    print("Starting Pan-India Internship Ingestion Pipeline...")
    all_found_jobs = []
    greenhouse_targets = ["razorpay", "cred", "swiggy"]
    for company in greenhouse_targets:
        print(f"Checking updates for: {company}...")
        jobs = scrape_greenhouse(company)
        all_found_jobs.extend(jobs)
    if all_found_jobs:
        print(f"Found {len(all_found_jobs^)} matches. Pushing to database layer...")
        try:
            save_internships(all_found_jobs)
            print("Ingestion complete.")
        except Exception as e:
            print(f"Database save skipped or failed: {e}")
    else:
        print("No new target internships found across current cycles.")

if __name__ == "__main__":
    run_pipeline()
