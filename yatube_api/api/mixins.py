from rest_framework import mixins, viewsets


class CreateGetListViewSet(mixins.CreateModelMixin,
                           mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    pass
