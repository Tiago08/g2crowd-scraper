# G2Crowd Scraper

This Python module uses Playwright to scrape the contents of a company's details from G2Crowd and returns the output in a structured format. The output can be a JSON or a CSV file with fields and values.

## Requirements

- Python 3
- Playwright (`pip install playwright`)
- pandas (`pip install pandas`)

## Usage

1. Clone this repository: `git clone https://github.com/Tiago08/g2crowd-scraper.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Create a CSV file named `urls.csv` with one column named `url` and add the G2Crowd URLs you want to scrape.
4. Run the code: `python scraper.py`
5. The results will be saved in a JSON file named `results.json` and a CSV file named `results.csv`.

## Example

Here's an example of what the `urls.csv` file could look like:
https://www.g2.com/products/thinkbridge/reviews 
https://www.g2.com/products/airtable/reviews 
https://www.g2.com/products/trello/reviews 

After running the code, the `results.json` file will contain the scraped data in the following format:

```json
[
    {
        "url": "https://www.g2.com/products/thinkbridge/reviews",
        "name": "ThinkBridge",
        "rating": "4.7",
        "reviews": "46 reviews",
        "categories": [
            "Custom Application Development Services",
            "eCommerce Development Companies",
            "Magento Development Companies",
            "Shopify Development Companies"
        ]
    },
    {
        "url": "https://www.g2.com/products/airtable/reviews",
        "name": "Airtable",
        "rating": "4.6",
        "reviews": "671 reviews",
        "categories": [
            "Database Management Systems (DBMS)",
            "Low-Code Development Platforms",
            "No-Code Development Platforms",
            "Online Database Software",
            "Rapid Application Development (RAD) Software"
        ]
    },
    {
        "url": "https://www.g2.com/products/trello/reviews",
        "name": "Trello",
        "rating": "4.3",
        "reviews": "20,351 reviews",
        "categories": [
            "Agile Project Management Software",
            "Collaboration Software",
            "Kanban Software",
            "Task Management Software",
            "Workflow Management Software"
        ]
    }
]
```

The results.csv file will contain the same data in a CSV format:
```url,name,rating,reviews,categories
https://www.g2.com/products/thinkbridge/reviews,ThinkBridge,4.7,"46 reviews","Custom Application Development Services,eCommerce Development Companies,Magento Development Companies,Shopify Development Companies"
https://www.g2.com/products/airtable/reviews,Airtable,4.6,"671 reviews","Database Management Systems (DBMS),Low-Code Development Platforms,No-Code Development Platforms,Online Database Software,Rapid Application Development (RAD) Software"
https://www.g2.com/products/trello/reviews,Trello,4.3,"20,351 reviews","Agile Project Management Software,Collaboration Software,Kanban Software,Task Management Software,Workflow Management Software"```
