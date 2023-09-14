from django.shortcuts import render

from rest_framework.filters import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend  # altını kızartıyor ama çalışmaya devam ediyor ..


from .models import Category ,Brand ,Firm ,Product , Purchases , Sales

from .serializers import CategorySerializer ,BrandSerializer , FirmSerializer ,ProductSerializer ,CategoryProductSerializer , PurchasesSerializer ,SalesSerializer

from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response

from rest_framework import status

from .permissions import IsStaffOrReadOnly ,IsOwnerOrReadOnlyComment

from .pagination import LargeResultsSetPagination

# Create your views here.
class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # FİLTRELEME ÖZELLİĞİ EKLEDİĞİMİZ ALAN..
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name']
    # SEARCH EKLEDİĞİMİZ ALAN..
    search_fields = ['name']
    pagination_class = LargeResultsSetPagination
    
    permission_classes = [IsStaffOrReadOnly]
    
    def get_serializer_class(self):
        if self.request.query_params.get('name'):
            return CategoryProductSerializer
        return CategorySerializer
    
class BrandView(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['name']
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = LargeResultsSetPagination
    
    
class FirmView(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    search_fields = ['name','phone']
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = LargeResultsSetPagination
    
class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['category', 'name']
    search_fields = ['name']
    permission_classes = [IsStaffOrReadOnly]
    pagination_class = LargeResultsSetPagination
    
    
class PurchasesView(ModelViewSet):
   
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['firm', 'product']
    search_fields = ['firm']
    permission_classes =[IsOwnerOrReadOnlyComment]
    pagination_class = LargeResultsSetPagination
    
    #### YENİ BİR ÜRÜN EKLEDİĞİMİZDE STOCK ATTIRMASI
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #### STOCK EKLEME KISMI ######
        purchase = request.data # istek gelen data 
        product = Product.objects.get(id = purchase['product_id'])
        product.stock += int(purchase['quantitiy'])
        product.save()
        
        
        ######------##########
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        
    ######-UPTADE GÜNCELLEME-########
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object() 
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        #####  KOŞULLARI EKLEME YERİ #####
        
        purchase = request.data  # istek yapılan datayı görme
        product = Product.objects.get(id =instance.product_id)
        product.stock += int(purchase['quantitiy']) - instance.quantitiy
        product.save()
       
        ########################
       
        self.perform_update(serializer)
        

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()   
        
    ###### DELETE  İŞLEMİ  ########
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        ###########  DELETE Stock #########
        
        product = Product.objects.get(id = instance.product_id)  
        product.stock -= instance.quantitiy
        product.save()

        ####################################
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SalesView(ModelViewSet):
    queryset =  Sales.objects.all()
    serializer_class = SalesSerializer
    filter_backends = [SearchFilter, OrderingFilter,DjangoFilterBackend]
    filterset_fields = ['brand', 'product']
    search_fields = ['brand']
    permission_classes = [IsOwnerOrReadOnlyComment]
    pagination_class = LargeResultsSetPagination
    
        #### YENİ BİR ÜRÜN EKLEDİĞİMİZDE STOCK ATTIRMASI
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        #### STOCK EKLEME KISMI ######
        sales = request.data # istek gelen data 
        product = Product.objects.get(id = sales['product_id'])
        if int(sales['quantitiy']) <= product.stock :
            product.stock -= int(sales['quantitiy'])
            product.save()
            
        else : 
            mesaj ={
            "mesaj" : f"YETERİNCE STOK BULUNMADI... -- TOPLAM STOCK {product.stock}"
        }
            return Response(mesaj)
       
       
        ######------##########
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
        
    
    ######-UPTADE GÜNCELLEME-########
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object() 
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        #####  KOŞULLARI EKLEME YERİ #####
        
        sales = request.data  # istek yapılan datayı görme
        product = Product.objects.get(id =instance.product_id)
        if int(sales['quantitiy']) <= instance.quantitiy + product.stock :
            product.stock += instance.quantitiy - int(sales['quantitiy']) 
            product.save()
        else:
          mesaj = {
             "mesaj" :f"ELİMİZDE BU KADAR ÜRÜN BULUNMAMAKTADIR.- KALAN STOCK ADEDİ: {product.stock} "
            }
          return Response(mesaj)
        
    
        self.perform_update(serializer)
        

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()  
        
    
     ###### DELETE  İŞLEMİ  ########
     
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        ###########  DELETE Stock #########
        
        product = Product.objects.get(id = instance.product_id)  
        product.stock += instance.quantitiy
        product.save()
        mesaj = {
             "mesaj" :f"BAŞARILI BİR ŞEKİLDE SİLİNME GERÇEKLEŞTİ... GÜNCEL STOCK : {product.stock} "
            }
        

        ####################################
        self.perform_destroy(instance)
        return Response(mesaj,status=status.HTTP_204_NO_CONTENT) 
        
    
   
        
       