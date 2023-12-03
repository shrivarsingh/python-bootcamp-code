import requests
from bs4 import BeautifulSoup
from re import sub
from decimal import Decimal

# Sometimes website has no price hence price variable will show None
url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

check = input("Enter URL of amazon product you wish to check or press ENTER to use default:\n")
if check == "":
    print(f"Using Default:\n{url}")
else:
    url = check

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36 Edg/89.0.774.45",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=url, headers=header)
response.raise_for_status()
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
print(f"\n{soup.title.text}")

price = soup.find(id="priceblock_ourprice")
amount = price.getText()

amount_split = amount.split("$")
if amount[0] == "$":
    print("Amount in $ converting to R")
    value = round(float(amount_split[1]) * 14.85, 2)
    print(f"Amount is: R{value}\n")
else:
    print("Amount not converted")
    value = round(float(amount_split[1]), 2)
    print(f"Amount is: {amount}\n")
