from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import MethodNotAllowed
from django.shortcuts import get_object_or_404

from .models import Node

from .serializers import *


from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404





class NodeViewSet(viewsets.ModelViewSet):
    serializer_class = NodeSerializer
    queryset = Node.objects.all()

    @action(methods=['get'], detail=False)
    def get_tree(self, request):
        tree = Node.get_tree(request.query_params.get('item'))
        serializer = NodeSerializer(tree, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=True)
    def get_descendants(self, request, pk=None):
        node = get_object_or_404(Node, id=pk)
        descendants = node.get_descendants()
        serializer = NodeSerializer(descendants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False)
    def add_root(self, request):
        data = request.data
        serializer = NewRootNodeSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        project_id = serializer.validated_data['project_id']
        item_type = serializer.validated_data['item_type']
        item = serializer.validated_data['item']
        inner_order = serializer.validated_data.get('inner_order', 1)
        attributes = serializer.validated_data.get('attributes')

        root = Node.add_root(
            project_id=project_id,
            item_type=item_type,
            item=item,
            inner_order=inner_order,
            attributes=attributes
        )
        root_data = self.get_serializer(root).data
        return Response(root_data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=True)
    def add_child(self, request, pk=None):
        parent = self.get_object()
        data = request.data

        serializer = NewRootNodeSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        project_id = serializer.validated_data['project_id']
        item_type = serializer.validated_data['item_type']
        item = serializer.validated_data['item']
        inner_order = serializer.validated_data.get('inner_order', 1)
        attributes = serializer.validated_data.get('attributes')

        try:
            child = parent.add_child(
                project_id=project_id,
                item_type=item_type,
                item=item,
                inner_order=inner_order,
                attributes=attributes
            )
        except ValueError as e:
            return Response({"detail": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)

        child_data = self.get_serializer(child).data
        return Response(child_data, status=status.HTTP_201_CREATED)


#
#
# class NodeViewSet(viewsets.ModelViewSet):
#     serializer_class = NodeSerializer
#     queryset = Node.objects.all()
#
#     def create(self, request, *args, **kwargs):
#         raise MethodNotAllowed('POST')
#
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = NewNodeSerializer(instance, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(NodeSerializer(instance).data)
#
#     @action(detail=False, methods=['get'])
#     def get_roots(self, request):
#         roots = Node.get_root_nodes()
#         serializer = NodeSerializer(roots, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @action(detail=True, methods=['get'])
#     def get_descendants(self, request, pk=None):
#         root = get_object_or_404(Node, pk=pk)
#         descendants = root.get_descendants()
#         serializer = NodeSerializer(descendants, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @action(detail=True, methods=['get'])
#     def get_children(self, request, pk=None):
#         node = get_object_or_404(Node, pk=pk)
#         children = node.get_children()
#         serializer = NodeSerializer(children, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     @action(detail=False, methods=['post'])
#     def add_root(self, request):
#         data = request.data
#         serializer = NewNodeSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         item_type = serializer.validated_data['item_type']
#         attributes = serializer.validated_data.get('attributes')
#         root = Node.add_root(item_type=item_type, attributes=attributes)
#         root_data = self.get_serializer(root).data
#         return Response(root_data, status=status.HTTP_201_CREATED)
#
#     @action(detail=True, methods=['post'])
#     def add_child(self, request, pk=None):
#         parent = self.get_object()
#         data = request.data
#         serializer = NewNodeSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         item_type = serializer.validated_data['item_type']
#         attributes = serializer.validated_data.get('attributes')
#         child = parent.add_child(item_type=item_type, attributes=attributes)
#         child_data = self.get_serializer(child).data
#         return Response(child_data, status=status.HTTP_201_CREATED)
#
#     @action(detail=True, methods=['put'])
#     def change_parent(self, request, pk=None):
#         node = self.get_object()
#         new_parent_id = request.data.get('new_parent_id')
#         if not new_parent_id or type(new_parent_id) is not int:
#             return Response({"detail": "new_parent_id has to be provided and has to be an existing node id"},
#                             status=status.HTTP_400_BAD_REQUEST)
#         new_parent = get_object_or_404(Node, id=new_parent_id)
#         node.move(new_parent, pos='sorted-child')  # or 'last-child' or 'first-child'
#         return Response(self.get_serializer(node).data, status=status.HTTP_200_OK)
