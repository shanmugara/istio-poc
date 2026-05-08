# Customizations for CSI Injection

## Update the istiod chart as follows:
```bash
vi ../manifests/charts/istio-control/istio-discovery/files/gateway-injection-template.yaml
```

Under the `volumes:` section, add the following code snippet:
```console
volumes:
  # Inject Bloomberg managed spiffe CSI volume if set to true
  {{- if eq .Values.global.csiVolumeInject true }}
  - name: workload-socket
    csi:
      driver: "csi.spiffe.io"
      readOnly: true
  {{- else }}
  - emptyDir: {}
    name: workload-socket
  {{- end }}
```
