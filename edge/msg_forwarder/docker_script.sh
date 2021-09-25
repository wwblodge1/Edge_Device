docker build -t msg_forwarder --no-cache -f Dockerfile.alpine .
docker tag msg_forwarder wwblodge1/msg_forwarder:latest
docker push wwblodge1/msg_forwarder:latest
