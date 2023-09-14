from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe # bizim içine verdiğimiz stringi güvenli olarak işaretleme

# Create your models here.
class Firm (models.Model): # FİRMA BİLGİSİ
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    image =  models.ImageField(null=True,blank=True, default='user.png', upload_to="image/")
    
    
    def __str__(self):
        return f"{self.name} -{self.phone}- {self.address} "
    # class Meta:
    #     verbose_name_plural = ("FİRMA")
    
        
class Category(models.Model):

    name = models.CharField(max_length = 35)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     verbose_name_plural = ("KATEGORİ")
        
class Brand(models.Model): # MARKA BİLGİSİ
    name = models.CharField(max_length=25)
    image =  models.ImageField(null=True,blank=True, default='user.png', upload_to="image/")
    
    def __str__(self):
        return self.name
    # class Meta:
    #     verbose_name_plural = ("MARKA")
    @property
    def detay_resim_getir(self):
        if self.image:
            return mark_safe(f"<img src={self.image.url} width=400 height=400></img>")
        return mark_safe(f"<h3>{self.name} adlı yazı resime sahip değil</h3>")
    
class Product(models.Model): #  ÜRÜN BİLGİSİ
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='product_c')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name= 'product_b')  #MARKA
    stock = models.SmallIntegerField(blank=True,null=True,default=0) # STOCK ADETİ
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.name}-{self.category}-{self.stock}"
    
    # class Meta:
    #     verbose_name_plural = ("ÜRÜN")
    
class Sales(models.Model): #SATIŞ BİLGİSİ
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales_p')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,related_name='sales_b') #MARKA BİLGİSİ
    quantitiy = models.SmallIntegerField() # MİKTAR DEMEKTİR
    price = models.DecimalField(max_digits=10, decimal_places= 3)
    price_total = models.DecimalField(max_digits=10, decimal_places=3 ,blank=True)
    
    def __str__(self):
        return f"{self.product}-{self.quantitiy}-{self.price_total}"
    
    # class Meta:
    #     verbose_name_plural = ("SATIŞ")

        
class Purchases (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firm = models.ForeignKey(Firm, on_delete=models.CASCADE, related_name= 'fpurchases')
    brand = models.ForeignKey(Brand , on_delete= models.CASCADE, related_name= 'bpurchases') #MARKA BİLGİSİ
    product = models.ForeignKey(Product , on_delete= models.CASCADE, related_name= 'p_purchases')
    quantitiy = models.SmallIntegerField() # MİKTAR DEMEKTİR
    price = models.DecimalField(max_digits=5 , decimal_places=2) #FİYAT DEMEKTİR
    price_total = models.DecimalField(max_digits=10 , decimal_places=3,blank=True) #TOPLAM FİYAT
    
    def __str__(self):
        return f"{self.quantitiy}-{self.product}"
    
    # class Meta:
    #     verbose_name_plural = ("ALIŞVERİŞ")
    
  