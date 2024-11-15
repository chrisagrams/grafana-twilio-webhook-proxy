# Grafana Webhook to Twilio Proxy

A simple proxy to use Grafana webhooks with Twilio.

## Supported Features
✅ **SMS Notifications via Twilio**
Receive real-time alerts directly to your phone via SMS from Grafana.

✅ **Voice Phone Call via Twilio**
Receive automated voice calls for urgents alerts from Grafana.

## Installation and Configuration
The proxy is built and run as a Docker container within docker-compose. The container can be run on any machine that your Grafana instance can access (or hosted on the same machine).

1. Clone the repository:
```sh
git clone https://github.com/chrisagrams/grafana-twilio-webhook-proxy.git
```

2. Create a .env file within the cloned directory containing your Twilio credentials. An example .env is found in `.env.example`:
```
ACCOUNT_SID=
AUTH_TOKEN=
FROM_NUMBER=
``` 

3. Build and run docker-compose:
```sh
docker compose build && docker compose up -d
```
> [!NOTE]
> By default, this proxy runs on port `8000`. Change this port within `docker-compose.yaml` if this port is taken.

4. In Grafana, navigate to **Alerting** > **Contact points** > **Create contact point**.

5. Under **Integration**, select **Webhook**.

6. Under **URL**, 

    a. For SMS, enter `http://IP_ADDRESS:8000/sms?to_number=YOUR_NUMBER`

    b. For Phone call, enter `http://IP_ADDRESS:8000/call?to_number=YOUR_NUMBER`

> [!IMPORTANT]
> `IP_ADDRESS` is the IP address of the host where the proxy is running (localhost if on the same machine). 
> `YOUR_NUMBER` Must be formated in Twilio-friendly way. ex: +11231231234

7. **Save contact point**, and use it in your alerts!

## License
This project is licensed under the MIT License.