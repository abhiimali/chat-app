# chat-app
chat  application in django python 

Simple Message Chat Application API


Technologies Used :  *Python Django   DRF JWT* 

## Register User 

``` POST /api/register```


Following are the required fields

first_name
last_name
username
email
password
confirm_password

*********


## Login User 

``` POST /api/login```

Required Fields

username
password

JWT Token Will Be Generated

******

# Message Sent API 

``` POST /api/messages``` 

Only Needed Parameter Is ```message`` 

*****

# Get All Messages 

``` GET /api/messages```

ALL Messages Will Displayed 

*****

**Messaging Related Routes Are Only Allowed For Authenticated Users**

# Delete a Message

``` DELETE /api/messages/{ID}```

Message With Given {ID} get  Deleted

*****







