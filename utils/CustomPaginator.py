from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.query import QuerySet
from django.core.paginator import Page


class PagePaginator:
    def __init__(self, queryset: QuerySet, pages: int):
        self.pages = pages
        self.paginator = Paginator(queryset, self.pages)

    def __len__(self) -> int:
        return self.paginator.num_pages

    def page_obj(self, page_number: int) -> Page:
        try:
            page_obj = self.paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = self.paginator.page(1)
        except EmptyPage:
            page_obj = self.paginator.page(len(self))
        return page_obj

    def is_paginate(self) -> bool:
        if len(self) > 1:
            return True
        return False

