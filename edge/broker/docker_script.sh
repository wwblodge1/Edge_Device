docker build -t wwblodge1/mosquitto:v1 --no-cache .
docker tag mosquitto wwblodge1/mosquitto:v1
docker push wwblodge1/mosquitto:v1
