from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        return Response(
            {
                "page_metadata": {
                    "total_pages": self.page.paginator.num_pages,
                    "count": self.page.paginator.count,
                    "page_size": self.get_page_size(self.request),
                },
                "results": data,
            }
        )
