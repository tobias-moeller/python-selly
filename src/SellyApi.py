import json
import base64
import urllib.parse
from urllib.request import Request, urlopen

class SellyRequest(object):
    """
    Module to communicate with selly.gg api
    Read more in selly developer documentation
    https://developer.selly.gg/#introduction
    """

    def __init__(self, api_key, email):
        """
        Initialize SellyRequest
        @param api_key: Api key for selly
        @type api_key: string
        @param email: email account to selly
        @type email: string
        """
        self.api_key = api_key
        self.email = email
        self.url = "https://selly.gg/api/v2"

    def request(self, method, path, data):
        """
        Sending HTTP request to selly api
        @param method: Http method
        @type method: string
        @param path: path from main url
        @type path: string
        @param data: data to send to selly
        @type data: dictionary
        @return: Response text
        @rtype: json
        """
        full_http_path = self.url + path
        prep_data = json.dumps(data).encode('utf8')
        request = Request(full_http_path, data=prep_data, method=method)
        prep_auth = '%s:%s' % (self.email, self.api_key)

        auth = base64.standard_b64encode(prep_auth.encode('utf-8'))
        request.add_header("Authorization", "Basic %s" % auth.decode('utf-8'))
        request.add_header('content-type', 'application/json')
        response = urlopen(request)
        response_text = json.loads(response.read())
        return response_text

    def get(self, path):
        """
        Send HTTP GET method to selly api
        @param path: Path to from main url
        @type path: string
        @return: Response text
        @rtype: json
        """
        return self.request("GET", path, None)

    def post(self, path, data):
        """
        Send HTTP POST method to selly api
        @param path: Path to from main url
        @type path: string
        @param data: data to send to api
        @type data: dictionary
        @return: Response text
        @rtype: json
        """
        return self.request("POST", path, data)

    def put(self, path, data):
        """
        Send HTTP PUT method to selly api
        @param path: Path to from main url
        @type path: string
        @param data: data to send to api
        @type data: dictionary
        @return: Response text
        @rtype: json
        """
        return self.request("PUT", path, data)
    
    def delete(self, path):
        """
        Send HTTP DELETE method to selly api
        @param path: Path to from main url
        @type path: string
        @return: Response text
        @rtype: json
        """
        return self.request("DELETE", path, None)

    def get_all_coupons(self):
        """
        Gets all coupons https://developer.selly.gg/#get-all-coupons
        @returns: data from api
        @rtype: json
        """
        return self.get("/coupons")

    def get_coupon(self, coupon_id):
        """
        Gets specific coupon https://developer.selly.gg/#get-a-specific-coupon
        @returns: data from api
        @rtype: json
        """
        return self.get("/coupons/%s" % coupon_id)

    def create_coupon(self, code, discount, product_ids, max_use=None):
        """
        Create new coupon https://developer.selly.gg/#create-a-coupon
        @param code: new coupon code
        @type code: string
        @param discount: discount to offer
        @type discount: int
        @param product_ids: ids of product to add coupon to
        @type product_ids: list[string]
        @param max_use: max uses of this coupon code, None means unlimited
        @type max_use: int
        @returns: response
        @rtype: json
        """
        data = {
            'coupon':{
                'code': code, 
                'discount': discount, 
                'product_ids': product_ids, 
                'max_use': max_use
                }
            }     
        return self.post("/coupons", data)

    def update_coupon(self, coupon_id, new_code, discount, product_ids, max_use=None):
        """
        Create new coupon https://developer.selly.gg/#update-a-coupon
        @param coupon_id: coupon id to update
        @type coupon_id: string
        @param new_code: name to update coupon code to
        @type new_code: string
        @param discount: discount to offer
        @type discount: int
        @param product_ids: ids of product to add coupon to
        @type product_ids: list[string]
        @param max_use: max uses of this coupon code, None means unlimited
        @type max_use: int
        @returns: response
        @rtype: json
        """
        data = {
            'coupon':{
                'code': new_code, 
                'discount': discount, 
                'product_ids': product_ids, 
                'max_use': max_use
                }
            }
        return self.put("/coupons/%s" % coupon_id, data)

    def delete_coupon(self, coupon_id):
        """
        Deletes an existing coupon
        @param coupon_id: coupon id to delete
        @type coupon_id: string
        @returns: response
        @rtype: json
        """
        return self.delete("/coupons/%s" % coupon_id)

    def get_all_orders(self):
        """
        Get all orders https://developer.selly.gg/#get-all-orders
        @returns: orders
        @rtype: json
        """
        return self.get("/orders")
    
    def get_order(self, order_id):
        """
        Get specific order https://developer.selly.gg/#get-a-specific-order
        @returns: order
        @rtype: json
        """
        return self.get("/orders/%s" % order_id)

    def get_all_products(self):
        """
        Get all products https://developer.selly.gg/#get-all-products
        @returns: products
        @rtype: json
        """
        return self.request("GET","/products", None)
    
    def get_product(self, product_id):
        """
        Get specific products https://developer.selly.gg/#get-a-specific-product
        @returns: products
        @rtype: json
        """
        return self.get("/products/%s" % product_id)

    def create_product(self):
        """
        Create a new product https://developer.selly.gg/#create-a-product
        """
        pass
    
    def update_product(self):
        """
        Update existing product https://developer.selly.gg/#update-a-product
        """
        pass

    def delete_product(self, product_id):
        """
        Delete existing product https://developer.selly.gg/#delete-a-product
        @param product_id: product id to delete
        @type product_id: string
        @returns: response
        @rtype: json
        """
        return self.delete("products/%s" % product_id)

    def get_all_product_groups(self):
        """
        Get all product groups https://developer.selly.gg/#get-all-product-groups
        @returns: product groups
        @rtype: json
        """
        return self.get("/product_groups")

    def get_product_group(self, product_group_id):
        """
        Get specific product groups https://developer.selly.gg/#get-a-specific-product-group
        @param product_group_id: id of the product group
        @type product_group_id: string
        @returns: product groups
        @rtype: json
        """
        return self.get("/product_groups/%s" % product_group_id)

    def get_all_queries(self):
        """
        Get all queries https://developer.selly.gg/#get-all-queries
        @returns: queries
        @rtype: json
        """
        return self.get("/queries")

    def get_query(self, query_id):
        """
        Get specific query https://developer.selly.gg/#get-a-specific-query
        @returns: query
        @rtype: json
        """
        return self.get("/queries/%s" % query_id)