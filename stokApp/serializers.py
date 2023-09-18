from rest_framework import serializers

from .models import Firm, Category , Brand , Product , Sales ,Purchases

class CategorySerializer(serializers.ModelSerializer):
    category_count = serializers.SerializerMethodField()
    class Meta :
        model = Category
        fields = ['id','name','category_count']
    # Bir Kategorideki toplam ürün sayısını hesaplar...   
    def get_category_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count()
    
class ProductSerializer(serializers.ModelSerializer):

    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'category_id', 'brand', 'brand_id', 'stock', 'updated', 'created']
        read_only_fields = ['stock']
        
# Category’e giriş noktasındaki name filtresini kullanarak arama yaparken Category’e ait ürün(products)ayrıntılarını görüntülemek için yeni bir serializer oluşturulmalı      
class CategoryProductSerializer (serializers.ModelSerializer):
    product_c = ProductSerializer (many = True)
    category_count = serializers.SerializerMethodField()
    class Meta :
        model = Category
        fields = ['id','name','category_count','product_c']
        
    def get_category_count(self, obj):
        return Product.objects.filter(category_id = obj.id).count()
    


class BrandSerializer(serializers.ModelSerializer):
    
    class Meta :
        model = Brand
        fields = ['id','name','image',]
       

class FirmSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = Firm
        fields = ['id', 'name', 'phone', 'image', 'address', ]
         
        
        def get_category_count(self, obj):
         return Firm.objects.filter(image_id = obj.id).count()
         
        
class PurchasesSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(read_only = True)
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    # price_total = serializers.SerializerMethodField()
    
    category = serializers.SerializerMethodField()
    class Meta:
        model = Purchases
        fields = ['id','user','user_id','firm','firm_id','brand','brand_id','product','product_id','quantitiy', 'price', 'price_total','category','image',]    
        
    def create(self,validate_date):
        validate_date['user_id']= self.context['request'].user.id  ### YENİ BİR ALIŞ YAPILDIĞINDA USER ID Yİ OTOMATİK ALMAK İÇİN YAZMAK ZORUNDAYIZ..
        instance = Purchases.objects.create(**validate_date)
        return instance
        
    def get_category(self,obj):
        return obj.product.category.name
    
    # def get_price_total(self, obj):
    #     return obj.price * obj.quantitiy
    
class SalesSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField() 
    user_id = serializers.IntegerField(read_only = True)
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand_id = serializers.IntegerField()
    
    class Meta : 
        model = Sales
        fields = ['id','user','user_id','brand','brand_id','product','product_id','quantitiy','price','price_total', 'image',]
    
    def create(self,validate_date):
        validate_date['user_id']= self.context['request'].user.id    ### YENİ BİR SATIŞ YAPILDIĞINDA USER ID Yİ OTOMATİK ALMAK İÇİN YAZMAK ZORUNDAYIZ..
        instance = Sales.objects.create(**validate_date)
        return instance    
