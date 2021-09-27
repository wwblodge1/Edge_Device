docker build -t broker --no-cache -f Dockerfile.broker .
docker tag broker wwblodge1/broker:latest
docker push wwblodge1/broker:latest
