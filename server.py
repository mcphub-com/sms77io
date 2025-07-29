import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/sms77io-sms77io-default/api/sms77io'

mcp = FastMCP('sms77io')

@mcp.tool()
def get_contact(id: Annotated[str, Field(description='')]) -> dict: 
    '''Retrieves a single contact by its ID.'''
    url = 'https://sms77io.p.rapidapi.com/contacts/%7Bid%7D'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def update_contact(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Edit a contact with a given ID.'''
    url = 'https://sms77io.p.rapidapi.com/contacts/%7Bid%7D'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.patch(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_contact(id: Annotated[str, Field(description='')]) -> dict: 
    '''Deletes a single contact by ID for the given API key.'''
    url = 'https://sms77io.p.rapidapi.com/contacts/%7Bid%7D'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def create_contact(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Creates a single contact for a given API key.'''
    url = 'https://sms77io.p.rapidapi.com/contacts'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def list_contacts(p: Annotated[str, Field(description='API Key from Sms77.io.')],
                  order_by: Annotated[Union[str, None], Field(description='The column by which the contacts should be sorted.')] = None,
                  order_direction: Annotated[Literal['asc', 'desc', None], Field(description='The direction of the sorting. Can be either asc or desc.')] = None,
                  search: Annotated[Union[str, None], Field(description='You can use this parameter to search in all columns in your contacts.')] = None,
                  offset: Annotated[Union[int, float, None], Field(description='The page to be displayed. Default: 0')] = None,
                  limit: Annotated[Union[int, float, None], Field(description='The number of contacts to be displayed per page. Can be a value between 30 and 500. Default: 30')] = None,
                  group_id: Annotated[Union[int, float, None], Field(description='Only display contacts who are members of a specific group. Default: 123')] = None) -> dict: 
    '''Retrieves all contacts for a given API key.'''
    url = 'https://sms77io.p.rapidapi.com/contacts'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'order_by': order_by,
        'order_direction': order_direction,
        'search': search,
        'offset': offset,
        'limit': limit,
        'group_id': group_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def rcscapabilities(number: Annotated[str, Field(description='')],
                    _from: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''You can use this endpoint to query the RCS capability of a phone number. Before sending an RCS, you should always query the capabilities of a phone number first and cache the result if necessary.'''
    url = 'https://sms77io.p.rapidapi.com/lookup/rcs'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'number': number,
        'from': _from,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def home_location_register(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Retrieves ***H*ome *L*ocation *R*egister** information for a given phone number.'''
    url = 'https://sms77io.p.rapidapi.com/lookup'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def caller_name_delivery(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Retrieves ***C*alling *N*ame *D*elivery** information for a phone number.'''
    url = 'https://sms77io.p.rapidapi.com/lookup'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def number_format_lookup(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Retrieves the network operator as well as additional (porting) information for the given phone number.'''
    url = 'https://sms77io.p.rapidapi.com/lookup'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def mobile_number_portability(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Retrieves ***M*obile *N*umber *P*ortability** information for a given phone number.'''
    url = 'https://sms77io.p.rapidapi.com/lookup'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def send_sms(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Send SMS to one/multiple user(s) and/or contact(s).'''
    url = 'https://sms77io.p.rapidapi.com/sms'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_status(p: Annotated[str, Field(description='API Key')],
               msg_id: Annotated[Union[int, float], Field(description='The message ID of the SMS. Can be obtained by setting parameter JSON, return_msg_id or details to 1 when sending SMS via the API. Alternatively it can be retrieved from the message journal in the user area. Default: 0')]) -> dict: 
    '''Get a delivery report for a message ID sent with your API key.'''
    url = 'https://sms77io.p.rapidapi.com/status'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'msg_id': msg_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def send_voice_call(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Make a call to a specific number using seven's Voice API. In the simplest variant, you can specify a text that will then be read out to the recipient via our Text-To-Speech (TTS) Gateway. For advanced applications, you have the option to send the text in SSML format.'''
    url = 'https://sms77io.p.rapidapi.com/voice'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def validate_caller_id(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''The caller ID validation API allows you to automatically validate caller IDs for the *Voice API*. After calling this endpoint you will get a code back if successful. At the same time, the phone number is going to receive a call from us. The returned code must then be entered via *DTMF* using the telephone’s keypad.'''
    url = 'https://sms77io.p.rapidapi.com/validate_for_voice'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def auto_charge(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''With this API you can configure the automatic credit transfer for a subaccount. This can transfer credit from the main account to the subaccount when the balance falls below a defined threshold. To deactivate, simply set amount to 0.'''
    url = 'https://sms77io.p.rapidapi.com/subaccounts'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''You can use this API to delete subaccount by its ID.'''
    url = 'https://sms77io.p.rapidapi.com/subaccounts'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def transfer_credits(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''You can use this API to transfer credits from the main account to the subaccount once.'''
    url = 'https://sms77io.p.rapidapi.com/subaccounts'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def list(id: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''Query a list of all subaccounts of an account.'''
    url = 'https://sms77io.p.rapidapi.com/subaccounts'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def create(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Creates a new subaccount.'''
    url = 'https://sms77io.p.rapidapi.com/subaccounts'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_webhook() -> dict: 
    '''Deletes the webhook with the given ID.'''
    url = 'https://sms77io.p.rapidapi.com/hooks'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def create_webhook(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Creates a webhook with the given configuration.'''
    url = 'https://sms77io.p.rapidapi.com/hooks'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_webhooks(p: Annotated[str, Field(description='API key from Sms77.io.')]) -> dict: 
    '''Query the active webhooks of your account.'''
    url = 'https://sms77io.p.rapidapi.com/hooks'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def update_group(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''You can use this endpoint to update a group.'''
    url = 'https://sms77io.p.rapidapi.com/groups/%7Bid%7D'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.patch(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_group(delete_contacts: Annotated[Union[bool, None], Field(description='Specifies whether the contacts who are members of this group should also be deleted.')] = None) -> dict: 
    '''This endpoint allows you to delete groups.'''
    url = 'https://sms77io.p.rapidapi.com/groups/%7Bid%7D'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'delete_contacts': delete_contacts,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def create_group(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''You can use this endpoint to create a new group.'''
    url = 'https://sms77io.p.rapidapi.com/groups'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_group(id: Annotated[str, Field(description='')]) -> dict: 
    '''You can use this endpoint to retrieve a group by specifying the group ID.'''
    url = 'https://sms77io.p.rapidapi.com/groups/%7Bid%7D'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def list_groups(limit: Annotated[Union[int, float, None], Field(description='Limit the number of groups returned. Default: 77')] = None,
                offset: Annotated[Union[int, float, None], Field(description='The starting point from which the list should be displayed. Default: 0')] = None) -> dict: 
    '''This endpoint allows you to retrieve a paginated list of all your groups. By default, a maximum of ten groups are displayed per page.'''
    url = 'https://sms77io.p.rapidapi.com/groups'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def inbound(p: Annotated[str, Field(description='API key from Sms77.io')],
            date_from: Annotated[Union[str, None], Field(description='Start date for performed search')] = None,
            date_to: Annotated[Union[str, None], Field(description='End date for performed search')] = None,
            id: Annotated[Union[int, float, None], Field(description='Message ID Default: 123')] = None,
            state: Annotated[Union[str, None], Field(description='Message status - e.g. completed / failed for Voice or DELIVERED / NOTDELIVERED for SMS')] = None,
            to: Annotated[Union[str, None], Field(description='Receiver phone number in any format')] = None,
            limit: Annotated[Union[int, float, None], Field(description='Default: 77')] = None,
            offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Retrieves inbound messages history.'''
    url = 'https://sms77io.p.rapidapi.com/journal/inbound'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'date_from': date_from,
        'date_to': date_to,
        'id': id,
        'state': state,
        'to': to,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def outbound(p: Annotated[str, Field(description='API key from Sms77.io')],
             date_from: Annotated[Union[str, None], Field(description='Start date for performed search')] = None,
             date_to: Annotated[Union[str, None], Field(description='End date for performed search')] = None,
             id: Annotated[Union[int, float, None], Field(description='Message ID Default: 123')] = None,
             state: Annotated[Union[str, None], Field(description='Message status - e.g. completed / failed for Voice or DELIVERED / NOTDELIVERED for SMS')] = None,
             to: Annotated[Union[str, None], Field(description='Receiver phone number in any format')] = None,
             limit: Annotated[Union[int, float, None], Field(description='Default: 77')] = None,
             offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Retrieves outbound messages history.'''
    url = 'https://sms77io.p.rapidapi.com/journal/outbound'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'date_from': date_from,
        'date_to': date_to,
        'id': id,
        'state': state,
        'to': to,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def replies(p: Annotated[str, Field(description='API key from Sms77.io')],
            date_from: Annotated[Union[str, None], Field(description='Start date for performed search')] = None,
            date_to: Annotated[Union[str, None], Field(description='End date for performed search')] = None,
            id: Annotated[Union[int, float, None], Field(description='Message ID Default: 123')] = None,
            state: Annotated[Union[str, None], Field(description='Message status - e.g. completed / failed for Voice or DELIVERED / NOTDELIVERED for SMS')] = None,
            to: Annotated[Union[str, None], Field(description='Receiver phone number in any format')] = None,
            limit: Annotated[Union[int, float, None], Field(description='Default: 77')] = None,
            offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Retrieves message replies history.'''
    url = 'https://sms77io.p.rapidapi.com/journal/replies'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'date_from': date_from,
        'date_to': date_to,
        'id': id,
        'state': state,
        'to': to,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def voice(p: Annotated[str, Field(description='API key from Sms77.io')],
          date_from: Annotated[Union[str, None], Field(description='Start date for performed search')] = None,
          date_to: Annotated[Union[str, None], Field(description='End date for performed search')] = None,
          id: Annotated[Union[int, float, None], Field(description='Message ID Default: 123')] = None,
          state: Annotated[Union[str, None], Field(description='Message status - e.g. completed / failed etc.')] = None,
          to: Annotated[Union[str, None], Field(description='Receiver phone number in any format')] = None,
          limit: Annotated[Union[int, float, None], Field(description='Default: 77')] = None,
          offset: Annotated[Union[int, float, None], Field(description='Default: 0')] = None) -> dict: 
    '''Retrieves voice messages history.'''
    url = 'https://sms77io.p.rapidapi.com/journal/voice'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'date_from': date_from,
        'date_to': date_to,
        'id': id,
        'state': state,
        'to': to,
        'limit': limit,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def update_number(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Update the details of a single active number by providing the phone number. Currently you can update the friendly name and whether or not you would like to forward incoming SMS via SMS or email. As response you will get the updated number details.'''
    url = 'https://sms77io.p.rapidapi.com/numbers/active/%7Bnumber%7D'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.patch(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def get_active_number(number: Annotated[str, Field(description='')]) -> dict: 
    '''Get a single active number by providing the phone number.'''
    url = 'https://sms77io.p.rapidapi.com/numbers/active/%7Bnumber%7D'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'number': number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def active_numbers() -> dict: 
    '''Get a list of all active numbers that are currently associated with your account.'''
    url = 'https://sms77io.p.rapidapi.com/numbers/active'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def order_anumber(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Order a phone number by providing the desired number. The response will include the details of the number you ordered.'''
    url = 'https://sms77io.p.rapidapi.com/numbers/order'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def available_numbers(country: Annotated[Union[str, None], Field(description='')] = None,
                      features_sms: Annotated[Union[bool, None], Field(description='')] = None,
                      features_a2p_sms: Annotated[Union[bool, None], Field(description='')] = None,
                      features_voice: Annotated[Union[bool, None], Field(description='')] = None) -> dict: 
    '''This endpoint lets you search for available phone numbers based on the provided search criteria. The search criteria can include the country code, area code, and the number type. The response will include a list of available phone numbers that match the search criteria.'''
    url = 'https://sms77io.p.rapidapi.com/numbers/available'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country': country,
        'features_sms': features_sms,
        'features_a2p_sms': features_a2p_sms,
        'features_voice': features_voice,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def send_rcs_message(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''This endpoint allows you to send RCS messages to users. Before sending an RCS, you should ideally query the capabilities of the phone number to ensure the best possible user experience.'''
    url = 'https://sms77io.p.rapidapi.com/rcs/messages'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def trigger_event(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Send an event to a phone number to provide users with a more authentic conversational experience. After receiving a message, you should send the event READ and then IS_TYPING accordingly within a reasonable time. Either **msg_id** *or* **to** must be set.'''
    url = 'https://sms77io.p.rapidapi.com/rcs/events'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def delete_message(id: Annotated[str, Field(description='')]) -> dict: 
    '''You can revoke an RCS message that has not yet been delivered. This API immediately returns a successful response, regardless of whether the message has been deleted or not. Revocation is only possible if the end device has the REVOCATION capability.'''
    url = 'https://sms77io.p.rapidapi.com/rcs/messages/%7Bid%7D'
    headers = {'Content-Type': 'application/json', 'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.delete(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_pricing(p: Annotated[str, Field(description='API Key from Sms77.io.')],
                format: Annotated[Literal['json', 'csv', None], Field(description='Whether to return the response as JSON or CSV. The default is JSON.')] = None,
                country: Annotated[Union[str, None], Field(description='An ISO Code of the country you wish to retrieve the pricing for. Examples: \\\\\\"de\\\\\\" for Germany \\\\\\"uk\\\\\\" for Great Britain \\\\\\"fr\\\\\\" for France If this parameter is not specified, the prices of all countries are getting returned.')] = None) -> dict: 
    '''Retrieves pricing information for a single country or all.'''
    url = 'https://sms77io.p.rapidapi.com/pricing'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'format': format,
        'country': country,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_analytics(p: Annotated[str, Field(description='API Key')],
                  group_by: Annotated[Union[str, datetime], Field(description='Enum Defines the grouping of the data.')],
                  start: Annotated[Union[str, datetime, None], Field(description='Start date of the statistics in the format YYYY-MM-DD. By default, the date of 30 days ago is set.')] = None,
                  end: Annotated[Union[str, datetime, None], Field(description='End date of the statistics. By default, the current day.')] = None,
                  label: Annotated[Union[str, None], Field(description="Shows only data of a specific label. Allowed values: 'all' (default) or .")] = None,
                  subaccounts: Annotated[Union[str, None], Field(description="Receive the data only for the main account, all your (sub-)accounts or only for specific subaccounts. Allowed values: 'only_main', 'all' or subaccount ID.")] = None) -> dict: 
    '''Get detailed statistics of your account directly through our API.'''
    url = 'https://sms77io.p.rapidapi.com/analytics'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
        'group_by': group_by,
        'start': start,
        'end': end,
        'label': label,
        'subaccounts': subaccounts,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def get_balance(p: Annotated[str, Field(description='Your API key from Sms77.io.')]) -> dict: 
    '''Retrieves the account balance for the given API key.'''
    url = 'https://sms77io.p.rapidapi.com/balance'
    headers = {'x-rapidapi-host': 'sms77io.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'p': p,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
