from twilio.rest import Client


def make_call(
    account_sid, account_token, from_number, to_number, message, pause_length=5
):
    client = Client(account_sid, account_token)
    call = client.calls.create(
        twiml=f'<Response><Pause length="{pause_length}"/><Say> {message} </Say> <Pause length="{pause_length}"/></Response>',
        to=to_number,
        from_=from_number,
    )
    return call


def make_text(account_sid, account_token, from_number, to_number, message):
    client = Client(account_sid, account_token)
    message = client.messages.create(to=to_number, from_=from_number, body=message)

    return message
