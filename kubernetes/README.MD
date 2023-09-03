## Steps for EKS:


### Prerequisites:

EKS cluster with AWS Load Balancer Controller addon, Cert Manager.

AWS Load Balancer Controller addon chart, repo https://aws.github.io/eks-charts and chart is "aws-load-balancer-controller"
Cert Manager chart, repo https://charts.jetstack.io, chart is "cert-manager".


### Create namespace:

```
kubectl apply -f namespace.yaml
```

### Install the helm chart:

```
helm install -n webapp-namespace webapp helmchart/webapp -f helmchart/webapp/values.yaml
```

### Install the ingress:

```
kubectl apply -f ingress.yaml
```

The ingress will publicy expose the webapp installed via local helm chart and running in EKS on service as ClusterIP (port 80).
Accessing the ALB DNS address should return the reversed IP.
