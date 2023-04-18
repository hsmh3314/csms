from django import forms
from csms.models import Customer, Service

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['ccode', 'cname', 'birth', 'phoneNum', 'address', 'imgfile']

        labels = {
            'ccode': '고객 코드',
            'cname': '고객명',
            'birth': '생년월일',
            'phoneNum': '전화번호',
            'address': '주소',
            'imgfile': '사진',
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['ccode', 'cname', 'sDate', 'departure', 'arrival', 'fee', 'type']

        labels = {
            'ccode': '고객 코드',
            'cname': '고객명',
            'sDate': '일시',
            'departure': '출발지',
            'arrival': '도착지',
            'fee': '요금',
            'type': '유형',
        }