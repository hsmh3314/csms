from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Service
from .forms import CustomerForm, ServiceForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q


def index(request):
    """
    csms 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '') # 검색어

    # 조회
    customer_list = Customer.objects.order_by('ccode')
    if kw:
        customer_list = customer_list.filter(
            Q(ccode__icontains=kw) |
            Q(cname__icontains=kw) |
            Q(birth__icontains=kw) |
            Q(phoneNum__icontains=kw) |
            Q(address__icontains=kw)
        ).distinct()

    # 페이징 처리
    paginator = Paginator(customer_list, 10)
    page_obj = paginator.get_page(page)

    context = {'customer_list': page_obj, 'page':page, 'kw':kw}
    return render(request, 'csms/customer_list.html', context)

def service_index(request):
    """
    csms 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '') # 검색어

    # 조회
    service_list = Service.objects.order_by('sDate')
    if kw:
        service_list = service_list.filter(
            Q(ccode__icontains=kw) |
            Q(cname__icontains=kw) |
            Q(departure__icontains=kw) |
            Q(arrival__icontains=kw)
        ).distinct()

    # 페이징 처리
    paginator = Paginator(service_list, 10)
    page_obj = paginator.get_page(page)

    context = {'service_list': page_obj, 'page':page, 'kw':kw}
    return render(request, 'csms/service_list.html', context)

def service_detail(request, service_sNo):
    """
    csms 내용 출력
    """
    service = get_object_or_404(Service, pk = service_sNo)
    context = {'service': service}
    return render(request, 'csms/service_detail.html', context)

@login_required(login_url='common:login')
def service_create(request):
    """
    csms 등록
    """

    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.author = request.user
            cus = Customer.objects.get(ccode = service.ccode)
            service.customer_id = cus.id
            service.save()
            return redirect('csms:service_index')
    else:
        form = ServiceForm()
    context = {'form': form}
    return render(request, 'csms/service_form.html', context)

def customer_detail(request, customer_id):
    """
    csms 내용 출력
    """
    customer = get_object_or_404(Customer, pk = customer_id)
    context = {'customer': customer}
    return render(request, 'csms/customer_detail.html', context)

@login_required(login_url='common:login')
def customer_create(request):
    """
    csms 고객 등록
    """
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.author = request.user
            customer.save()
            return redirect('csms:index')
    else:
        form = CustomerForm()
    context = {'form': form}
    return render(request, 'csms/customer_form.html', context)

@login_required(login_url='common:login')
def customer_modify(request, customer_id):
    """
    csms 고객 수정
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.user != customer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('csms:customer_detail', customer_id=customer.id)

    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.author = request.user
            customer.save()
            return redirect('csms:customer_detail', customer_id=customer.id)
    else:
        form = CustomerForm(instance=customer)
    context = {'form': form}
    return render(request, 'csms/customer_form.html', context)

@login_required(login_url='common:login')
def customer_delete(request, customer_id):
    """
    csms 고객 삭제
    """
    customer = get_object_or_404(Customer, pk=customer_id)
    if request.user != customer.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('csms:customer_detail', customer_id=customer.id)
    customer.delete()
    return redirect('csms:index')

















