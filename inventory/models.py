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

class Stock(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, related_name="stocks")
    quantity = models.PositiveBigIntegerField()
    expiry_date = models.DateField()
    added_on =models.DateTimeField(auto_now_add=True)


