from datetime import datetime
from functools import reduce

from rest_framework import viewsets, serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ProductModel, ProductChangesModel
from .serlializers import ProductSerializer, ProductShowListSerializer, ProductChangesSerializer, \
    ProductPriceSerializer, ProductHistorySerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'All_Products': 'all/',
        'Add': 'add-product/',
        'Product_History_Of_Changes': 'product-changes/pk/',
        'Update': 'update-product/pk/',
        'Delete': 'delete-product/pk/',
        'Price': 'edit-product-price/pk/',
        'Calculate_Price': 'calculate-product-prices/pk/',
    }

    return Response(api_urls)


@api_view(['POST'])
def add_items(request):
    """
    :param request:
    :return Response(product.data):
    """
    product = ProductSerializer(data=request.data)

    if ProductModel.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if product.is_valid():
        product.save()
        return Response(product.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_products(request):

    if request.query_params:
        products = ProductModel.objects.filter(**request.query_param.dict())
    else:
        products = ProductModel.objects.all()

    if products:
        data = ProductShowListSerializer(products, many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def edit_products(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product_serializer = ProductSerializer(instance=product, data=request.data)

    if product_serializer.is_valid():
        ProductChangesModel.objects.create(
            product=product,
            name_was=product.name,
            name_new=product_serializer.validated_data.get('name'),
            description_was=product.description,
            description_new=product_serializer.validated_data.get('description'),
            start_date_was=product.start_date,
            start_date_new=product.start_date,
            end_date_was=product.end_date,
            end_date_new=product.end_date,
            price_was=product.price,
            price_new=product.price,
        )
        product_serializer.save()

        return Response(product_serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def edit_products_price(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product_serializer = ProductPriceSerializer(instance=product, data=request.data)

    if product_serializer.is_valid():
        ProductChangesModel.objects.create(
            product=product,
            name_was=product.name,
            name_new=product.name,
            description_was=product.description,
            description_new=product.description,
            start_date_was=product.start_date,
            start_date_new=product_serializer.validated_data.get('start_date'),
            end_date_was=product.end_date,
            end_date_new=product_serializer.validated_data.get('end_date'),
            price_was=product.price,
            price_new=product_serializer.validated_data.get('price'),
        )
        product_serializer.save()
        return Response(product_serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['DELETE'])
def delete_product(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product_history = ProductChangesModel.objects.filter(product=product)
    product_history.delete()
    product.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['POST'])
def calculate_product_prices(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product_changes_history = ProductChangesModel.objects.filter(product=product)

    price_history = []
    i = 1
    for pr_history in product_changes_history:
        if not (pr_history.start_date_new is None or pr_history.end_date_new is None):
            if pr_history.start_date_new <= datetime.strptime(request.data['start_date'], '%Y-%m-%d').date() and pr_history.end_date_new >= datetime.strptime(request.data['end_date'], '%Y-%m-%d').date():
                price_history.append(pr_history.price_new)
                if i == 1:
                    price_history.append(pr_history.price_was)
                i += 1

    if not price_history:
        return Response(
            {
                'detail': f'Product with {product.id} ID does not have ProductHistoryChanges'
            },
            status=status.HTTP_404_NOT_FOUND)

    average_price = round(float(reduce((lambda x, y: x + y), price_history))/len(price_history), 2)
    return Response({'average_price': average_price}, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def product_changes(request, pk):
    product = get_object_or_404(ProductModel, pk=pk)
    product_changes_history = ProductChangesModel.objects.filter(product=product)

    data = ProductHistorySerializer(product_changes_history, many=True)
    return Response(data.data)
