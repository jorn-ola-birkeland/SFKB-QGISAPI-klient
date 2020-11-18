# coding: utf-8

"""
    Oppdateringsgrensesnitt for SFKB

    # NGIS-OpenAPI  Grov oversikt over funksjonalitet:   - Hente liste over tilgjengelige datasett    - Hente metadata for et bestemt datasett   - Hente data fra et bestemt datasett     - Med lesetilgang eller skrivetilgang (medfører låsing)       - områdebegrensning       - egenskapsspørring (begrenset i første versjon til bygningsnummer eller lokalid)   - Lagre data til et bestemt datasett     - Operasjoner som håndteres: nytt objekt, endre objekt og slett objekt  ## Generelle prinsipper for systemet  ### Delt geometri  Flater består av avgrensningslinjer som ligger lagret som egne objekter. På den måten kan en linje avgrense ingen, én eller flere flater. Det er likevel slik at flater hentes ut og lagres med egen geometri for å gjøre det enklere å tegne opp datene, men ved endring av (delte) linjer og flater må det tas hensyn til delt geometri. Forsøk på endring av linje eller flate uten tilsvarende endring av evt. delt geometri vil bli avvist av systemet.  ### Låsing  Dette er nærmere beskrevet i de aktuelle kallene.  Foreløpig er det kun `user_lock` som er støttet. Det betyr at data må hentes ut med `user_lock` før de kan sendes inn med endringer.  ### Porsjonering  All uthenting av feature-objekter vil kunne bli porsjonert av serveren, se `limit`-parameteret.   ### Koordinatsystemer og transformasjon  Dersom annet koordinatsystem enn det som ligger i dataset skal brukes (se `GET /datasets/{datasetId}`) må koordinatsystem angis med `crs_EPSG`-parameteret. Dette styrer data som sendes inn, data som hentes ut og koordinatsystemet i `bbox`-parameteret i kallet. For å bytte rekkefølge på aksene brukes `crs_normalized_for_visualization`-parameteret.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class LocksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_dataset_locks(self, x_client_product_version, dataset_id, **kwargs):  # noqa: E501
        """Fjerne alle låser brukeren har i et bestemt dataset  # noqa: E501

        Fjerne alle låser brukeren har i et bestemt dataset   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dataset_locks(x_client_product_version, dataset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_client_product_version: Brukes for å kunne identifisere klienten som er brukt (required)
        :param str dataset_id: UUID of the dataset to get (required)
        :param str locking_type: Angir låsetype som skal brukes (foreløpig er kun `user_lock` støttet). Krever at brukeren har skrivetilgang mot dataset'et.  *user_lock*  Hver bruker har én lås per dataset. Hver gang data hentes ut med `user_lock` legges objektene til denne låsen.  Alle objekter i låsen låses opp neste gang brukeren skriver data til dataset'et.  Låsen vil fjernes neste gang brukeren skriver data til dataset'et med `user_lock`, eller dersom låsen slettes. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_dataset_locks_with_http_info(x_client_product_version, dataset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_dataset_locks_with_http_info(x_client_product_version, dataset_id, **kwargs)  # noqa: E501
            return data

    def delete_dataset_locks_with_http_info(self, x_client_product_version, dataset_id, **kwargs):  # noqa: E501
        """Fjerne alle låser brukeren har i et bestemt dataset  # noqa: E501

        Fjerne alle låser brukeren har i et bestemt dataset   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_dataset_locks_with_http_info(x_client_product_version, dataset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_client_product_version: Brukes for å kunne identifisere klienten som er brukt (required)
        :param str dataset_id: UUID of the dataset to get (required)
        :param str locking_type: Angir låsetype som skal brukes (foreløpig er kun `user_lock` støttet). Krever at brukeren har skrivetilgang mot dataset'et.  *user_lock*  Hver bruker har én lås per dataset. Hver gang data hentes ut med `user_lock` legges objektene til denne låsen.  Alle objekter i låsen låses opp neste gang brukeren skriver data til dataset'et.  Låsen vil fjernes neste gang brukeren skriver data til dataset'et med `user_lock`, eller dersom låsen slettes. 
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_client_product_version', 'dataset_id', 'locking_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_dataset_locks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_client_product_version' is set
        if ('x_client_product_version' not in params or
                params['x_client_product_version'] is None):
            raise ValueError("Missing the required parameter `x_client_product_version` when calling `delete_dataset_locks`")  # noqa: E501
        # verify the required parameter 'dataset_id' is set
        if ('dataset_id' not in params or
                params['dataset_id'] is None):
            raise ValueError("Missing the required parameter `dataset_id` when calling `delete_dataset_locks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501

        query_params = []
        if 'locking_type' in params:
            query_params.append(('locking_type', params['locking_type']))  # noqa: E501

        header_params = {}
        if 'x_client_product_version' in params:
            header_params['X-Client-Product-Version'] = params['x_client_product_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasetId}/locks', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dataset_locks(self, x_client_product_version, dataset_id, **kwargs):  # noqa: E501
        """Hent informasjon om brukerens låste features i et bestemt dataset.  # noqa: E501

        Henter bl.a. informasjon om hvilke objekter brukeren har låst i et bestemt dataset.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset_locks(x_client_product_version, dataset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_client_product_version: Brukes for å kunne identifisere klienten som er brukt (required)
        :param str dataset_id: UUID of the dataset to get (required)
        :param str locking_type: Angir låsetype som skal brukes (foreløpig er kun `user_lock` støttet). Krever at brukeren har skrivetilgang mot dataset'et.  *user_lock*  Hver bruker har én lås per dataset. Hver gang data hentes ut med `user_lock` legges objektene til denne låsen.  Alle objekter i låsen låses opp neste gang brukeren skriver data til dataset'et.  Låsen vil fjernes neste gang brukeren skriver data til dataset'et med `user_lock`, eller dersom låsen slettes. 
        :return: Locks
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_dataset_locks_with_http_info(x_client_product_version, dataset_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_dataset_locks_with_http_info(x_client_product_version, dataset_id, **kwargs)  # noqa: E501
            return data

    def get_dataset_locks_with_http_info(self, x_client_product_version, dataset_id, **kwargs):  # noqa: E501
        """Hent informasjon om brukerens låste features i et bestemt dataset.  # noqa: E501

        Henter bl.a. informasjon om hvilke objekter brukeren har låst i et bestemt dataset.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dataset_locks_with_http_info(x_client_product_version, dataset_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_client_product_version: Brukes for å kunne identifisere klienten som er brukt (required)
        :param str dataset_id: UUID of the dataset to get (required)
        :param str locking_type: Angir låsetype som skal brukes (foreløpig er kun `user_lock` støttet). Krever at brukeren har skrivetilgang mot dataset'et.  *user_lock*  Hver bruker har én lås per dataset. Hver gang data hentes ut med `user_lock` legges objektene til denne låsen.  Alle objekter i låsen låses opp neste gang brukeren skriver data til dataset'et.  Låsen vil fjernes neste gang brukeren skriver data til dataset'et med `user_lock`, eller dersom låsen slettes. 
        :return: Locks
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_client_product_version', 'dataset_id', 'locking_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dataset_locks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_client_product_version' is set
        if ('x_client_product_version' not in params or
                params['x_client_product_version'] is None):
            raise ValueError("Missing the required parameter `x_client_product_version` when calling `get_dataset_locks`")  # noqa: E501
        # verify the required parameter 'dataset_id' is set
        if ('dataset_id' not in params or
                params['dataset_id'] is None):
            raise ValueError("Missing the required parameter `dataset_id` when calling `get_dataset_locks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'dataset_id' in params:
            path_params['datasetId'] = params['dataset_id']  # noqa: E501

        query_params = []
        if 'locking_type' in params:
            query_params.append(('locking_type', params['locking_type']))  # noqa: E501

        header_params = {}
        if 'x_client_product_version' in params:
            header_params['X-Client-Product-Version'] = params['x_client_product_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.kartverket.ngis.locks+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/datasets/{datasetId}/locks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Locks',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
