from django.shortcuts import render, redirect, get_object_or_404
from member.forms import MemberForm
from family_tree.models import FamilyTree
from member.services import add_member_to_family

def register_member(request, tree_id):
    tree = get_object_or_404(FamilyTree, id=tree_id)
    root_family = tree.root_family

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            add_member_to_family(
                family=root_family,
                name=data['name'],
                birth_date=data['birth_date'],
                death_date=data.get('death_date'),
                relation=data.get('relation', ''),
                photo=request.FILES.get('photo'),
                marital_status=data.get('marital_status', 'single'),
                spouse=data.get('spouse'),
                parent=data.get('parent')
            )
            return redirect('view_family_tree', tree_id=tree.id)
    else:
        form = MemberForm()

    return render(request, 'member/register.html', {'form': form, 'tree': tree})
