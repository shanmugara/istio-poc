# istio-poc
Istio poc cases

## Istio Installation

1. `/istio/samples/security/spire` contains the `istio-spire-config-omega.yaml` and other omega files.
2. use `istioctl` or `helm`  to install istio with the following command:
```bash
istioctl install -f istio-spire-config-omega.yaml
```
**OR with helm:**

- Helm values are under `helm/values` path.
- Use the appropriate values file to install istio with helm.
- Make sure to change the values according to your environment.

3. install csi driver with the following command:
```bash
kubectl apply -f spire-csi-driver-omega.yaml
```
3. install the spire server and agent with the following command:
```bash
kubectl apply -f spire-quickstart.yaml
```
4. install the spire agent with the following command. look at the files under spire-agent/ for more details.:
```bash
kubectl apply -f spire-agent/

```
5. install `cert-manager` with the following command:
```bash
helm install cert-manager oci://quay.io/jetstack/charts/cert-manager -n cert-manager --create-namespace --set crds.enabled=true
```
6. install `omega-issuer` Helm chart with the following command:
```bash
helm install omega-issuer oci://docker.io/shanmugara/omega-issuer --version 0.0.2 -n cert-manager
``` 
7. Crete the `OmegaIssuer` resource with the following command:
```bash
kubectl apply -f manifests/omega-issuer/omega-cluster-issuer.yaml -n cert-manager
```
8. Create a certificate resource for istio ingress gateway with the following command:
```bash
kubectl apply -f  manifests/omega-issuer/omegaapp3-cert.yaml -n istio-system
```

