from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Instagram
from .forms import InstagramForm


def create(request):
    akun_form = InstagramForm(request.POST or None)

    if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()
            messages.success(request, '🎉 Akun berhasil ditambahkan')
            return redirect('sosmed:list')

    context = {
        "page_title": "Tambah Akun",
        "akun_form": akun_form,
    }

    return render(request, 'sosmed/create.html', context)


def list_instagram(request):
    keyword = request.GET.get('q')
    platform = request.GET.get('platform', 'instagram')

    semua_akun = Instagram.objects.filter(platform=platform)

    if keyword:
        semua_akun = semua_akun.filter(username__icontains=keyword)

    context = {
        'page_title': 'Sosial Media',
        'semua_akun': semua_akun,
        'keyword': keyword,
        'platform': platform,
    }

    return render(request, 'sosmed/list.html', context)


def update(request, update_id):
    akun_update = Instagram.objects.get(id=update_id)

    akun_form = InstagramForm(
        request.POST or None,
        instance=akun_update
    )

    if request.method == 'POST':
        if akun_form.is_valid():
            akun_form.save()
            messages.success(request, '✏️ Data berhasil diupdate')
            return redirect('sosmed:list')

    context = {
        "page_title": "Update Akun",
        "akun_form": akun_form,
    }

    return render(request, 'sosmed/create.html', context)


def delete(request, delete_id):
    Instagram.objects.filter(id=delete_id).delete()
    messages.error(request, '🗑️ Data berhasil dihapus')
    return redirect('sosmed:list')