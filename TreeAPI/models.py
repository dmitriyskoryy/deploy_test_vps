from django.db import models
from treebeard.mp_tree import MP_Node


class Node(MP_Node):
    item_type_choices = (
        ('company', 'Company'),
        ('department', 'Department'),
        ('employee', 'Employee')
    )

    item_type = models.CharField(max_length=100, choices=item_type_choices)
    attributes = models.JSONField(null=True, blank=True)

    node_order_by = ['item_type']

    def __str__(self):
        return f"{self.item_type}"
