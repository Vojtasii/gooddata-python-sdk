# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gooddata_api_client import schemas  # noqa: F401


class PositiveAttributeFilter(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Filter able to limit element values by label and related selected elements.
    """


    class MetaOapg:
        required = {
            "positiveAttributeFilter",
        }
        
        class properties:
            
            
            class positiveAttributeFilter(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    required = {
                        "in",
                        "label",
                    }
                    
                    class properties:
                        applyOnResult = schemas.BoolSchema
                    
                        @staticmethod
                        def _in() -> typing.Type['AttributeFilterElements']:
                            return AttributeFilterElements
                    
                        @staticmethod
                        def label() -> typing.Type['AfmIdentifier']:
                            return AfmIdentifier
                        __annotations__ = {
                            "applyOnResult": applyOnResult,
                            "in": _in,
                            "label": label,
                        }
                
                label: 'AfmIdentifier'
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["applyOnResult"]) -> MetaOapg.properties.applyOnResult: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["in"]) -> 'AttributeFilterElements': ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["label"]) -> 'AfmIdentifier': ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["applyOnResult", "in", "label", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["applyOnResult"]) -> typing.Union[MetaOapg.properties.applyOnResult, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["in"]) -> 'AttributeFilterElements': ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["label"]) -> 'AfmIdentifier': ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["applyOnResult", "in", "label", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    label: 'AfmIdentifier',
                    applyOnResult: typing.Union[MetaOapg.properties.applyOnResult, bool, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'positiveAttributeFilter':
                    return super().__new__(
                        cls,
                        *_args,
                        label=label,
                        applyOnResult=applyOnResult,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "positiveAttributeFilter": positiveAttributeFilter,
            }
    
    positiveAttributeFilter: MetaOapg.properties.positiveAttributeFilter
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["positiveAttributeFilter"]) -> MetaOapg.properties.positiveAttributeFilter: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["positiveAttributeFilter", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["positiveAttributeFilter"]) -> MetaOapg.properties.positiveAttributeFilter: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["positiveAttributeFilter", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        positiveAttributeFilter: typing.Union[MetaOapg.properties.positiveAttributeFilter, dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PositiveAttributeFilter':
        return super().__new__(
            cls,
            *_args,
            positiveAttributeFilter=positiveAttributeFilter,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.afm_identifier import AfmIdentifier
from gooddata_api_client.model.attribute_filter_elements import AttributeFilterElements