from django.db import models

DOSAGE_FORMS = [
    ("TAB", "Tablet"),
    ("CAP", "Capsule"),
    ("SYR", "Syrup"),
    ("SUPP", "Suppository"),
    ("VIAL", "vial"),
    ("AMP", "Ampoule"),
    ("OTHER", "Other")
]

class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100)
    dosage_form = models.CharField(max_length= 5, choices=DOSAGE_FORMS)
    fractions = models.PositiveIntegerField()
    price = models.DecimalField(max_digits= 6, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.name} - {self.dosage_form}"
    
    
class Vendor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name
    

class PurchaseInvoice(models.Model):
    id = models.AutoField(primary_key=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, related_name= "invoices")
    notes = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"invoice number:{self.id} Purchased from: {self.vendor} At:{self.date}"
    
    
class PurchaseItem(models.Model):
    id = models.AutoField(primary_key=True)
    invoice = models.ForeignKey(PurchaseInvoice, on_delete=models.CASCADE, related_name="items" )
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name="purchases")
    quantity = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
    expiry_date = models.DateField()
    added_on =models.DateTimeField(auto_now_add=True)

    def unit_cost(self):
        return self.medicine.price - ( self.medicine.price * self.discount / 100)

    def __str__(self):
        return f"{self.medicine.name} - {self.quantity} units - Expiry date:{self.expiry_date}"
    
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class SaleInvoice(models.Model):    
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="sales")
    date = models.DateField(auto_now_add=True)
    notes = models.CharField(max_length=200)
    discount = models.PositiveIntegerField()


    def __str__(self):
        return f"Sales invoice No.{self.id} to {self.customer} at {self.date}"
    
class SaleItem(models.Model):
    id = models.AutoField(primary_key=True)
    sale_invoice = models.ForeignKey(SaleInvoice, on_delete=models.CASCADE, related_name="items")
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT, related_name="sales")
    quantity = models.PositiveIntegerField()

    @property
    def total_price(self):
        return self.medicine.price * self.quantity
    