import asyncio
import csv
import json
import pandas as pd
from playwright.async_api import async_playwright


async def scrape_company_page(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(url)
        company_name = await page.inner_text('h1[itemprop="name"]')
        company_rating = await page.inner_text('div[itemprop="ratingValue"]')
        company_reviews = await page.inner_text('span[itemprop="reviewCount"]')
        company_categories = await page.inner_text_all('a[itemprop="applicationCategory"]')
        await browser.close()
        return {
            "url": url,
            "name": company_name,
            "rating": company_rating,
            "reviews": company_reviews,
            "categories": company_categories
        }


async def scrape_company_pages(urls):
    tasks = []
    for url in urls:
        tasks.append(asyncio.ensure_future(scrape_company_page(url)))
    results = await asyncio.gather(*tasks)
    return results


def save_to_json(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)


async def main():
    urls = []
    with open("urls.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            urls.extend(row)
    results = await scrape_company_pages(urls)
    save_to_json(results, "results.json")
    save_to_csv(results, "results.csv")


if __name__ == "__main__":
    asyncio.run(main())