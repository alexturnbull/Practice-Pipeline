import requests 
from datetime import date 
downloadUrl = 'https://www.ons.gov.uk/generator?uri=/economy/inflationandpriceindices/bulletins/housepriceindex/february2022/61b62a24&format=csv'

today = date.today()
print(today)

with requests.get(downloadUrl) as rq:
      with open(f"C:\\Data\\ONS\\housing_prices\\housing_prices_{today}.csv", 'wb') as file:
          file.write(rq.content)
    
