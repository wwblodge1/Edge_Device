#!/bin/bash 

if [ "$1"  == run ]; then 
   kubectl apply -f ~/w251/cloud/broker/mqtt_deployment.yaml
   kubectl apply -f ~/w251/cloud/broker/mqtt_service.yaml
   kubectl apply -f ~/w251/cloud/processor/processor.yaml
  # kubectl expose deployment mosquitto-deployment --type=NodePort --port=32364 --name=mosquitto
else
   kubectl delete deployment mosquitto-deployment
   kubectl delete deployment processor-deployment 
   kubectl delete service mosquitto-service
   kubectl delete service mosquitto
fi
