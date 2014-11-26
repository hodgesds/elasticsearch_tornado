import sys
from   abc import ABCMeta, abstractmethod
from   tornado.httpclient import AsyncHTTPClient, HTTPRequest

PY2 = sys.version_info[0] == 2
if PY2:
    from urllib import urlencode
else:
    from urllib.parse import urlencode


class BaseClient(object):

    __metaclass__ = ABCMeta

    def __init__(self,
            host         = 'localhost',
            port         = 9200,
            prefix       = '',
            method       = 'http',
            ssl          = False,
            verify_certs = True,
            ca_certs     = '',
            *args,
            **kwargs
    ):
        # TODO: curlclient in tornado for proxy requests
        self.base_url = "%s://%s:%s%s" % (method, host, port, prefix)
        self.certs    = ca_certs
        self.client   = AsyncHTTPClient()

    def mk_req(self, url, **kwargs):
        req_url = self.base_url + url
        return HTTPRequest(req_url, ca_certs=self.certs, **kwargs)

    def mk_url(self, *args, **kwargs):
        params = urlencode(kwargs)
        url = '/' + '/'.join([x for x in args if x])
        return url + params

    def ping(self, cb=None, **kwargs):
        self.client.fetch(
            self.mk_req('', method='HEAD', **kwargs),
            callback = cb
        )

    def info(self, cb=None, **kwargs):
        """
        Get the basic info from the current cluster.
        """
        self.client.fetch(
            self.mk_req('', method='GET', **kwargs),
            callback = cb
        )

    def create(self,
            index,
            doc_type,
            body,
            doc_id = None,
            params = {},
            cb     = None,
            **kwargs
        ):
        """
        Adds a typed JSON document in a specific index, making it searchable.
        Behind the scenes this method calls index(..., op_type='create')
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-index_.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document
        :arg doc_id: Document ID
        :arg body: The document
        :arg consistency: Explicit write consistency setting for the operation
        :arg id: Specific document ID (when the POST method is used)
        :arg parent: ID of the parent document
        :arg percolate: Percolator queries to execute while indexing the document
        :arg refresh: Refresh the index after performing the operation
        :arg replication: Specific replication type (default: sync)
        :arg routing: Specific routing value
        :arg timeout: Explicit operation timeout
        :arg timestamp: Explicit timestamp for the document
        :arg ttl: Expiration time for the document
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        method = 'PUT' if doc_id else 'POST'
        query_params = ('consistency', 'op_type', 'parent', 'refresh',
            'replication', 'routing', 'timeout', 'timestamp', 'ttl', 'version',
            'version_type',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id], **params)
        self.client.fetch(
            self.mk_req(url, method=method, body=body, **kwargs),
            callback = cb
        )


    def index(self,
            index,
            doc_type,
            body,
            doc_id = None,
            params = {},
            cb     = None,
            **kwargs
        ):
        """
        Adds or updates a typed JSON document in a specific index, making it searchable.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-index_.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document
        :arg body: The document
        :arg doc_id: Document ID
        :arg consistency: Explicit write consistency setting for the operation
        :arg op_type: Explicit operation type (default: index)
        :arg parent: ID of the parent document
        :arg refresh: Refresh the index after performing the operation
        :arg replication: Specific replication type (default: sync)
        :arg routing: Specific routing value
        :arg timeout: Explicit operation timeout
        :arg timestamp: Explicit timestamp for the document
        :arg ttl: Expiration time for the document
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        method = 'PUT' if doc_id else 'POST'
        query_params = ('consistency', 'op_type', 'parent', 'refresh',
            'replication', 'routing', 'timeout', 'timestamp', 'ttl', 'version',
            'version_type',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id], **params)
        self.client.fetch(
            self.mk_req(url, method=method, body=body, **kwargs),
            callback = cb
        )

    def exists(self, index, doc_id, doc_type='_all', cb=None, **kwargs):
        """
        Returns a boolean indicating whether or not given document exists in Elasticsearch.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-get.html>`_
        :arg index: The name of the index
        :arg doc_id: The document ID
        :arg doc_type: The type of the document (uses `_all` by default to
            fetch the first document matching the ID across all types)
        :arg parent: The ID of the parent document
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg realtime: Specify whether to perform the operation in realtime or
            search mode
        :arg refresh: Refresh the shard containing the document before
            performing the operation
        :arg routing: Specific routing value
        """
        query_params = (
            'parent', 'preference', 'realtime', 'refresh', 'routing',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id], **params)
        self.client.fetch(
            self.mk_req(url, method='HEAD', **kwargs),
            callback = cb
        )

    def get(self, index, doc_id, doc_type='_all', params={}, cb=None, **kwargs):
        """
        Get a typed JSON document from the index based on its id.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-get.html>`_
        :arg index: The name of the index
        :arg doc_id: The document ID
        :arg doc_type: The type of the document (uses `_all` by default to
            fetch the first document matching the ID across all types)
        :arg _source: True or false to return the _source field or not, or a
            list of fields to return
        :arg _source_exclude: A list of fields to exclude from the returned
            _source field
        :arg _source_include: A list of fields to extract and return from the
            _source field
        :arg fields: A comma-separated list of fields to return in the response
        :arg parent: The ID of the parent document
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg realtime: Specify whether to perform the operation in realtime or
            search mode
        :arg refresh: Refresh the shard containing the document before
            performing the operation
        :arg routing: Specific routing value
        :arg version: Explicit version number for concurrency control
        :arg version_type: Explicit version number for concurrency control
        """
        query_params = ('_source', '_source_exclude', '_source_include',
            'fields', 'parent', 'preference', 'realtime', 'refresh', 'routing',
            'version', 'version_type',
        )
        params = dict((k,v) for k, v in params.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def get_source(self,
            index,
            doc_id,
            doc_type = '_all',
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Get the source of a document by it's index, type and id.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-get.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document (uses `_all` by default to
            fetch the first document matching the ID across all types)
        :arg doc_id: The document ID
        :arg _source: True or false to return the _source field or not, or a
            list of fields to return
        :arg _source_exclude: A list of fields to exclude from the returned
            _source field
        :arg _source_include: A list of fields to extract and return from the
            _source field
        :arg parent: The ID of the parent document
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg realtime: Specify whether to perform the operation in realtime or search mode
        :arg refresh: Refresh the shard containing the document before
            performing the operation
        :arg routing: Specific routing value
        :arg version: Explicit version number for concurrency control
        :arg version_type: Explicit version number for concurrency control
        """
        query_params = ('_source', '_source_exclude', '_source_include',
            'parent', 'preference', 'realtime', 'refresh', 'routing', 'version',
            'version_type',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id, '_source'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def mget(self,
            body,
            index    = None,
            doc_type = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Get multiple documents based on an index, type (optional) and ids.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-multi-get.html>`_
        :arg body: Document identifiers; can be either `docs` (containing full
            document information) or `ids` (when index and type is provided in the URL.
        :arg index: The name of the index
        :arg doc_type: The type of the document
        :arg _source: True or false to return the _source field or not, or a
            list of fields to return
        :arg _source_exclude: A list of fields to exclude from the returned
            _source field
        :arg _source_include: A list of fields to extract and return from the
            _source field
        :arg fields: A comma-separated list of fields to return in the response
        :arg parent: The ID of the parent document
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg realtime: Specify whether to perform the operation in realtime or search mode
        :arg refresh: Refresh the shard containing the document before
            performing the operation
        :arg routing: Specific routing value
        """
        query_params = ('_source', '_source_exclude', '_source_include',
            'fields', 'parent', 'preference', 'realtime', 'refresh', 'routing',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_mget'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def update(self,
            index,
            doc_type,
            doc_id,
            body   = None,
            params = {},
            cb     = None,
            **kwargs
        ):
        """
        Update a document based on a script or partial data provided.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-update.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document
        :arg doc_id: Document ID
        :arg body: The request definition using either `script` or partial `doc`
        :arg consistency: Explicit write consistency setting for the operation
        :arg fields: A comma-separated list of fields to return in the response
        :arg lang: The script language (default: mvel)
        :arg parent: ID of the parent document
        :arg refresh: Refresh the index after performing the operation
        :arg replication: Specific replication type (default: sync)
        :arg retry_on_conflict: Specify how many times should the operation be
            retried when a conflict occurs (default: 0)
        :arg routing: Specific routing value
        :arg script: The URL-encoded script definition (instead of using request body)
        :arg timeout: Explicit operation timeout
        :arg timestamp: Explicit timestamp for the document
        :arg ttl: Expiration time for the document
        :arg version: Explicit version number for concurrency control
        :arg version_type: Explicit version number for concurrency control
        """
        query_params('consistency', 'fields', 'lang', 'parent', 'refresh',
            'replication', 'retry_on_conflict', 'routing', 'script', 'timeout',
            'timestamp', 'ttl', 'version', 'version_type',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id, '_update'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', body=body, **kwargs),
            callback = cb
        )


    def search(self,
            index    = None,
            doc_type = None,
            body     = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Execute a search query and get back search hits that match the query.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-search.html>`_
        :arg index: A comma-separated list of index names to search; use `_all`
            or empty string to perform the operation on all indices
        :arg doc_type: A comma-separated list of document types to search;
            leave empty to perform the operation on all types
        :arg body: The search definition using the Query DSL
        :arg _source: True or false to return the _source field or not, or a
            list of fields to return
        :arg _source_exclude: A list of fields to exclude from the returned
            _source field
        :arg _source_include: A list of fields to extract and return from the
            _source field
        :arg analyze_wildcard: Specify whether wildcard and prefix queries
            should be analyzed (default: false)
        :arg analyzer: The analyzer to use for the query string
        :arg default_operator: The default operator for query string query (AND
            or OR) (default: OR)
        :arg df: The field to use as default where no field prefix is given in
            the query string
        :arg explain: Specify whether to return detailed information about
            score computation as part of a hit
        :arg fields: A comma-separated list of fields to return as part of a hit
        :arg indices_boost: Comma-separated list of index boosts
        :arg lenient: Specify whether format-based query failures (such as
            providing text to a numeric field) should be ignored
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg lowercase_expanded_terms: Specify whether query terms should be lowercased
        :arg from\_: Starting offset (default: 0)
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg q: Query in the Lucene query string syntax
        :arg routing: A comma-separated list of specific routing values
        :arg scroll: Specify how long a consistent view of the index should be
            maintained for scrolled search
        :arg search_type: Search operation type
        :arg size: Number of hits to return (default: 10)
        :arg sort: A comma-separated list of <field>:<direction> pairs
        :arg source: The URL-encoded request definition using the Query DSL
            (instead of using request body)
        :arg stats: Specific 'tag' of the request for logging and statistical purposes
        :arg suggest_field: Specify which field to use for suggestions
        :arg suggest_mode: Specify suggest mode (default: missing)
        :arg suggest_size: How many suggestions to return in response
        :arg suggest_text: The source text for which the suggestions should be returned
        :arg timeout: Explicit operation timeout
        :arg version: Specify whether to return document version as part of a hit
        """
        query_params = ('_source', '_source_exclude', '_source_include',
            'analyze_wildcard', 'analyzer', 'default_operator', 'df', 'explain',
            'fields', 'indices_boost', 'lenient', 'allow_no_indices',
            'expand_wildcards', 'ignore_unavailable',
            'lowercase_expanded_terms', 'from_', 'preference', 'q', 'routing',
            'scroll', 'search_type', 'size', 'sort', 'source', 'stats',
            'suggest_field', 'suggest_mode', 'suggest_size', 'suggest_text',
            'timeout', 'version',
        )
        if 'from_' in params:
            params['from'] = params.pop('from_')

        if doc_type and not index:
            index = '_all'
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_search'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def search_shards(self,
            index    = None,
            doc_type = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        The search shards api returns the indices and shards that a search
        request would be executed against. This can give useful feedback for working
        out issues or planning optimizations with routing and shard preferences.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/search-shards.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both. (default: '"open"')
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg local: Return local information, do not retrieve the state from
            master node (default: false)
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg routing: Specific routing value
        """
        query_params('allow_no_indices', 'expand_wildcards',
            'ignore_unavailable', 'local', 'preference', 'routing',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_search_shards'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def search_template(self,
            index    = None,
            doc_type = None,
            body     = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        A query that accepts a query template and a map of key/value pairs to
        fill in template parameters.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/query-dsl-template-query.html>`_
        :arg index: A comma-separated list of index names to search; use `_all`
            or empty string to perform the operation on all indices
        :arg doc_type: A comma-separated list of document types to search; leave
            empty to perform the operation on all types
        :arg body: The search definition template and its params
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg routing: A comma-separated list of specific routing values
        :arg scroll: Specify how long a consistent view of the index should be
            maintained for scrolled search
        :arg search_type: Search operation type
        """
        query_params = ('allow_no_indices', 'expand_wildcards',
            'ignore_unavailable', 'preference', 'routing', 'scroll',
            'search_type',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_search', 'template'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def explain(self,
            index,
            doc_type,
            doc_id,
            body   = None,
            params = {},
            cb     = None,
            **kwargs
        ):
        """
        The explain api computes a score explanation for a query and a specific
        document. This can give useful feedback whether a document matches or
        didn't match a specific query.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-explain.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document
        :arg doc_id: The document ID
        :arg body: The query definition using the Query DSL
        :arg _source: True or false to return the _source field or not, or a
            list of fields to return
        :arg _source_exclude: A list of fields to exclude from the returned
            _source field
        :arg _source_include: A list of fields to extract and return from the
            _source field
        :arg analyze_wildcard: Specify whether wildcards and prefix queries in
            the query string query should be analyzed (default: false)
        :arg analyzer: The analyzer for the query string query
        :arg default_operator: The default operator for query string query (AND
            or OR), (default: OR)
        :arg df: The default field for query string query (default: _all)
        :arg fields: A comma-separated list of fields to return in the response
        :arg lenient: Specify whether format-based query failures (such as
            providing text to a numeric field) should be ignored
        :arg lowercase_expanded_terms: Specify whether query terms should be lowercased
        :arg parent: The ID of the parent document
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg q: Query in the Lucene query string syntax
        :arg routing: Specific routing value
        :arg source: The URL-encoded query definition (instead of using the
            request body)
        """
        query_params = ('_source', '_source_exclude', '_source_include',
            'analyze_wildcard', 'analyzer', 'default_operator', 'df', 'fields',
            'lenient', 'lowercase_expanded_terms', 'parent', 'preference', 'q',
            'routing', 'source',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id, '_explain'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )


    def scroll(self, scroll_id, params={}, cb=None, **kwargs):
        """
        Scroll a search request created by specifying the scroll parameter.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-request-scroll.html>`_
        :arg scroll_id: The scroll ID
        :arg scroll: Specify how long a consistent view of the index should be
            maintained for scrolled search
        """
        query_params = ('scroll',)
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*['/_search/scroll'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=scroll_id, **kwargs),
            callback = cb
        )

    def clear_scroll(self,
            scroll_id = None,
            body      = None,
            params    = {},
            cb        = None,
            **kwargs
        ):
        """
        Clear the scroll request created by specifying the scroll parameter to
        search.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-request-scroll.html>`_
        :arg scroll_id: The scroll ID or a list of scroll IDs
        :arg body: A comma-separated list of scroll IDs to clear if none was
            specified via the scroll_id parameter
        """
        url = self.mk_url(*['_search', 'scroll', scroll_id])
        self.client.fetch(
            self.mk_req(url, method='DELETE', body=body, **kwargs),
            callback = cb
        )

    def delete(self, index, doc_type, doc_id, params={}, cb=None, **kwargs):
        """
        Delete a typed JSON document from a specific index based on its id.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-delete.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document
        :arg doc_id: The document ID
        :arg consistency: Specific write consistency setting for the operation
        :arg parent: ID of parent document
        :arg refresh: Refresh the index after performing the operation
        :arg replication: Specific replication type (default: sync)
        :arg routing: Specific routing value
        :arg timeout: Explicit operation timeout
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        query_params('consistency', 'parent', 'refresh', 'replication',
            'routing', 'timeout', 'version', 'version_type',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def count(self,
            index    = None,
            doc_type = None,
            body     = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Execute a query and get the number of matches for that query.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-count.html>`_
        :arg index: A comma-separated list of indices to restrict the results
        :arg doc_type: A comma-separated list of types to restrict the results
        :arg body: A query to restrict the results (optional)
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg min_score: Include only documents with a specific `_score` value in the result
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg q: Query in the Lucene query string syntax
        :arg routing: Specific routing value
        :arg source: The URL-encoded query definition (instead of using the request body)
        """
        query_params('allow_no_indices', 'expand_wildcards',
            'ignore_unavailable', 'min_score', 'preference', 'q', 'routing',
            'source',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_count'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', body=body, **kwargs),
            callback = cb
        )


    def bulk(self,
            body,
            index    = None,
            doc_type = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Perform many index/delete operations in a single API call.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-bulk.html>`_
        See the :func:`~elasticsearch.helpers.bulk` helper function for a more
        friendly API.
        :arg body: The operation definition and data (action-data pairs), as
            either a newline separated string, or a sequence of dicts to
            serialize (one per row).
        :arg index: Default index for items which don't provide one
        :arg doc_type: Default document type for items which don't provide one
        :arg consistency: Explicit write consistency setting for the operation
        :arg refresh: Refresh the index after performing the operation
        :arg routing: Specific routing value
        :arg replication: Explicitly set the replication type (default: sync)
        :arg timeout: Explicit operation timeout
        """
        query_params(
            'consistency', 'refresh', 'routing', 'replication', 'timeout',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_bulk'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', body=body, **kwargs),
            callback = cb
        )


    def msearch(self,
            body,
            index    = None,
            doc_type = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Execute several search requests within the same API.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-multi-search.html>`_
        :arg body: The request definitions (metadata-search request definition
            pairs), as either a newline separated string, or a sequence of
            dicts to serialize (one per row).
        :arg index: A comma-separated list of index names to use as default
        :arg doc_type: A comma-separated list of document types to use as default
        :arg search_type: Search operation type
        """
        query_params = ('search_type',)
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_msearch'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )


    def delete_by_query(self,
            index,
            doc_type = None,
            body     = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Delete documents from one or more indices and one or more types based on a query.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/docs-delete-by-query.html>`_
        :arg index: A comma-separated list of indices to restrict the operation;
            use `_all` to perform the operation on all indices
        :arg doc_type: A comma-separated list of types to restrict the operation
        :arg body: A query to restrict the operation specified with the Query
            DSL
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg analyzer: The analyzer to use for the query string
        :arg consistency: Specific write consistency setting for the operation
        :arg default_operator: The default operator for query string query (AND
            or OR), default u'OR'
        :arg df: The field to use as default where no field prefix is given in
            the query string
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default u'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg q: Query in the Lucene query string syntax
        :arg replication: Specific replication type, default u'sync'
        :arg routing: Specific routing value
        :arg source: The URL-encoded query definition (instead of using the
            request body)
        :arg timeout: Explicit operation timeout
        """
        query_params(
            'allow_no_indices', 'analyzer', 'consistency', 'default_operator',
            'df', 'expand_wildcards', 'ignore_unavailable', 'q', 'replication',
            'routing', 'source', 'timeout',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_query'], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', body=body, **kwargs),
            callback = cb
        )

    def suggest(self, body, index=None, params={}, cb=None, **kwargs):
        """
        The suggest feature suggests similar looking terms based on a provided
        text by using a suggester.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-search.html>`_
        :arg index: A comma-separated list of index names to restrict the operation;
            use `_all` or empty string to perform the operation on all indices
        :arg body: The request definition
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg routing: Specific routing value
        :arg source: The URL-encoded request definition (instead of using request body)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'preference', 'routing', 'source',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_query'], **params)
        self.client.fetch(
            self.mk_req(url, method='POST', body=body, **kwargs),
            callback = cb
        )

    def percolate(self,
            index,
            doc_type,
            doc_id = None,
            body   = None,
            params = {},
            cb     = None,
            **kwargs
        ):
        """
        The percolator allows to register queries against an index, and then
        send percolate requests which include a doc, and getting back the
        queries that match on that doc out of the set of registered queries.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-percolate.html>`_
        :arg index: The index of the document being percolated.
        :arg doc_type: The type of the document being percolated.
        :arg doc_id: Substitute the document in the request body with a document
            that is known by the specified id. On top of the id, the index and
            type parameter will be used to retrieve the document from within the
            cluster.
        :arg body: The percolator request definition using the percolate DSL
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg percolate_format: Return an array of matching query IDs instead of
            objects
        :arg percolate_index: The index to percolate the document into. Defaults
            to index.
        :arg percolate_type: The type to percolate document into. Defaults to
            type.
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg routing: A comma-separated list of specific routing values
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        query_params(
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'percolate_format', 'percolate_index', 'percolate_type',
            'preference', 'routing', 'version', 'version_type',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id, '_percolate'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def mpercolate(self,
            body,
            index    = None,
            doc_type = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        The percolator allows to register queries against an index, and then
        send percolate requests which include a doc, and getting back the
        queries that match on that doc out of the set of registered queries.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-percolate.html>`_
        :arg index: The index of the document being count percolated to use as
            default
        :arg doc_type: The type of the document being percolated to use as
            default.
        :arg body: The percolate request definitions (header & body pair),
            separated by newlines
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_mpercolate'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def count_percolate(self,
            index,
            doc_type,
            doc_id = None,
            body   = None,
            params = {},
            **kwargs
        ):
        """
        The percolator allows to register queries against an index, and then
        send percolate requests which include a doc, and getting back the
        queries that match on that doc out of the set of registered queries.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-percolate.html>`_
        :arg index: The index of the document being count percolated.
        :arg doc_type: The type of the document being count percolated.
        :arg doc_id: Substitute the document in the request body with a document
            that is known by the specified id. On top of the id, the index and
            type parameter will be used to retrieve the document from within the
            cluster.
        :arg body: The count percolator request definition using the percolate
            DSL
        :arg allow_no_indices: Whether to ignore if a wildcard indices
            expression resolves into no concrete indices. (This includes `_all`
            string or when no indices have been specified)
        :arg expand_wildcards: Whether to expand wildcard expression to concrete
            indices that are open, closed or both., default 'open'
        :arg ignore_unavailable: Whether specified concrete indices should be
            ignored when unavailable (missing or closed)
        :arg percolate_index: The index to count percolate the document into.
            Defaults to index.
        :arg percolate_type: The type to count percolate document into. Defaults
            to type.
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random)
        :arg routing: A comma-separated list of specific routing values
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        query_params = (
            'allow_no_indices', 'expand_wildcards', 'ignore_unavailable',
            'percolate_index', 'percolate_type', 'preference', 'routing',
            'version', 'version_type',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id, '_percolate', 'count'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def mlt(self,
            index,
            doc_type,
            doc_id,
            body   = None,
            params = {},
            cb     = None,
            **kwargs
        ):
        """
        Get documents that are "like" a specified document.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-more-like-this.html>`_
        :arg index: The name of the index
        :arg doc_type: The type of the document (use `_all` to fetch the first
            document matching the ID across all types)
        :arg id: The document ID
        :arg body: A specific search request definition
        :arg boost_terms: The boost factor
        :arg include: Whether to include the queried document from the response
        :arg max_doc_freq: The word occurrence frequency as count: words with
            higher occurrence in the corpus will be ignored
        :arg max_query_terms: The maximum query terms to be included in the generated query
        :arg max_word_length: The minimum length of the word: longer words will be ignored
        :arg min_doc_freq: The word occurrence frequency as count: words with
            lower occurrence in the corpus will be ignored
        :arg min_term_freq: The term frequency as percent: terms with lower
            occurence in the source document will be ignored
        :arg min_word_length: The minimum length of the word: shorter words will be ignored
        :arg mlt_fields: Specific fields to perform the query against
        :arg percent_terms_to_match: How many terms have to match in order to
            consider the document a match (default: 0.3)
        :arg routing: Specific routing value
        :arg search_from: The offset from which to return results
        :arg search_indices: A comma-separated list of indices to perform the
            query against (default: the index containing the document)
        :arg search_query_hint: The search query hint
        :arg search_scroll: A scroll search request definition
        :arg search_size: The number of documents to return (default: 10)
        :arg search_source: A specific search request definition (instead of
            using the request body)
        :arg search_type: Specific search type (eg. `dfs_then_fetch`, `count`, etc)
        :arg search_types: A comma-separated list of types to perform the query
            against (default: the same type as the document)
        :arg stop_words: A list of stop words to be ignored
        """
        query_params('boost_terms', 'include', 'max_doc_freq',
            'max_query_terms', 'max_word_length', 'min_doc_freq',
            'min_term_freq', 'min_word_length', 'mlt_fields',
            'percent_terms_to_match', 'routing', 'search_from',
            'search_indices', 'search_query_hint', 'search_scroll',
            'search_size', 'search_source', 'search_type', 'search_types',
            'stop_words',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id, '_mlt'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def termvector(self,
            index,
            doc_type,
            doc_id,
            body   = None,
            params = {},
            cb     = None,
            **kwargs
        ):
        """
        Added in 1.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/search-termvectors.html>`_
        :arg index: The index in which the document resides.
        :arg doc_type: The type of the document.
        :arg id: The id of the document.
        :arg body: Define parameters. See documentation.
        :arg field_statistics: Specifies if document count, sum of document
            frequencies and sum of total term frequencies should be returned.,
            default True
        :arg fields: A comma-separated list of fields to return.
        :arg offsets: Specifies if term offsets should be returned., default
            True
        :arg parent: Parent id of documents.
        :arg payloads: Specifies if term payloads should be returned., default
            True
        :arg positions: Specifies if term positions should be returned., default
            True
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random).
        :arg realtime: Specifies if request is real-time as opposed to near-
            real-time (default: true).
        :arg routing: Specific routing value.
        :arg term_statistics: Specifies if total term frequency and document
            frequency should be returned., default False
        """
        query_params = (
            'field_statistics', 'fields', 'offsets', 'parent', 'payloads',
            'positions', 'preference', 'realtime', 'routing', 'term_statistics',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, doc_id, '_termvector'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def mtermvectors(self,
            index    = None,
            doc_type = None,
            body     = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        Multi termvectors API allows to get multiple termvectors based on an
        index, type and id.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/docs-multi-termvectors.html>`_
        :arg index: The index in which the document resides.
        :arg doc_type: The type of the document.
        :arg body: Define ids, parameters or a list of parameters per document
            here. You must at least provide a list of document ids. See
            documentation.
        :arg field_statistics: Specifies if document count, sum of document
            frequencies and sum of total term frequencies should be returned.
            Applies to all returned documents unless otherwise specified in body
            "params" or "docs"., default True
        :arg fields: A comma-separated list of fields to return. Applies to all
            returned documents unless otherwise specified in body "params" or
            "docs".
        :arg ids: A comma-separated list of documents ids. You must define ids
            as parameter or set "ids" or "docs" in the request body
        :arg offsets: Specifies if term offsets should be returned. Applies to
            all returned documents unless otherwise specified in body "params"
            or "docs"., default True
        :arg parent: Parent id of documents. Applies to all returned documents
            unless otherwise specified in body "params" or "docs".
        :arg payloads: Specifies if term payloads should be returned. Applies to
            all returned documents unless otherwise specified in body "params"
            or "docs"., default True
        :arg positions: Specifies if term positions should be returned. Applies
            to all returned documents unless otherwise specified in body
            "params" or "docs"., default True
        :arg preference: Specify the node or shard the operation should be
            performed on (default: random) .Applies to all returned documents
            unless otherwise specified in body "params" or "docs".
        :arg routing: Specific routing value. Applies to all returned documents
            unless otherwise specified in body "params" or "docs".
        :arg term_statistics: Specifies if total term frequency and document
            frequency should be returned. Applies to all returned documents
            unless otherwise specified in body "params" or "docs"., default
            False
        """
        query_params(
            'field_statistics', 'fields', 'ids', 'offsets', 'parent',
            'payloads', 'positions', 'preference', 'routing', 'term_statistics',
        )
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_mtermvectors'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )


    def benchmark(self,
            index    = None,
            doc_type = None,
            body     = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        The benchmark API provides a standard mechanism for submitting queries
        and measuring their performance relative to one another.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/search-benchmark.html>`_
        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg doc_type: The name of the document type
        :arg body: The search definition using the Query DSL
        :arg verbose: Specify whether to return verbose statistics about each
            iteration (default: false)
        """
        query_params = ('verbose',)
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*[index, doc_type, '_bench'], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', body=body, **kwargs),
            callback = cb
        )

    def abort_benchmark(self, name=None, params={}, cb=None, **kwargs):
        """
        Aborts a running benchmark.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/search-benchmark.html>`_
        :arg name: A benchmark name
        """
        url = self.mk_url(*['_bench', 'abort', name])
        self.client.fetch(
            self.mk_req(url, method='POST', **kwargs),
            callback = cb
        )

    def list_benchmarks(self,
            index    = None,
            doc_type = None,
            params   = {},
            cb       = None,
            **kwargs
        ):
        """
        View the progress of long-running benchmarks.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/master/search-benchmark.html>`_
        :arg index: A comma-separated list of index names; use `_all` or empty
            string to perform the operation on all indices
        :arg doc_type: The name of the document type
        """
        url = self.mk_url(*[index, doc_type, '_bench'], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def put_script(self, lang, script_id, body, params={}, cb=None, **kwargs):
        """
        Create a script in given language with specified ID.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/modules-scripting.html>`_
        :arg lang: Script language
        :arg script_id: Script ID
        :arg body: The document
        :arg op_type: Explicit operation type, default u'index'
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        query_params = ('op_type', 'version', 'version_type',)
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*['_scripts', lang, script_id], **params)
        self.client.fetch(
            self.mk_req(url, method='PUT', body=body, **kwargs),
            callback = cb
        )

    def get_script(self, lang, script_id, params={}, cb=None, **kwargs):
        """
        Retrieve a script from the API.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/modules-scripting.html>`_
        :arg lang: Script language
        :arg script_id: Script ID
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        query_params = ('version', 'version_type',)
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*['_scripts', lang, script_id], **params)
        self.client.fetch(
            self.mk_req(url, method='GET', **kwargs),
            callback = cb
        )

    def delete_script(self, lang, script_id, params={}, cb=None, **kwargs):
        """
        Remove a stored script from elasticsearch.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/modules-scripting.html>`_
        :arg lang: Script language
        :arg script_id: Script ID
        :arg version: Explicit version number for concurrency control
        :arg version_type: Specific version type
        """
        query_params = ('version', 'version_type',)
        params = dict((k,v) for k, v in kwargs.items() if k in query_params and v)
        url = self.mk_url(*['_scripts', lang, script_id], **params)
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )

    def put_template(self, temp_id, body, params={}, cb=None, **kwargs):
        """
        Create a search template.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-template.html>`_
        :arg temp_id: Template ID
        :arg body: The document
        """
        url = self.mk_url(*['_search', 'template', temp_id])
        self.client.fetch(
            self.mk_req(url, method='PUT', body=body, **kwargs),
            callback = cb
        )

    def get_template(self, temp_id, body=None, params={}, cb=None, **kwargs):
        """
        Retrieve a search template.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-template.html>`_
        :arg temp_id: Template ID
        :arg body: The document
        """
        url = self.mk_url(*['_search', 'template', temp_id])
        self.client.fetch(
            self.mk_req(url, method='GET', body=body, **kwargs),
            callback = cb
        )

    def delete_template(self, temp_id=None, params={}, cb=None, **kwargs):
        """
        Delete a search template.
        `<http://www.elasticsearch.org/guide/en/elasticsearch/reference/current/search-template.html>`_
        :arg temp_id: Template ID
        """
        url = self.mk_url(*['_search', 'template', temp_id])
        self.client.fetch(
            self.mk_req(url, method='DELETE', **kwargs),
            callback = cb
        )
