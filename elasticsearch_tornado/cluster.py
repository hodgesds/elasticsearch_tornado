from .client import BaseClient


class ClusterClient(BaseClient):

    def health(self, index=None, params={}, callback=None, **kwargs):
        """
        Get a very simple status on the health of the cluster.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-health.html#cluster-health>`_

        :arg index: Limit the information returned to a specific index
        :arg level: Specify the level of detail for returned information, default u'cluster'
        :arg local: Return local information, do not retrieve the state from master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master node
        :arg timeout: Explicit operation timeout
        :arg wait_for_active_shards: Wait until the specified number of shards is active
        :arg wait_for_nodes: Wait until the specified number of nodes is available
        :arg wait_for_relocating_shards: Wait until the specified number of relocating shards is finished
        :arg wait_for_status: Wait until cluster is in a specific state, default None
        """

        query_params = (
            'level', 'local', 'master_timeout', 'timeout',
            'wait_for_active_shards', 'wait_for_nodes',
            'wait_for_relocating_shards', 'wait_for_status',
        )

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cluster', 'health', index], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def pending_tasks(self, params={}, callback=None, **kwargs):
        """
        The pending cluster tasks API returns a list of any cluster-level
        changes (e.g. create index, update mapping, allocate or fail shard)
        which have not yet been executed.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cluster-pending.html>`_

        :arg local: Return local information, do not retrieve the state from master node (default: false)
        :arg master_timeout: Specify timeout for connection to master
        """

        query_params = ('local', 'master_timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cluster', 'pending_tasks'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def state(self, metric=None, index=None, params={}, callback=None, **kwargs):
        """
        Get a comprehensive state information of the whole cluster.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cluster-state.html>`_

        :arg metric: Limit the information returned to the specified metrics.
            Possible values: "_all", "blocks", "index_templates", "metadata",
            "nodes", "routing_table", "master_node", "version"
        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg index_templates: A comma separated list to return specific index
            templates when returning metadata.
        :arg local: Return local information, do not retrieve the state from master node (default: false)
        :arg master_timeout: Specify timeout for connection to master
        :arg flat_settings: Return settings in flat format (default: false)
        """

        query_params = (
            'index_templates', 'local', 'master_timeout', 'flat_settings',
        )

        if index and not metric:
            metric = '_all'

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cluster', 'state', metric, index], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def stats(self, node_id=None, params={}, callback=None, **kwargs):
        """
        The Cluster Stats API allows to retrieve statistics from a cluster wide
        perspective. The API returns basic index metrics and information about
        the current nodes that form the cluster.
        `<https://www.elastic.co/guide/en/elasticsearch/reference/current/cluster-stats.html#cluster-stats>`_

        :arg node_id: A comma-separated list of node IDs or names to limit the
            returned information; use `_local` to return information from the node
            you're connecting to, leave empty to get information from all nodes
        :arg flat_settings: Return settings in flat format (default: false)
        :arg human: Whether to return time and byte values in human-readable format.

        """

        query_params = ('flat_settings', 'human',)

        params = self._filter_params(query_params, params)

        if node_id:
            node_id = 'nodes/%s' % node_id

        url = self.mk_url(*['_cluster', 'stats', node_id], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def reroute(self, body, params={}, callback=None, **kwargs):
        """
        Explicitly execute a cluster reroute allocation command including specific commands.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cluster-reroute.html>`_

        :arg body: The definition of `commands` to perform (`move`, `cancel`, `allocate`)
        :arg dry_run: Simulate the operation only and return the resulting state
        :arg explain: Return an explanation of why the commands can or cannot be executed
        :arg filter_metadata: Don't return cluster state metadata (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master node
        :arg metric: Limit the information returned to the specified metrics.
            Defaults to all but metadata
        :arg timeout: Explicit operation timeout
        """
        query_params = (
            'dry_run', 'explain', 'master_timeout', 'metric', 'timeout',
        )

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cluster', 'reroute'], **params)

        self.client.fetch(
            self.mk_req(url, body=body, method='POST', **kwargs),
            body     = body,
            callback = callback
        )

    def get_settings(self, params={}, callback=None, **kwargs):
        """
        Get cluster settings.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cluster-update-settings.html>`_

        :arg flat_settings: Return settings in flat format (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master node
        :arg timeout: Explicit operation timeout
        """

        query_params = ('flat_settings', 'master_timeout', 'timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cluster', 'settings'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def put_settings(self, body, params={}, callback=None, **kwargs):
        """
        Update cluster wide specific settings.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cluster-update-settings.html>`_

        :arg body: The settings to be updated. Can be either `transient` or
            `persistent` (survives cluster restart).
        :arg flat_settings: Return settings in flat format (default: false)
        """

        query_params = ('flat_settings',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cluster', 'settings'], **params)

        self.client.fetch(
            self.mk_req(url, body=body, method='PUT', **kwargs),
            body     = body,
            callback = callback
        )
