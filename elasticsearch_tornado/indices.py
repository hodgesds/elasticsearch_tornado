from client import BaseClient


class IndicesClient(BaseClient):
    def __init__(self,
        *args,
        **kwargs
    ):
        super(IndicesClient, self).__init__(*args, **kwargs)


    def analyze(self, index=None, body=None, params={}, cb=None, **kwargs):
        """
        Perform the analysis process on a text and return the tokens breakdown of the text.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-analyze.html>`_

        :arg index: The name of the index to scope the operation
        :arg body: The text on which the analysis should be performed
        :arg analyzer: The name of the analyzer to use
        :arg char_filters: A comma-separated list of character filters to use
            for the analysis
        :arg field: Use the analyzer configured for this field (instead of
            passing the analyzer name)
        :arg filters: A comma-separated list of filters to use for the analysis
        :arg format: Format of the output, default u'detailed'
        :arg index: The name of the index to scope the operation
        :arg prefer_local: With `true`, specify that a local shard should be
            used if available, with `false`, use a random shard (default: true)
        :arg text: The text on which the analysis should be performed (when
            request body is not used)
        :arg tokenizer: The name of the tokenizer to use for the analysis
        """
        query_params = (
            'analyzer', 'char_filters', 'field', 'filters', 'format', 'index',
            'prefer_local', 'text', 'tokenizer',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_analyze'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def refresh(self, index=None, params={}, cb=None, **kwargs):
        """
        Explicitly refresh one or more index, making all operations performed
        since the last refresh available for search.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-refresh.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones, default u'none'
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg force: Force a refresh even if not required
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'force',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_refresh'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def flush(self, index=None, params={}, cb=None, **kwargs):
        """
        Explicitly flush one or more indices.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-flush.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string for all indices
        :arg force: Whether a flush should be forced even if it is not
            necessarily needed ie. if no changes will be committed to the index.
        :arg full: If set to true a new index writer is created and settings
            that have been changed related to the index writer will be refreshed.
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones (default: none)
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        """
        query_params = (
            'force', 'full', 'allow_no_indices', 'expand_wildcards',
            'ignore_indices', 'ignore_unavailable',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_flush'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def create(self, index, body=None, params={}, cb=None, **kwargs):
        """
        Create an index in Elasticsearch.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-create-index.html>`_

        :arg index: The name of the index
        :arg body: The configuration for the index (`settings` and `mappings`)
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit operation timeout
        """
        query_params = ('timeout', 'master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def get(self, index, feature=None, params={}, cb=None, **kwargs):
        """
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-get.html>`_

        :arg index: A comma-separated list of index names
        :arg feature: A comma-separated list of features
        :arg allow_no_indices: Ignore if a wildcard expression resolves to no
            concrete indices (default: false)
        :arg expand_wildcards: Whether wildcard expressions should get expanded
            to open or closed indices (default: open)
        :arg ignore_unavailable: Ignore unavailable indexes (default: false)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, feature], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def open(self, index, params={}, cb=None, **kwargs):
        """
        Open a closed index to make it available for search.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-open-close.html>`_

        :arg index: The name of the index
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit operation timeout
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        """
        query_params = (
            'timeout', 'master_timeout' 'allow_no_indices', 'expand_wildcards',
            'ignore_unavailable',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_open'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def close(self, index, params={}, cb=None, **kwargs):
        """
        Close an index to remove it's overhead from the cluster. Closed index
        is blocked for read/write operations.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-open-close.html>`_

        :arg index: A comma-separated list of indices to close; use `_all` or
            '*' to close all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default u'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit operation timeout
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'master_timeout', 'timeout',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_close'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def delete(self, index, params={}, cb=None, **kwargs):
        """
        Delete an index in Elasticsearch
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-delete-index.html>`_

        :arg index: A comma-separated list of indices to delete; use `_all` or
            '*' to delete all indices
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit operation timeout
        """
        query_params = ('timeout', 'master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def exists(self, index, params={}, cb=None, **kwargs):
        """
        Return a boolean indicating whether given index exists.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-indices-exists.html>`_

        :arg index: A list of indices to check
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default u'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index], **params)
        self.client.fetch(
            self.mk_req(url, method='HEAD', **kwargs),
            callback = cb
        )

    def exists_type(self, index, doc_type, params={}, cb=None, **kwargs):
        """
        Check if a type/types exists in an index/indices.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-types-exists.html>`_

        :arg index: A comma-separated list of index names; use `_all` to check
            the types across all indices
        :arg doc_type: A comma-separated list of document types to check
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones (default: none)
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type], **params)
        self.client.fetch(
            self.mk_req(url, method='HEAD', **kwargs),
            callback = cb
        )

    def put_mapping(self, doc_type, body, index=None, params={}, cb=None, **kwargs):
        """
        Register specific mapping definition for a specific type.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-put-mapping.html>`_

        :arg index: A comma-separated list of index names the alias should
            point to (supports wildcards); use `_all` or omit to perform the
            operation on all indices.
        :arg doc_type: The name of the document type
        :arg body: The mapping definition
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default u'open'
        :arg ignore_conflicts: Specify whether to ignore conflicts while
            updating the mapping (default: false)
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit operation timeout
        """
        query_params(
            'allow_no_indices', 'expand_wildcards', 'ignore_conflicts',
            'ignore_unavailable', 'master_timeout', 'timeout',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_mapping', doc_type], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def get_mapping(self, index=None, doc_type=None, params={}, cb=None, **kwargs):
        """
        Retrieve mapping definition of index or index/type.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-get-mapping.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string for all indices
        :arg doc_type: A comma-separated list of document types
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'ignore_unavailable', 'allow_no_indices', 'expand_wildcards',
            'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_mapping', doc_type], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def get_field_mapping(self, field, index=None, doc_type=None, params={}, cb=None, **kwargs):
        """
        Retrieve mapping definition of a specific field.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-get-field-mapping.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string for all indices
        :arg doc_type: A comma-separated list of document types
        :arg field: A comma-separated list of fields to retrieve the mapping for
        :arg include_defaults: A boolean indicating whether to return default values
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'include_defaults', 'ignore_unavailable', 'allow_no_indices',
            'expand_wildcards', 'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_mapping', doc_type, 'field', field], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def delete_mapping(self, index, doc_type, params={}, cb=None, **kwargs):
        """
        Delete a mapping (type) along with its data.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-delete-mapping.html>`_

        :arg index: A comma-separated list of index names (supports wildcard);
            use `_all` for all indices
        :arg doc_type: A comma-separated list of document types to delete
            (supports wildcards); use `_all` to delete all document types in the
            specified indices.
        :arg master_timeout: Specify timeout for connection to master
        """
        query_params = ('master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_mapping', doc_type], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def put_alias(self, name, index, body=None, params={}, cb=None, **kwargs):
        """
        Create an alias for a specific index/indices.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-aliases.html>`_

        :arg index: A comma-separated list of index names the alias should
            point to (supports wildcards); use `_all` or omit to perform the
            operation on all indices.
        :arg name: The name of the alias to be created or updated
        :arg body: The settings for the alias, such as `routing` or `filter`
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit timestamp for the document
        """
        query_params = ('timeout', 'master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_alias', name], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def exists_alias(self, name, index=None, params={}, cb=None, **kwargs):
        """
        Return a boolean indicating whether given alias exists.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-aliases.html>`_

        :arg name: A comma-separated list of alias names to return
        :arg index: A comma-separated list of index names to filter aliases
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones (default: none)
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_alias', name], **params)
        self.client.fetch(
            self.mk_req(url, method='HEAD', **kwargs),
            callback = cb
        )

    def get_alias(self, index=None, name=None, params={}, cb=None, **kwargs):
        """
        Retrieve a specified alias.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-aliases.html>`_

        :arg name: A comma-separated list of alias names to return
        :arg index: A comma-separated list of index names to filter aliases
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones, default u'none'
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_alias', name], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def get_aliases(self, index=None, name=None, params={}, cb=None, **kwargs):
        """
        Retrieve specified aliases
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-aliases.html>`_
        :arg index: A comma-separated list of index names to filter aliases
        :arg name: A comma-separated list of alias names to filter
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg timeout: Explicit operation timeout
        """
        query_params = ('local', 'timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_aliases', name], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def update_aliases(self, body, params={}, cb=None, **kwargs):
        """
        Update specified aliases.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-aliases.html>`_

        :arg body: The definition of `actions` to perform
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Request timeout
        """
        query_params = ('timeout', 'master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_aliases'], **params)
        self.client.fetch(
            self.mk_req(url, method='Post', **kwargs),
            callback = cb
        )

    def delete_alias(self, index, name, params={}, cb=None, **kwargs):
        """
        Delete specific alias.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-aliases.html>`_

        :arg index: A comma-separated list of index names (supports wildcards);
            use `_all` for all indices
        :arg name: A comma-separated list of aliases to delete (supports
            wildcards); use `_all` to delete all aliases for the specified indices.
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit timestamp for the document
        """
        query_params = ('timeout', 'master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_alias', name], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def put_template(self, name, body, params={}, cb=None, **kwargs):
        """
        Create an index template that will automatically be applied to new
        indices created.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-templates.html>`_

        :arg name: The name of the template
        :arg body: The template definition
        :arg create: Whether the index template should only be added if new or
            can also replace an existing one
        :arg order: The order for this template when merging multiple matching
            ones (higher numbers are merged later, overriding the lower numbers)
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit operation timeout
        :arg flat_settings: Return settings in flat format (default: false)
        """
        query_params = (
            'create', 'order', 'timeout', 'master_timeout', 'flat_settings',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_template', name], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def exists_template(self, name, params={}, cb=None, **kwargs):
        """
        Return a boolean indicating whether given template exists.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-templates.html>`_

        :arg name: The name of the template
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = ('local',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_template', name], **params)
        self.client.fetch(
            self.mk_req(url, method='HEAD', **kwargs),
            callback = cb
        )

    def get_template(self, name=None, params={}, cb=None, **kwargs):
        """
        Retrieve an index template by its name.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-templates.html>`_

        :arg name: The name of the template
        :arg flat_settings: Return settings in flat format (default: false)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = ('flat_settings', 'local',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_template', name], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def delete_template(self, name, params={}, cb=None, **kwargs):
        """
        Delete an index template by its name.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-templates.html>`_

        :arg name: The name of the template
        :arg master_timeout: Specify timeout for connection to master
        :arg timeout: Explicit operation timeout
        """
        query_params = ('timeout', 'master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*['_template', name], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def get_settings(self, index=None, name=None, params={}, cb=None, **kwargs):
        """
        Retrieve settings for one or more (or all) indices.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-get-settings.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg name: The name of the settings that should be included
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones, default u'none'
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg flat_settings: Return settings in flat format (default: false)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'expand_wildcards', 'ignore_indices', 'ignore_unavailable',
            'flat_settings', 'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_settings', name], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def put_settings(self, body, index=None, params={}, cb=None, **kwargs):
        """
        Change specific index level settings in real time.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-update-settings.html>`_

        :arg body: The index settings to be updated
        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default u'open'
        :arg flat_settings: Return settings in flat format (default: false)
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg master_timeout: Specify timeout for connection to master
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'flat_settings',
            'ignore_unavailable', 'master_timeout',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_settings'], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def put_warmer(self, name, body, index=None, doc_type=None, params={}, cb=None, **kwargs):
        """
        Create an index warmer to run registered search requests to warm up the
        index before it is available for search.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-warmers.html>`_

        :arg name: The name of the warmer
        :arg body: The search request definition for the warmer (query, filters,
            facets, sorting, etc)
        :arg index: A comma-separated list of index names to register the warmer
            for; use `_all` or omit to perform the operation on all indices
        :arg doc_type: A comma-separated list of document types to register the
            warmer for; leave empty to perform the operation on all types
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices in the search request
            to warm. (This includes `_all` string or when no indices have been
            specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both, in the search request to
            warm., default u'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed) in the search request
            to warm
        :arg master_timeout: Specify timeout for connection to master
        """
        query_params(
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'master_timeout',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_warmer', name], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', **kwargs),
            callback = cb
        )

    def get_warmer(self, index=None, doc_type=None, name=None, params={}, cb=None, **kwargs):
        """
        Retreieve an index warmer.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-warmers.html>`_

        :arg index: A comma-separated list of index names to restrict the
            operation; use `_all` to perform the operation on all indices
        :arg doc_type: A comma-separated list of document types to restrict the
            operation; leave empty to perform the operation on all types
        :arg name: The name of the warmer (supports wildcards); leave empty to
            get all warmers
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default u'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'local',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_warmer', name], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def delete_warmer(self, index, name, params={}, cb=None, **kwargs):
        """
        Delete an index warmer.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-warmers.html>`_

        :arg index: A comma-separated list of index names to delete warmers from
            (supports wildcards); use `_all` to perform the operation on all indices.
        :arg name: A comma-separated list of warmer names to delete (supports
            wildcards); use `_all` to delete all warmers in the specified indices.
        :arg master_timeout: Specify timeout for connection to master
        """
        query_params = ('master_timeout',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_warmer', name], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def status(self, index=None, params={}, cb=None, **kwargs):
        """
        Get a comprehensive status information of one or more indices.
        `<http://elasticsearch.org/guide/reference/api/admin-indices-_/>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones, default u'none'
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg operation_threading: TODO: ?
        :arg recovery: Return information about shard recovery
        :arg snapshot: TODO: ?
        :arg human: Whether to return time and byte values in human-readable format.
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'operation_threading', 'recovery', 'snapshot',
            'human',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_status'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def stats(self, index=None, metric=None, params={}, cb=None, **kwargs):
        """
        Retrieve statistics on different operations happening on an index.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-stats.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg metric: A comma-separated list of metrics to display. Possible
            values: "_all", "completion", "docs", "fielddata", "filter_cache",
            "flush", "get", "id_cache", "indexing", "merge", "percolate",
            "refresh", "search", "segments", "store", "warmer"
        :arg completion_fields: A comma-separated list of fields for
            `completion` metric (supports wildcards)
        :arg fielddata_fields: A comma-separated list of fields for `fielddata`
            metric (supports wildcards)
        :arg fields: A comma-separated list of fields for `fielddata` and
            `completion` metric (supports wildcards)
        :arg groups: A comma-separated list of search groups for `search` statistics
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones (default: none)
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg human: Whether to return time and byte values in human-readable format.
        :arg level: Return stats aggregated at cluster, index or shard level.
            ("cluster", "indices" or "shards", default: "indices")
        :arg types: A comma-separated list of document types for the `indexing`
            index metric
        """
        query_params = (
            'completion_fields', 'docs', 'fielddata_fields', 'fields', 'groups',
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'human', 'level', 'types',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_stats', metric], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def segments(self, index=None, params={}, cb=None, **kwargs):
        """
        Provide low level segments information that a Lucene index (shard level) is built with.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-segments.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones, default u'none'
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg human: Whether to return time and byte values in human-readable
            format (default: false)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'human',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_segments'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def optimize(self, index=None, params={}, cb=None, **kwargs):
        """
        Explicitly optimize one or more indices through an API.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-optimize.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg flush: Specify whether the index should be flushed after
            performing the operation (default: true)
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones, default u'none'
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg max_num_segments: The number of segments the index should be
            merged into (default: dynamic)
        :arg only_expunge_deletes: Specify whether the operation should only
            expunge deleted documents
        :arg operation_threading: TODO: ?
        :arg wait_for_merge: Specify whether the request should block until the
            merge process is finished (default: true)
        """
        query_params = (
            'flush', 'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'max_num_segments', 'only_expunge_deletes',
            'operation_threading', 'wait_for_merge',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_optimize'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def validate_query(self, index=None, doc_type=None, body=None, params={}, cb=None, **kwargs):
        """
        Validate a potentially expensive query without executing it.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-validate.html>`_

        :arg index: A comma-separated list of index names to restrict the operation;
            use `_all` or empty string to perform the operation on all indices
        :arg doc_type: A comma-separated list of document types to restrict the
            operation; leave empty to perform the operation on all types
        :arg body: The query definition
        :arg explain: Return detailed information about the error
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones (default: none)
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg operation_threading: TODO: ?
        :arg q: Query in the Lucene query string syntax
        :arg source: The URL-encoded query definition (instead of using the
            request body)
        """
        query_params(
            'explain', 'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable', 'operation_threading', 'q', 'source',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_validate', 'query'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def clear_cache(self, index=None, params={}, cb=None, **kwargs):
        """
        Clear either all caches or specific cached associated with one ore more indices.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-clearcache.html>`_

        :arg index: A comma-separated list of index name to limit the operation
        :arg field_data: Clear field data
        :arg fielddata: Clear field data
        :arg fields: A comma-separated list of fields to clear when using the
            `field_data` parameter (default: all)
        :arg filter: Clear filter caches
        :arg filter_cache: Clear filter caches
        :arg filter_keys: A comma-separated list of keys to clear when using
            the `filter_cache` parameter (default: all)
        :arg id: Clear ID caches for parent/child
        :arg id_cache: Clear ID caches for parent/child
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones (default: none)
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        :arg index: A comma-separated list of index name to limit the operation
        :arg recycler: Clear the recycler cache
        """
        query_params(
            'field_data', 'fielddata', 'fields', 'filter', 'filter_cache',
            'filter_keys', 'id', 'id_cache', 'allow_no_indices',
            'expand_wildcards', 'ignore_indices', 'ignore_unavailable', 'index',
            'recycler',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_cache', 'clear'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def recovery(self, index=None, params={}, cb=None, **kwargs):
        """
        The indices recovery API provides insight into on-going shard
        recoveries. Recovery status may be reported for specific indices, or
        cluster-wide.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/indices-recovery.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg active_only: Display only those recoveries that are currently on-
            going (default: 'false')
        :arg detailed: Whether to display detailed information about shard
            recovery (default: 'false')
        :arg human: Whether to return time and byte values in human-readable
            format. (default: 'false')

        """
        query_params = ('active_only', 'detailed', 'human',)
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_recovery'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def snapshot_index(self, index=None, params={}, cb=None, **kwargs):
        """
        Explicitly perform a snapshot through the gateway of one or more indices (backup them).
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/indices-gateway-snapshot.html>`_

        :arg index: A comma-separated list of index names; use `_all` or empty
            string for all indices
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all` string or
            when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :arg ignore_indices: When performed on multiple indices, allows to
            ignore `missing` ones (default: none)
        :arg ignore_unavailable: Whether specified concrete indices should be ignored
            when unavailable (missing or closed)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_indices',
            'ignore_unavailable',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, '_gateway', 'snapshot'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )
