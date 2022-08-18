# 🏪 Marketplace API

Tool for monitoring market products, day by day.

## ⚠️ Prerequisites
<a href="https://www.python.org/downloads/release/python-3100/">Python 3.10.0</a><br>
<a href="https://www.djangoproject.com/download/">Djanog 4.0.5</a><br>

## 🛠 Build
1. Create a venv environment `python -m venv ./venv` and activate it `source venv/bin/activate`
2. Create `.env` file in main direction and insert values from `.env.example`
  ```
  # SECRET KEY for working django.
  SECRET_KEY=
  
  # DEBAG MODE of WebApp. If it's true, all exception will show you.
  DEBUG_MODE=
  ```
 3. Download all needest requirements from `requirements.txt` - `pip3 install -r requirements.txt`
 4. Go to marketplace direct by command `cd marketplace`
 5. Create database and do migrations.
    `python3 manage.py makemigrations` - make migrations and create database
    `python3 manage.py migrate` - do migrations.
 6. Create supperuser `python3 manage.py createsuperuser` after enter all needest values.
 7. Start the api `python3 manage.py runserver`

## ⚙️ Using

### Add product
For adding product you should send POST request to this directions `http://127.0.0.1:8000/api/add-product/`.
Python3 example
```python
import requests
res = requests.post(
  "http://127.0.0.1:8000/api/add-product/", {
    "name": "Product 1",
    "description": "Product description",
  })
print(res) # if <Response [200]> - your product was created
```

### Edit product
For editting product you should send POST request to this directions `http://127.0.0.1:8000/api/edit-product/<product_id>/`.
Python3 example
```
import requests
res = requests.post(
  "http://127.0.0.1:8000/api/edit-product/1/", {
    "name": "New Product 1",
    "description": "New Product description",
  })
print(res) # if <Response [200]> - your product was updated
```

### Delete Product
For editting product you should send POST request to this directions `http://127.0.0.1:8000/api/delete-product/<product_id>/`.
Python3 example
```
import requests
res = requests.delete("http://127.0.0.1:8000/api/delete-product/1/")

print(res) # if <Response [202]> - your product was deleted
```

### Create/Edit Product Price
For editting product priceyou should send POST request to this directions `http://127.0.0.1:8000/api/edit-product-price/<product_id>/`.
Python3 example
```
import requests
res = requests.post(
  "http://127.0.0.1:8000/api/edit-product-price/1/", {
    "start_date": "2022-01-20",
    "end_date": "2022-09-10",
    "price": 20.99
    })
print(res) # if <Response [200]> - your product was updated
```

### All products
For showing all products you should send GET request to this directions `http://127.0.0.1:8000/api/all/`.
Python3 example
```
import requests
res = requests.get("http://127.0.0.1:8000/api/all/")
print(res.content)
```

### All product changes
For showing all product changes you should send GET request to this directions `http://127.0.0.1:8000/api/product-changes/<product_id>//`.
Python3 example
```
import requests
res = requests.get("http://127.0.0.1:8000/api/product-changes/1/")
print(res.content)
```

### Average Price
To calculate avarage price, send POST request to this link `http://127.0.0.1:8000/api/calculate-product-prices/<product_id>/`
Python3 example
```
import requests
res = requests.post(
  "http://127.0.0.1:8000/api/product-changes/1/", {
    "start_date": "2022-01-20", # year-month-day
    "end_date": "2022-09-10" # year-month-day
    })
print(res.content)
```


## 📄 License
 Copyright ©2022 NikStor03. Released under the MIT license.
