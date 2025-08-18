from django.shortcuts import render, redirect

from tree_share.forms import TreeShareForm


def share_tree(request):
    if request.method == 'POST':
        form = TreeShareForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tree_list')
        else:
            form = TreeShareForm()
        return render(request,'tree_share/share.html', {'form':form})