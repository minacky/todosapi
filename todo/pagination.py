from rest_framework import pagination


class CustomNumberPagination(pagination.PageNumberPagination):
    page_size =3
    page_size_query_param='count'
    max_page_size=5
    page_query_param='p'