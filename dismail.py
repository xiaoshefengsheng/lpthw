import requests

url = "https://api.exmail.qq.com/cgi-bin/user/update"

querystring = {"access_token":"UGOYApiP0TDr76xI99qBUVuvrvc6sxBbewtfIiNhdFOi8EzMM3wmEoExF3JdYb6oRnSLxISL1GWhe9V3hSUYsQ"}

payload = {
	'userid': "lixinhua@wuhaotech.com", 
	'enable': "0"
	}
headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'Postman-Token': "967858bf-53ad-40c9-b6e0-0f9dde552b18"
    }

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)