import uuid

import boto3
from boto3.dynamodb.conditions import Attr

dynamodb = boto3.resource('dynamodb')


def get_medicine(table_name, user_id):
    table = dynamodb.Table(table_name)
    response = table.scan(
        FilterExpression=Attr('user_id').eq(user_id)
    )
    return response["Items"]
    # print(table.creation_date_time)

def post_medicine(form,user_id):
    table = dynamodb.Table("medicine")
    medicine_id = str(uuid.uuid1())
    item = {"medicine_id":medicine_id,
            "medicine_name":form["medicine_name"],
            "date":form["date"],
            "user_id":user_id,
            "note":form["note"]}
    response = table.put_item(Item=item)
    return medicine_id
    # print(table.creation_date_time)


def if_insert_success(medicine_id):
    table = dynamodb.Table("medicine")
    response = table.get_item(
        Key={
            'medicine_id': medicine_id
        }
    )
    if "Item" in response:
        return True;
    else:
        return False;



def verify_user(user_id, password):
    table = dynamodb.Table("user")
    response = table.get_item(
        Key={
            'user_id': user_id
        }
    )
    if "Item" not in response:
        return False
    item = response['Item']
    if password != item["password"]:
        return False
    return True

if_insert_success("123")