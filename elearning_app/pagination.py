from rest_framework.pagination import PageNumberPagination

class CoursePagination(PageNumberPagination):
    page_size=10
    page_size_query_param = 'records'
    max_page_size=20
    last_page_strings='last'