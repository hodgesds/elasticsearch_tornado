from .client import BaseClient


class SnapshotClient(BaseClient):

    def create(self, repository, snapshot, body, params={}, callback=None, **kwargs):
        """
        Create a snapshot in repository
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg body: The snapshot definition
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg wait_for_completion: Should this request wait until the operation
            has completed before returning, default False
        """

        query_params = ('master_timeout', 'wait_for_completion',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_snapshot', repository, snapshot], **params)

        self.client.fetch(
            self.mk_req(url, body=body, method='PUT', **kwargs),
            callback = callback
        )

    def delete(self, repository, snapshot, params={}, callback=None, **kwargs):
        """
        Deletes a snapshot from a repository.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        """

        query_params = ('master_timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_snapshot', repository, snapshot], **params)

        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = callback
        )

    def get(self, repository, snapshot, params={}, callback=None, **kwargs):
        """
        Retrieve information about a snapshot.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A comma-separated list of repository names
        :arg snapshot: A comma-separated list of snapshot names
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        """

        query_params = ('master_timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_snapshot', repository, snapshot], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def delete_repository(self, repository, params={}, callback=None, **kwargs):
        """
        Removes a shared file system repository.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A comma-separated list of repository names
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg timeout: Explicit operation timeout
        """

        query_params = ('master_timeout', 'timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_snapshot', repository], **params)

        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = callback
        )

    def get_repository(self, repository=None, params={}, callback=None, **kwargs):
        """
        Return information about registered repositories.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A comma-separated list of repository names
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """

        query_params = ('local', 'master_timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_snapshot', repository], **params)

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def create_repository(self, repository, body, params={}, callback=None, **kwargs):
        """
        Registers a shared file system repository.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A repository name
        :arg body: The repository definition
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg timeout: Explicit operation timeout
        """

        query_params = ('master_timeout', 'timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_snapshot', repository], **params)

        self.client.fetch(
            self.mk_req(url, body=body, method='PUT', **kwargs),
            callback = callback
        )

    def restore(self, repository, snapshot, body, params={}, callback=None, **kwargs):
        """
        Restore a snapshot.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg body: Details of what to restore
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg wait_for_completion: Should this request wait until the operation
            has completed before returning, default False
        """

        query_params = ('master_timeout', 'wait_for_completion',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*[
                '_snapshot', repository, snapshot, '_restore'
            ],
            **params
        )

        self.client.fetch(
            self.mk_req(url, body=body, method='POST', **kwargs),
            callback = callback
        )

    def status(self, repository=None, snapshot=None, params={}, callback=None, **kwargs):
        """
        Return information about all currently running snapshots. By specifying
        a repository name, it's possible to limit the results to a particular
        repository.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/modules-snapshots.html>`_

        :arg repository: A repository name
        :arg snapshot: A comma-separated list of snapshot names
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        """

        query_params = ('master_timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*[
                '_snapshot', repository, snapshot, '_status'
            ],
            **params
        )

        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = callback
        )

    def verify_repository(self,
            repository,
            master_timeout = 10,
            timeout        = 10,
            body           = '',
            params         = {},
            callback       = None,
            **kwargs
        ):
        """
        Returns a list of nodes where repository was successfully verified or
        an error message if verification process failed.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/modules-snapshots.html>`_

        :arg repository: A repository name
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg timeout: Explicit operation timeout
        """

        query_params = ('master_timeout', 'timeout',)

        params = self._filter_params(query_params, params)

        url = self.mk_url(*['_snapshot', repository, '_verify'], **params)

        self.client.fetch(
            self.mk_req(url, body=body, method='POST', **kwargs),
            callback = callback
        )
