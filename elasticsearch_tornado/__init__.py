from __future__ import absolute_import

VERSION        = (2, 0, 0)
__version__    = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

from .client   import BaseClient
from .cat      import MeowClient
from .cluster  import ClusterClient
from .indices  import IndicesClient
from .nodes    import NodesClient
from .snapshot import SnapshotClient

class EsClient(BaseClient):
    def __init__(self, *args, **kwargs):
        super(EsClient, self).__init__(*args, **kwargs)
        self.cat      = MeowClient(*args, **kwargs)
        self.cluster  = ClusterClient(*args, **kwargs)
        self.indices  = IndicesClient(*args, **kwargs)
        self.nodes    = NodesClient(*args, **kwargs)
        self.snapshot = SnapshotClient(*args, **kwargs)
