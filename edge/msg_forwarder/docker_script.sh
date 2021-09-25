docker build -t forwarder --no-cache -f Dockerfile.forwarder .
docker tag forwarder wwblodge1/forwarder:latest
docker push wwblodge1/forwarder:latest
