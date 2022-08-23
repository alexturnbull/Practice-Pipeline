import requests 

downloadUrl = 'https://www.ons.gov.uk/generator?uri=/economy/inflationandpriceindices/bulletins/housepriceindex/february2022/61b62a24&format=csv'


with requests.get(downloadUrl) as rq:
    with open("C:\\Data\\ONS\\housing_prices\\housing_prices.csv", 'wb') as file:
        file.write(rq.content)
    
