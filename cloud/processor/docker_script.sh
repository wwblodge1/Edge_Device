docker build -t processor --no-cache -f Dockerfile.processor .
docker tag processor wwblodge1/processor:latest
docker push wwblodge1/processor:latest
