from django.urls import path
from .import views

urlpatterns = [path('' ,views.base , name = 'base'),
                path('team/' ,views.team , name = 'team'),
                path('gallery/' ,views.gallery , name = 'gallery'),
                path('rule/' ,views.rule , name = 'rule'),
                path('broucher/' ,views.broucher , name = 'broucher'),
                path('event/' ,views.event , name = 'event'),
                path('spon/' ,views.sponser , name = 'spon'),
                path('circket/',views.circket,name = 'circket'),
]