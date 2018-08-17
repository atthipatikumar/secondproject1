from django.http import Http404, HttpResponse, HttpResponseBadRequest
import json
from django.conf import settings
from secondproject.db import query


def register22(request):
    id = request.REQUEST.get('id', '')
    FirstName = request.REQUEST.get('FirstName', '')
    LastName = request.REQUEST.get('LastName', '')
    Emailid = request.REQUEST.get('Emailid', '')
    Password = request.REQUEST.get('Password', '')

    if id != '':
        sql = "SELECT * from register WHERE id= %s"
        param_for_user_details = [id]

    elif FirstName != '':
        sql = "SELECT * from register WHERE FirstName= %s"
        param_for_user_details = [FirstName]
    elif LastName != '':
        sql = "SELECT * from register WHERE LastName= %s"
        param_for_user_details = [LastName]
    elif Emailid != '':
        sql = "SELECT * from register WHERE Emailid= %s"
        param_for_user_details = [Emailid]
    elif Password != '':
        sql = "SELECT * from register WHERE Password= %s"
        param_for_user_details = [Password]
    else:
        sql = "SELECT * from register"
        param_for_user_details = []
    results = query(sql, *param_for_user_details)
    final_test_map = []
    metadata_totalcount = 0
    # result is constructed in the expected format
    for result in results:
        metadata_totalcount = metadata_totalcount + 1
        response_map = {}
        response_map['id'] = result['id']
        response_map['FirstName'] = result['FirstName']
        response_map['LastName'] = result['LastName']
        response_map['Emailid'] = result['Emailid']
        response_map['Password'] = result['Password']
        final_test_map.append(response_map)
    metadata = {"total_count": metadata_totalcount}
    response = {"metadata": metadata, 'data_test': final_test_map}
    data = json.dumps(response, encoding="ISO-8859-1")
    http_response = HttpResponse(data, content_type="application/json")
    return http_response


def order24(request):
    order_id = request.REQUEST.get('order_id', '')
    name = request.REQUEST.get('name', '')
    order_item = request.REQUEST.get('order_item', '')
    order_date = request.REQUEST.get('order_date', '')
    order_delivery = request.REQUEST.get('order_delivery', '')

    if order_id != '':
        sql = "SELECT * from orders WHERE order_id= %s"
        param_for_user_details = [order_id]

    elif name != '':
        sql = "SELECT * from orders WHERE name= %s"
        param_for_user_details = [name]
    elif order_item != '':
        sql = "SELECT * from orders WHERE order_item=%s"
        param_for_user_details = [order_item]
    elif order_date != '':
        sql = "SELECT * from orders WHERE order_date=%s"
        param_for_user_details = [order_date]
    elif order_delivery !='':
        sql = "SELECT * from orders WHERE order_delivery=%s"
        param_for_user_details = [order_delivery]
    else:
        sql = "SELECT * from orders"
        param_for_user_details = []
    results = query(sql, *param_for_user_details)
    final_test_map = []
    metadata_totalcount = 0
    # result is constructed in the expected format
    for result in results:
        metadata_totalcount = metadata_totalcount + 1
        response_map = {}
        response_map['order_id'] = result['order_id']
        response_map['name'] = result['name']
        response_map['order_item'] = result['order_item']
        response_map['order_date'] = result['order_date']
        response_map['order_delivery'] = result['order_delivery']
        final_test_map.append(response_map)
    metadata = {"total_count": metadata_totalcount}
    response = {"metadata": metadata, 'data_test': final_test_map}
    data = json.dumps(response, encoding="ISO-8859-1")
    http_response = HttpResponse(data, content_type="application/json")
    return http_response

