1. Enable the namespace label for ambient with label `istio.io/dataplane-mode=ambient`

2. istioctl ztunnel commands:
`istioctl ztunnel-config certificates ztunnel-m65sm.istio-system` - check spiffe certs
3. Waypoint SPIFFE impersonation:

`root@omegaspire01:~# /opt/spire/spire-server entry create \
  -parentID "spiffe://wl.dev.omegaworld.net/ns/istio-system/sa/waypoint" \
  -spiffeID "spiffe://wl.dev.omegaworld.net/ns/default/sa/default" \
  -selector "k8s:sa:waypoint" \
  -selector "k8s:ns:istio-system"
Entry ID         : 6366a674-453d-4701-9c4a-f991209d298c
SPIFFE ID        : spiffe://wl.dev.omegaworld.net/ns/default/sa/default
Parent ID        : spiffe://wl.dev.omegaworld.net/ns/istio-system/sa/waypoint
Revision         : 0
X509-SVID TTL    : default
JWT-SVID TTL     : default
Selector         : k8s:ns:istio-system
Selector         : k8s:sa:waypoint`