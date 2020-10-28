urlpatterns =[
    path('<int:id>/<slug:slug>/', views.product_detail,
         name='product_detail'),
]
