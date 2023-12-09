from django.shortcuts import render
from django.http import JsonResponse
from backend.models.Brand import Brand


# [GET] /api/brand-search
def brand_search(request):
    print (f"request: {request}")
    data = {"message": "This is the brand search API"}
    return JsonResponse(data)

def brands(request):
    # Fetch all brands
    all_brands = Brand.get_all_brands()

    # Serialize the data into JSON format
    serialized_brands = [
        {
            "name": brand["name"],
            "description": brand["description"],
            "image": brand["image"],
        }
        for brand in all_brands
    ]

    # Create a JSON response
    response_data = {"brands": serialized_brands}

    return JsonResponse(response_data)