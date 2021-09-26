docker build -t cam -f Dockerfile.ubuntu_NX .
docker tag cam wwblodge1/cam:v1
docker push wwblodge1/cam:v1