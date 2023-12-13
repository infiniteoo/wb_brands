
from django.http import JsonResponse
from backend.models.Colors import Colors
from backend.models.Brand import Brand
from django.views.decorators.csrf import csrf_protect
import json
from django.views.decorators.http import require_http_methods

authentication_classes = [];

# [GET] /api/brand-search
def brand_search(request):
    print (f"request: {request}")
    data = {"message": "This is the brand search API"}
    return JsonResponse(data)


@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def chatbot(request):
    print (f"request: {request}")
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            print(f"request.body: {request.body}")

            # Access specific fields in the JSON data
            """ field_value = data.get('field_name', None) """

            # Your processing logic here...

            # Prepare a response, if needed
            response = JsonResponse({"message": "Received and processed the JSON data"})
            response["Access-Control-Allow-Origin"] = "http://localhost:4200"
            return response
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            response_data = {"error": "Invalid JSON format in the request body"}
            return JsonResponse(response_data, status=400)
    else:
        # Handle other HTTP methods (e.g., GET, PUT, DELETE)
        return JsonResponse({"error": "Unsupported HTTP method"}, status=405)


def brands(request):
    # Fetch all brands
    all_brands = Brand.get_all_brands()

    # Serialize the data into JSON format
    serialized_brands = [
        {
            "name": brand["name"],
            "description": brand["description"],
            "image": brand["image"],
            "founding_year": brand["founding_year"],
            "founder": brand["founder"],
            "history": brand["history"],
            "CEO": brand["CEO"],
            "board_of_directors": brand["board_of_directors"],
            "number_of_employees": brand["number_of_employees"],
            "revenue_information": brand["revenue_information"],
            "location": brand["location"],
            "popular_brands_content": brand["popular_brands_content"]
            

        }
        for brand in all_brands
    ]

    # Create a JSON response
    response_data = {"brands": serialized_brands}

    return JsonResponse(response_data)