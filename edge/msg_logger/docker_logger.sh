docker build -t msg_logger --no-cache -f Dockerfile.msg_logger .
docker tag msg_logger wwblodge1/msg_logger:latest
docker push wwblodge1/msg_logger:latest
