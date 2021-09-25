docker build -t logger --no-cache -f Dockerfile.logger .
docker tag logger wwblodge1/logger:latest
docker push wwblodge1/logger:latest
