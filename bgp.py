from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.openconfig import bgp

provider = NetconfServiceProvider(address='xrv', port=830, username="cisco", password="cisco", protocol="ssh")

crud = CRUDService()

bgp = bgp.Bgp()
bgp.global_.config.as_ = 65512

crud.create(provider, bgp)

### verify bgp

bgp.global_.config.router_id = '1.1.1.1'
crud.create(provider, bgp)

### verify bgp router id

# intentional error
bgp.global_.config.as_ = -1
crud.create(provider, bgp)