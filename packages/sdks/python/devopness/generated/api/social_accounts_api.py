"""
Devopness API Python SDK - Painless essential DevOps to everyone

Note:
    This is auto generated by OpenAPI Generator.
    https://openapi-generator.tech
"""

from typing import List, Optional, Union

from .. import DevopnessBaseService, DevopnessBaseServiceAsync, DevopnessResponse
from ..models import (
    SocialAccount,
    SocialAccountCreate,
    SocialAccountCreatePlain,
    SocialAccountRelation,
    SocialAccountStatus,
)
from ..utils import parse_query_string


class SocialAccountsApiService(DevopnessBaseService):
    """
    SocialAccountsApiService - Auto Generated
    """

    def add_social_account(
        self,
        social_account_create: Union[
            SocialAccountCreate,
            SocialAccountCreatePlain,
        ],
    ) -> DevopnessResponse[SocialAccount]:
        """
        Add a social account

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            "/social-accounts",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._post(endpoint, social_account_create)

        return DevopnessResponse(response, SocialAccount)

    def delete_social_account(
        self,
        social_account_id: int,
    ) -> DevopnessResponse[None]:
        """
        Delete a given social account

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/social-accounts/{social_account_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._delete(endpoint)

        return DevopnessResponse(response, None)

    def get_social_account(
        self,
        social_account_provider: str,
    ) -> DevopnessResponse[SocialAccount]:
        """
        Get a social account by provider name

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/social-accounts/{social_account_provider}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._get(endpoint)

        return DevopnessResponse(response, SocialAccount)

    def get_social_account_status(
        self,
        social_account_provider: str,
    ) -> DevopnessResponse[SocialAccountStatus]:
        """
        Get status of a social account

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/social-accounts/{social_account_provider}/status",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._get(endpoint)

        return DevopnessResponse(response, SocialAccountStatus)

    def list_social_accounts(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[SocialAccountRelation]]:
        """
        Return a list of all social accounts of the current user

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = parse_query_string(
            {
                "page": page,
                "per_page": per_page,
            }
        )

        endpoint_parts = [
            "/social-accounts",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = self._get(endpoint)

        return DevopnessResponse(response, List[SocialAccountRelation])


class SocialAccountsApiServiceAsync(DevopnessBaseServiceAsync):
    """
    SocialAccountsApiServiceAsync - Auto Generated
    """

    async def add_social_account(
        self,
        social_account_create: Union[
            SocialAccountCreate,
            SocialAccountCreatePlain,
        ],
    ) -> DevopnessResponse[SocialAccount]:
        """
        Add a social account

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            "/social-accounts",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._post(endpoint, social_account_create)

        return DevopnessResponse(response, SocialAccount)

    async def delete_social_account(
        self,
        social_account_id: int,
    ) -> DevopnessResponse[None]:
        """
        Delete a given social account

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/social-accounts/{social_account_id}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._delete(endpoint)

        return DevopnessResponse(response, None)

    async def get_social_account(
        self,
        social_account_provider: str,
    ) -> DevopnessResponse[SocialAccount]:
        """
        Get a social account by provider name

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/social-accounts/{social_account_provider}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._get(endpoint)

        return DevopnessResponse(response, SocialAccount)

    async def get_social_account_status(
        self,
        social_account_provider: str,
    ) -> DevopnessResponse[SocialAccountStatus]:
        """
        Get status of a social account

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        endpoint_parts = [
            f"/social-accounts/{social_account_provider}/status",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._get(endpoint)

        return DevopnessResponse(response, SocialAccountStatus)

    async def list_social_accounts(
        self,
        page: Optional[int] = None,
        per_page: Optional[int] = None,
    ) -> DevopnessResponse[List[SocialAccountRelation]]:
        """
        Return a list of all social accounts of the current user

        Raises:
            DevopnessApiError: If an API request error occurs.
            DevopnessNetworkError: If a network error occurs.
        """

        query_string = parse_query_string(
            {
                "page": page,
                "per_page": per_page,
            }
        )

        endpoint_parts = [
            "/social-accounts",
            f"?{query_string}",
        ]

        endpoint: str = "".join(endpoint_parts)

        response = await self._get(endpoint)

        return DevopnessResponse(response, List[SocialAccountRelation])
