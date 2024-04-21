import requests
import json

# URL 설정
end_point = 'http://127.0.0.1:5000/vendor'


def get_vendor(uri):
    url = end_point + uri
    response_of_get_vendor = requests.get(url=url)
    print('Status Code:', response_of_get_vendor.status_code)
    print('Response Headers:', response_of_get_vendor.headers)
    print('Response Body:', response_of_get_vendor.text)
    vendor = json.loads(response_of_get_vendor.text)
    return vendor


def save_vendor(vendor_name, vendor_fax, vendor_address):
    vendor_data = make_vendor_data(vendor_name, vendor_fax, vendor_address)
    response_of_save_vendor = requests.post(url=end_point, data=vendor_data)
    print('Status Code:', response_of_save_vendor.status_code)
    print('Response Body:', response_of_save_vendor.text)
    return response_of_save_vendor


def make_vendor_data(vendor_name, vendor_fax, vendor_address):
    return {
        'vendor_name': vendor_name,
        'vendor_fax': vendor_fax,
        'vendor_address': vendor_address
    }
