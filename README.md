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
3. (OPTIONAL) install the spire server and agent with the following command:
```bash
kubectl apply -f spire-quickstart.yaml
```
4. Install the spire agent with the following command:

**For external spire**, use the manifests under `manifests/istio-external-spire/spire-agent/`
```bash
kubectl apply -f manifests/istio-external-spire/spire-agent/
```

5. Install `spire-registrar` with the Helm chart with the following command:
```bash
helm install spirereg -n spire oci://docker.io/shanmugara/spire-registrar --version 1.0.9
````
6. install `cert-manager` with the following command:
```bash
helm install cert-manager oci://quay.io/jetstack/charts/cert-manager -n cert-manager --create-namespace --set crds.enabled=true
```
```bash
kubectl label ns cert-manager csi-webhook=enabled
```
7. install `omega-issuer` Helm chart with the following command:
```bash
helm install omega-issuer oci://docker.io/shanmugara/omega-issuer --version 0.0.2 -n cert-manager
``` 
8. Crete the `OmegaIssuer` resource with the following command:
```bash
kubectl apply -f manifests/omega-issuer/omega-cluster-issuer.yaml -n cert-manager
```
9. Create a certificate resource for istio ingress gateway with the following command:
```bash
kubectl apply -f  manifests/omega-issuer/omegaapp3-cert.yaml -n istio-system
```
10. Install `trust-manager` with the following command:
```bash
helm install trust-manager oci://quay.io/jetstack/charts/trust-manager --namespace cert-manager
```

# 1.27.0 Istio changes
- 1.27.0 uses native mode side car injection. As a result spire and side templates are no longer supported.
- values.global.proxy.enableNativeSidecars=true is the default.
- Setting values.global.proxy.enableNativeSidecars=false will enable lgacy mode side car injection
- In the istiod values.yaml make sure to remove templates ["sidecar", "spire"].
