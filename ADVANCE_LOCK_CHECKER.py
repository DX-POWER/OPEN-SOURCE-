#_-_-ADVANCE_LOCK_ID_CHECKER-_-_#
#_-_-_GIFT_BY_DX_-_-_#
#_-_-_CODING_BY_-_-_PRINCE RONI_-_-_#

#ADVANCE PYTHON PROGRAMMING  PAID COURSE 
#ALL TELETEST ADVANCE CODING VIDEO 68
#COURSE  PRICE  : 1000 TK

        #OFFER
#70% DISCOUNT  COURSE  PRICE  300TK 
#OFFER END DATE : 15/06/2024

#CONTACT  :    TELEGRAM ID    :    @dxPrince150

import requests

def check_facebook_id(fb_id):
    url = f"https://graph.facebook.com/{fb_id}?fields=id,name,account_status&access_token=YOUR_ACCESS_TOKEN"
    response = requests.get(url)
    data = response.json()

    if "error" in data:
        return {"valid": False, "cloned": False, "locked": False}

    if data["account_status"] == "active":
        return {"valid": True, "cloned": False, "locked": False}
    elif data["account_status"] == "disabled":
        return {"valid": True, "cloned": False, "locked": True}
    elif data["account_status"] == "duplicate":
        return {"valid": True, "cloned": True, "locked": False}
    else:
        return {"valid": False, "cloned": False, "locked": False}

# Replace with your Facebook access token
access_token = "YOUR_ACCESS_TOKEN"

fb_id = input("Enter Facebook ID: ")
result = check_facebook_id(fb_id)

print("Valid:", result["valid"])
print("Cloned:", result["cloned"])
print("Locked:", result["locked"])