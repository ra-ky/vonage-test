
VONAGE
- https://www.vonage.kr/communications-apis/sms/

### Install

```bash
$ pip install vonage
```

### Client

```python
client = vonage.Client(key="xxxx", secret="xxxx")
sms = vonage.Sms(client)
```

### Send

```python
responseData = sms.send_message(
    {
        "from": "Vonage APIs",
        "to": "821012341234",
        "text": "A text message sent using the Nexmo SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
```
