import requests
from bs4 import BeautifulSoup
products_to_track = [
    {
        "product_url": "https://www.flipkart.com/vivo-t1-5g-rainbow-fantasy-128-gb/p/itm594222523bd8f?pid=MOBGB9TYFQR3FQZT&lid=LSTMOBGB9TYFQR3FQZTWOTIUO&marketplace=FLIPKART&q=5g+mobile&store=tyy%2F4io&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=3dc8fe45-4fcf-4be5-990d-0e81509575d0.MOBGB9TYFQR3FQZT.SEARCH&ppt=hp&ppn=homepage&ssid=v21m28a8c00000001652778345171&qH=721b57ce73b1a035",
        "name": "vivo T1 5G (Rainbow Fantasy, 128 GB)",
        "target_price": 16000
    },
    {
        "product_url": "https://www.flipkart.com/vivo-t1-5g-starlight-black-128-gb/p/itm594222523bd8f?pid=MOBGB9TYF7P7RNYX&lid=LSTMOBGB9TYF7P7RNYX6DFNDB&marketplace=FLIPKART&q=5g+mobile&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=3dc8fe45-4fcf-4be5-990d-0e81509575d0.MOBGB9TYF7P7RNYX.SEARCH&ppt=hp&ppn=homepage&ssid=v21m28a8c00000001652778345171&qH=721b57ce73b1a035",
        "name": "vivo T1 5G (Starlight Black, 128 GB)",
        "target_price":16000
    },
    {
        "product_url": "https://www.flipkart.com/poco-m3-pro-5g-cool-blue-128-gb/p/itmf923739d27b4b?pid=MOBG3P4ZMCSJNSAY&lid=LSTMOBG3P4ZMCSJNSAYIYDCCL&marketplace=FLIPKART&q=5g+mobile&store=tyy%2F4io&srno=s_1_7&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&fm=organic&iid=3dc8fe45-4fcf-4be5-990d-0e81509575d0.MOBG3P4ZMCSJNSAY.SEARCH&ppt=hp&ppn=homepage&ssid=v21m28a8c00000001652778345171&qH=721b57ce73b1a035",
        "name": "POCO M3 Pro 5G (Cool Blue, 128 GB)",
        "target_price":16000
    },{

    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(id="container")
    if (product_price==None):
        product_price=soup.find(id="priceblock_ourprice")
    return product_price.get_text()
result_file = open('my_result_file.txt', 'w')
try:
    for every_product in products_to_track:
        product_price_returned=give_product_price(every_product.get("URL"))
        print(product_price_returned + " " + every_product.get("name"))
        product_price=product_price_returned[2:]
        product_price=product_price.replace(","," ")
        product_price=int(float(product_price))

    print(product_price)
    if product_price_returned<every_product.get("target_price"):
        print("Available at your required price")
        result_file.write(every_product.get("name") + '_\t' + 'available at target price' + 'current price - ' + str(
            product_price) + "\n")
    else:
        print("Still at current price")
finally:
    result_file.close()




