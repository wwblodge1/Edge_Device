docker build -t cam --no-cache .
docker tag cam wwblodge1/cam:v1
docker push wwblodge1/cam:v1