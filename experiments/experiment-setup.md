# Setup Instructions for Experiment

* Connect to control plane
* Undeploy all services/functions
* make sure that func.yaml only has specVersion, name, runtime, created, (namespace, registry)
* deployment of function with desired execution mode
  ```
  func deploy --registry index.docker.io/maxireis/ -b=s2i -v --execution-mode auto
    ```
* write down GPU analyzer parameters
* configure testing script
* port forwarding (grafana, locust...)
  ```
  kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
  kubectl port-forward -n default svc/prometheus-grafana 3000:80
    ```
* open grafana
* redeploy GPU analyzer
    ```
    kubectl apply -f deployment.yaml
    ```
* start script

# After Experiment
* save GPU analyzer logs
* save locust results (plus images)
* save grafana cpu and gpu data
* Write down pod lifecycle