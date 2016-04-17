from __future__ import absolute_import

VERSION        = (2, 0, 1)
__version__    = VERSION
__versionstr__ = '.'.join(map(str, VERSION))

from .client   import BaseClient
from .cat      import MeowClient
from .cluster  import ClusterClient
from .indices  import IndicesClient
from .nodes    import NodesClient
from .snapshot import SnapshotClient


class EsClient(MeowClient, ClusterClient, IndicesClient, NodesClient,
        SnapshotClient):

    def __init__(self, *args, **kwargs):
        super(EsClient, self).__init__(*args, **kwargs)
