from .client import BaseClient


class MeowClient(BaseClient):

    def aliases(self, name=None, params={}, callback=None, **kwargs):
        """
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-aliases.html>`_

        :arg name: A comma-separated list of alias names to return
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'aliases', name], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )


    def allocation(self, node_id=None, params={}, callback=None, **kwargs):
        """
        Allocation provides a snapshot of how shards have located around the
        cluster and the state of disk usage.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-allocation.html>`_

        :arg node_id: A comma-separated list of node IDs or names to limit the
            returned information
        :arg byte_unit: The unit in which to display byte values
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('bytes', 'h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'allocation', node_id], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def count(self, index=None, params={}, callback=None, **kwargs):
        """
        Count provides quick access to the document count of the entire cluster,
        or individual indices.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-count.html>`_

        :arg index: A comma-separated list of index names to limit the returned
            information
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('bytes', 'h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'count', index], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def health(self, params={}, callback=None, **kwargs):
        """
        health is a terse, one-line representation of the same information from
        :meth:`~elasticsearch.client.cluster.ClusterClient.health` API
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-health.html>`_

        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg ts: Set to false to disable timestamping, default True
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'ts', 'v', )

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat/health'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def help(self, params={}, callback=None, **kwargs):
        """
        A simple help for the cat api.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat.html>`_

        :arg get_help: Return help information, default False
        """

        query_params = ('help',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def indices(self, index=None, params={}, callback=None, **kwargs):
        """
        The indices command provides a cross-section of each index.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-indices.html>`_

        :arg index: A comma-separated list of index names to limit the returned
            information
        :arg byte_unit: The unit in which to display byte values
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg pri: Set to true to return stats only for primary shards, default
            False
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = (
            'bytes', 'h', 'help', 'local', 'master_timeout', 'pri', 'v',
        )

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def master(self, params={}, callback=None, **kwargs):
        """
        Displays the master's node ID, bound IP address, and node name.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-master.html>`_

        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'master'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def nodes(self, params={}, callback=None, **kwargs):
        """
        The nodes command shows the cluster topology.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-nodes.html>`_

        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'nodes'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def recovery(self, index=None, params={}, callback=None, **kwargs):
        """
        recovery is a view of shard replication.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-recovery.html>`_

        :arg index: A comma-separated list of index names to limit the returned
            information
        :arg byte_unit: The unit in which to display byte values
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('bytes', 'h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'recovery', index], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def shards(self, index=None, params={}, callback=None, **kwargs):
        """
        The shards command is the detailed view of what nodes contain which shards.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-shards.html>`_

        :arg index: A comma-separated list of index names to limit the returned
            information
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'shards', index], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def segments(self, index=None, params={}, callback=None, **kwargs):
        """
        The segments command is the detailed view of Lucene segments per index.

        :arg index: A comma-separated list of index names to limit the returned
            information
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'segments', index], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def pending_tasks(self, params={}, callback=None, **kwargs):
        """
        pending_tasks provides the same information as the
        :meth:`~elasticsearch.client.cluster.ClusterClient.pending_tasks` API
        in a convenient tabular format.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-pending-tasks.html>`_

        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'pending_tasks'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def thread_pool(self, params={}, callback=None, **kwargs):
        """
        Get information about thread pools.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-thread-pool.html>`_

        :arg full_id: Enables displaying the complete node ids (default: 'false')
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information (default: 'false')
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers (default: 'false')

        """

        query_params = ('full_id', 'h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'thread_pool'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def fielddata(self, fields=None, params={}, callback=None, **kwargs):
        """
        Shows information about currently loaded fielddata on a per-node basis.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/cat-fielddata.html>`_

        :arg fields: A comma-separated list of fields to return the fielddata
            size
        :arg byte_unit: The unit in which to display byte values
        :arg fields: A comma-separated list of fields to return the fielddata
            size
        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information (default: 'false')
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers (default: 'false')

        """

        query_params = (
            'bytes', 'fields', 'h', 'help', 'local', 'master_timeout', 'v',
        )

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'fielddata', fields], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def plugins(self, params={}, callback=None, **kwargs):
        """
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/cat-plugins.html>`_

        :arg h: Comma-separated list of column names to display
        :arg get_help: Return help information, default False
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg v: Verbose mode. Display column headers, default False
        """

        query_params = ('h', 'help', 'local', 'master_timeout', 'v',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_cat', 'plugins'], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )
