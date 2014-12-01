from .client import BaseClient


class SnapshotClient(BaseClient):
    def __init__(self,
        *args,
        **kwargs
    ):
        super(SnapshotClient, self).__init__(*args, **kwargs)


    def create(self, repository, snapshot, body=None, params={}, cb=None, **kwargs):
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
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_snapshot', repository, snapshot], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def delete(self, repository, snapshot, params={}, cb=None, **kwargs):
        """
        Deletes a snapshot from a repository.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A repository name
        :arg snapshot: A snapshot name
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        """
        query_params = ('master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_snapshot', repository, snapshot], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def get(self, repository, snapshot, params={}, cb=None, **kwargs):
        """
        Retrieve information about a snapshot.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A comma-separated list of repository names
        :arg snapshot: A comma-separated list of snapshot names
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        """
        query_params = ('master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_snapshot', repository, snapshot], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def delete_repository(self, repository, params={}, cb=None, **kwargs):
        """
        Removes a shared file system repository.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/modules-snapshots.html>`_

        :arg repository: A comma-separated list of repository names
        :arg master_timeout: Explicit operation timeout for connection to master
            node
        :arg timeout: Explicit operation timeout
        """
        query_params = ('master_timeout', 'timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_snapshot', repository], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def get_repository(self, repository=None, params={}, cb=None, **kwargs):
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
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_snapshot', repository], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def create_repository(self, repository, body, params={}, cb=None, **kwargs):
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
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_snapshot', repository], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def restore(self, repository, snapshot, body=None, params={}, cb=None, **kwargs):
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
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[
                '_snapshot', repository, snapshot, '_restore'
            ],
            **params
        )
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def status(self, repository=None, snapshot=None, params={}, cb=None, **kwargs):
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
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[
                '_snapshot', repository, snapshot, '_status'
            ],
            **params
        )
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def verify_repository(self,
            repository,
            master_timeout = 10,
            timeout        = 10,
            params         = {},
            cb             = None,
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
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_snapshot', repository, '_verify'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )
