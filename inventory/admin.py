from django.contrib import admin

from .models import Medicine, PurchaseInvoice, PurchaseItem, Vendor,Customer,SaleInvoice,SaleItem

admin.site.register(Medicine)
admin.site.register(Vendor)
admin.site.register(Customer)
admin.site.register(PurchaseItem)
admin.site.register(PurchaseInvoice)
admin.site.register(SaleInvoice)
admin.site.register(SaleItem)



