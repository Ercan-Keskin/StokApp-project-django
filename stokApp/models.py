from django.db import models
from django.contrib.auth.models import User, AbstractUser

 
 
# from django.utils.safestring import mark_safe # bizim içine verdiğimiz stringi güvenli olarak işaretleme

# Create your models here.


# class CustomUser(AbstractUser):
#     image = models.ImageField(null=True,blank=True, default='user.png', upload_to="image/")
    
#     groups = models.ManyToManyField(
#         "auth.Group",
#         verbose_name="groups",
#         blank=True,
#         help_text="The groups this user belongs to.",
#         related_name="custom_user_groups",
#         related_query_name="custom_user_group",
#     )
#     user_permissions = models.ManyToManyField(
#         "auth.Permission",
#         verbose_name="user permissions",
#         blank=True,
#         help_text="Specific permissions for this user.",
#         related_name="custom_user_permissions",
#         related_query_name="custom_user_permission",
#     )

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
    image =  models.ImageField(null=True,blank=True, default='user.png', upload_to="image/")
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
    image =  models.ImageField(null=True,blank=True, default='user.png', upload_to="image/")
    
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
    image =  models.ImageField(null=True,blank=True, default='user.png', upload_to="image/")
    
    def __str__(self):
        return f"{self.quantitiy}-{self.product}-{self.image}"
    
    # class Meta:
    #     verbose_name_plural = ("ALIŞVERİŞ")


  
