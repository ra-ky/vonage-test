import vonage

client = vonage.Client(key="xxxx", secret="xxxx")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "reborn",
        "to": "821012341234",
        "text": "code: 1234\nsite",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
