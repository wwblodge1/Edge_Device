#!/bin/bash 

if [ "$1"  == run ]; then
   kubectl apply -f mqtt_deployment.yaml
   kubectl apply -f mqtt_service.yaml
   kubectl apply -f other_deployments.yaml
else
   kubectl delete deployment mosquitto-deployment
   kubectl delete deployment other-deployments 
   kubectl delete service mosquitto-service
fi
