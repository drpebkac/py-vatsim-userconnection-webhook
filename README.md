# py-vatsim-userconnection-webhook
The updated version of the vatsim user connection Discord webhook. Written with Py and uses the API that Vatspy uses
## How to use
Run python script and pass the CID, Discord Webhook URI and name of username of webhook as arguments
#### Example
`python main.py "123456" "https://discord.com/api/webhooks/123456742354235/dsfgaedgaeeagr" "Webhook Bot"`
#### Deploy script onto a docker image
All dependencies are included inside the Dockerfile.

1. Build an image using a base
`docker build -t <name of image you want to call it> .

2. Once the image has been create it, use `docker run` to spin up a container with the image. Besure to pass the CID, Discord webhook url and name of webhook as you run the command.
`docker run -d -p 880:80 -it vathooks-userconnectionalerts "123456" "https://discord.com/api/webhooks/123456742354235/dsfgaedgaeeagr" "vatsim notification bot"`
