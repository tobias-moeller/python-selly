# python-selly
Simple API wrapper for selly.gg

### Prerequisites
* python3 


### Features
* Get all coupons
* Get specific coupon
* Create coupon
* Update coupon
* Delete coupon
* Get all orders
* Get specific order
* Get all products
* Get specific product
* Create product
* Update product
* Delete product
* Get all product groups
* Get specific product group
* Get all queries
* Get specific query

### Using
```python
from SellyApi import SellyRequest
req = SellyRequest("API_KEY", "EMAIL")
response = req.get_all_products()
print(response)
```

References https://developer.selly.gg/#introduction
