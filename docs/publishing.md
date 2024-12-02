## Steps to publish a new ingress endpoint

### CedarACL derived intent for Istio: 
TBD (need to break down the intent and atrributes)


1. Deploy the application in kubernetes namespace. (we are injecting istio sidecar in the deployment)
2. Create a new service for the application.
3. Istio steps:
    1. Create a new virtual service for the application.
    2. Create a new gateway for the application.
    3. Create a new destination rule for the application.
    4. Create authorization policy for the application.
    5. Peer authentication policy for the application. 
    6. Create requestAuthentication policy for the application.

4. Create new gateway step:
    1. What information do we need to create a new gateway?
    - Gateway name: Generate based on the BRI?
    - Gateway namespace: This can be fixed as istio-system.
    - Gateway selector: This can be fixed as `istio=ingressgateway`. Do we need to override?
    - Host FQDN to listen on: This can be generated based on the BRI from CirACL.
    - Port to listen on: This can be fixed as 443.
    - Protocol to listen on: This can be fixed as HTTPS.
    - Gateway server TLS configuration
    - Gateway server TLS secret: This can be generated based on the BRI from CirACL. pkiCore? Need Secret for cert and cacert.
    - Gateway server TLS mode: This can be fixed as SIMPLE for most cases. We will need to support override?

5. Create new virtual service step:
    1. What information do we need to create a new virtual service?
    - Virtual service name: Generate based on the BRI?
    - Virtual service namespace: This can be fixed as istio-system.
    - Virtual service hosts FQDN: We have this from Gateway step.
    - Virtual service gateways: We have this from Gateway step.
    - Virtual service http routes uri prefix: This wont be in the CirACL. We need to get this from some other mapping.
    - How do we handle different uri prefixes for the same host? Can we use annotations in the service to auto generate this mapping?
      - spec.blp.istio.io/virtual-service-prefix: [/path]
      - spec.blp.istio.io/virtual-service-host: [host.domain.com]
    - If we use annotations, we need a controller that watches for service annotations and registers in SPEC database.
    - Virtual service http route destination: This wont be in the CirACL. We need to get this from some other mapping.
    - Virtual service http route destination port: This wont be in the CirACL. We need to get this from some other mapping.

6. Create new destination rule step:
    1. What information do we need to create a new destination rule?
    - Destination rule name: Generate based on the BRI?
    - Destination rule namespace: This can be fixed as istio-system.
    - Destination rule host: This is the backend service, we need to get from SPEC database mapping.
    - Destination rule traffic policy: This should include custom policy template defined in the SPEC database.
    - Traffic policy template in SPEC: should contain all trafficPolicy settings, such as tls mode, outlier detection, subsets, load balancing, etc.
    - Can we default most of the trafficPolicy options?
    - Should ISTIO_MUTAL be the default?

7. Create Authorization Policy
   - 
8. Create Peer Authentication Policy
   -
9. Create Request Authentication Policy
   -
   
 In all the above resources, we need to define locked and unlocked attributes. 
 Locked:
   Gateway:
   - Resource name
   - Resource namespace
   - Gateway selector
   - Published host FQDN spec:servers:hosts:[]
   - Published port spec:servers:port: name, number, protocol
   - TLS secret
   VirtualService:
   - Resource name
   - Resource namespace
   - Gateway
   - Hosts FQDN spec:hosts:[]
   DestinationRule:
   - Resource name
   - Resource namespace
   - Host spec:host
   - Traffic policy

Customizable:
  Gateway:
  - None
  VirtualService:
  - spec:http, spec:tcp, spec:tls
  DestinationRule:
  - trafficPolicy (should tls be locked?)
  - subsets

   