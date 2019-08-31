from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    url = "https://www.marathon.tokyo/result/index.php"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    all_headlines = soup.find_all("a", class_="result-title")
    all_prices = soup.find_all("span", class_="result-price")
    all_hood = soup.find_all("span", class_="result-hood")

    results = []

    # for row in zip(all_headlines, all_prices, all_hood):
    #     listings = {}
    #     listings["headline"] = row[0].get_text()
    #     listings["price"] = row[1].get_text()
    #     listings["hood"] = row[2].get_text()
    #     results.append(listings)

    # # Close the browser after scraping
    # browser.quit()

    # return results
