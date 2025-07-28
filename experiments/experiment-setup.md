# Setup Instructions for Experiment

* Undeploy all services/functions
* make sure that func.yaml only has specVersion, name, runtime, created, (namespace, registry)
* deployment of function with desired execution mode
* write down GPU analyzer parameters
* redeploy GPU analyzer
* configure locust script
* port forwarding (grafana, locust...)
* open grafana and locust

# After Experiment
* save GPU analyzer logs
* save locust results (plus images)
* save grafana cpu and gpu data
* Write down pod lifecycle