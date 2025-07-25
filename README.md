# Other repos
## Reevaluation
https://github.com/Mareise/knative-execution-mode-reevaluation

## func
https://github.com/Mareise/func

# Knative Deploy
```
func deploy --registry index.docker.io/maxireis/ -b=s2i -v --execution-mode auto

```

# Microk8s
installation like in https://microk8s.io/docs/getting-started
GPU node should not have --worker flag because we need to install gpu addon
```
microk8s enable gpu
```

# Knative
Install like https://knative.dev/docs/install/yaml-install/
0
i dont know but i used istio (not sure why)

# Prometheus / Grafana
## Prerequisits
* Ensure that node exporter are running on every node (i think this is in microk8s observability addon)
* Disable microk8s observability addon

## Install
from https://knative.dev/docs/serving/observability/metrics/collecting-metrics/
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
cd prometheus
helm install prometheus prometheus-community/kube-prometheus-stack -n default -f values.yaml
```

## Run / Upgrade
```
cd prometheus
helm upgrade prometheus prometheus-community/kube-prometheus-stack -n default -f values.yaml

kubectl port-forward -n default svc/prometheus-kube-prometheus-prometheus 9090:9090
kubectl port-forward -n default svc/prometheus-grafana 3000:80
```

admin
prom-operator

## Knative monitoring
```
kubectl apply -f https://raw.githubusercontent.com/knative-extensions/monitoring/main/servicemonitor.yaml
kubectl apply -f https://raw.githubusercontent.com/knative-extensions/monitoring/main/grafana/dashboards.yaml
```

## GPU monitoring
dcgm exporter comes with microk8s nvidia addon but somehow doesnt work with kubecost and prometheus
https://www.ibm.com/docs/en/kubecost/self-hosted/2.x?topic=configuration-nvidia-gpu-monitoring-configurations

so i installed it manually
```
cd dcgm
helm upgrade -i dcgm dcgm-exporter \
  --repo https://nvidia.github.io/dcgm-exporter/helm-charts \
  -n dcgm-exporter --create-namespace \
  -f values-dcgm.yaml
```

https://github.com/NVIDIA/dcgm-exporter/issues/22#issuecomment-2116538739
Our GPU doesnt support DCP which is needed for kubecost to work with dcgm exporter

# GPU support
enable nvidia microk8s addon which uses nvidia gpu operator


# Testing and Evaluation
```
kubectl port-forward -n istio-system svc/istio-ingressgateway 8080:80
```
Now it can be accessed via:
```
curl -H "Host: wasgeht.default.128.131.172.200.sslip.io" http://localhost:8080
```

## Locust
On Host machine install locust:
```
pip install locust
```
## Locustfile

## Cost Estimation
### Kubecost
```
cd kube-cost
helm install kubecost cost-analyzer \
--repo https://kubecost.github.io/cost-analyzer/ \
--namespace kubecost --create-namespace --values values.yaml

kubectl port-forward --namespace kubecost deployment/kubecost-cost-analyzer 9090
```

To access kubecost prometheus server:
```
kubectl -n kubecost port-forward svc/kubecost-prometheus-server 8080:80
```

# Dynamic Reevaluation
See https://github.com/Mareise/knative-execution-mode-reevaluation
```
cd reevaluation/kubernetes
kubectl apply -f deployment.yaml
kubectl apply -f roleBinding.yaml
```
