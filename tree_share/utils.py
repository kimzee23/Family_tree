from django.shortcuts import get_object_or_404, redirect
from family_tree.models import FamilyTree
from .models import TreeShare
from typing import Optional

def user_can_access_tree(view_func):
    def wrapper(request, tree_id, *args, **kwargs):
        tree = get_object_or_404(FamilyTree, id=tree_id)

        if tree.owner == request.user:
            return view_func(request, tree_id, *args, **kwargs)

        share: Optional[TreeShare] = TreeShare.objects.filter(
            tree=tree, shared_with=request.user
        ).first()

        if share is not None:
            request.access_type = share.access_type
            return view_func(request, tree_id, *args, **kwargs)

        return redirect('access_denied')

    return wrapper
