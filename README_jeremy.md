# Running locally on Docker Desktop Kubernetes
kubectl apply -f aks-store-quickstart.yaml

kubectl get pods -l app=python-front

kubectl get svc | grep kubernetes??? 

kubectl expose pod (podname) --type=NodePort
kubectl port-forward python-front-85bd787987-66mwn 82:82

minikube 0r kubectl  service (service name) --url

kubectl port-forward python-front-8449655db4-9sjml 8082:8082

http://127.0.0.1:8082/


# Deploying to AKS
az aks get-credentials --resource-group jeremyvoss --name myAKSCluster
kubectl apply -f aks-store-quickstart.yaml

kubectl get pods -l app=python-front
kubectl get service python-front

Enable azure vpn

# Switching Apps?

