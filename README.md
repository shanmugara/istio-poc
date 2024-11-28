# istio-poc
Istio poc cases

## Istio Installation

1. /istio/samples/security/spire contains the istio-spire-config-omega.yaml and other omega files.
2. use istioctl to install istio with the following command:
```bash
istioctl install -f istio-spire-config-omega.yaml
```
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
