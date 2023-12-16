
from django.http import JsonResponse
from backend.models.Brand import Brand
import json
from django.views.decorators.http import require_http_methods
from openai import OpenAI
from dotenv import load_dotenv
import os
from django.core.paginator import Paginator, EmptyPage

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


authentication_classes = [];

# [GET] /api/brand-search
def brand_search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        
        if query:
            # Search for brands that match the query
            search_results = Brand.search_brands(query)
            
            # Serialize the data into JSON format
          
            # Create a JSON response
            response_data = {
                "results": search_results,
            }


            
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'No query parameter found'})

    return JsonResponse({'error': 'Invalid request method'})
   


@require_http_methods(['GET', 'POST', 'PUT', 'DELETE'])
def chatbot(request):
   
    if request.method == 'POST':
        try:
            system_content = "You are well knowledged in the company Warner Bros. Discovery (and it's subsidiaries), and are designed to output responses in JSON format.  You are Bugs Bunny.  You will only talk and act like the famous cartoon character Bugs Bunny.  Use lots of silly and fun language, like 'whats up doc?' or 'should have taken a right at Albuquerque'.  Have fun and play the role!  Please don't overuse 'whats up doc'.  you don't need to start every chat reply with it.  switch it up a little."
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            chat_message = data.get('message', None)
            chat_completion = client.chat.completions.create(
                response_format={ "type": "json_object" },
                messages=[
                    {"role": "system", "content": system_content},
                    {
                        "role": "user",
                        "content": chat_message,
                    }
                ],
                model="gpt-3.5-turbo-1106",
            )           
            
            for choice in chat_completion.choices:
                try:
                    content = json.loads(choice.message.content)
                    return JsonResponse(content)
                except json.JSONDecodeError:
                    print(f"Failed to parse JSON content: {choice.message.content}")
                    continue

            
            
            # Extract the chatbot's response from the completion
            chatbot_response = chat_completion['choices']

            # Prepare a JSON response
            response_data = {"message": chatbot_response}

            return JsonResponse(response_data)
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            response_data = {"error": "Invalid JSON format in the request body"}
            return JsonResponse(response_data, status=400)
    else:
        # Handle other HTTP methods (e.g., GET, PUT, DELETE)
        return JsonResponse({"error": "Unsupported HTTP method"}, status=405)



@require_http_methods(['GET'])
def brands(request):
    try:
        # Get parameters from the URL
        page = request.GET.get('page', 1)  # Default page is 1 if not specified
        per_page = request.GET.get('perPage', 15)  # Default per_page is 8 if not specified
        """ print(f'page: {page}, per_page: {per_page}, type: {type(page)}, request: {request}') """
        
        # Convert page and per_page to integers
        try:
            page = int(page)
            per_page = int(per_page)
        except ValueError:
            return JsonResponse({"error": "Invalid page or perPage parameter"}, status=400)

        # Fetch all brands from custom class
        all_brands_data = Brand.get_all_brands(page, per_page)
        """ print('all_brands_data', all_brands_data) """

        # Ensure all_brands_data is a list of dictionaries
        if not isinstance(all_brands_data, list) or not all(isinstance(brand_data, dict) for brand_data in all_brands_data):
            return JsonResponse({"error": "Invalid data format for brands"}, status=500)

        # Create instances of the Brand class from the dictionary data
        all_brands = [
            Brand(
                name=brand_data["name"],
                description=brand_data["description"],
                image=brand_data["image"],
                founding_year=brand_data["founding_year"],
                founder=brand_data["founder"],
                history=brand_data["history"],
                CEO=brand_data["CEO"],
                board_of_directors=brand_data["board_of_directors"],
                number_of_employees=brand_data["number_of_employees"],
                revenue_information=brand_data["revenue_information"],
                location=brand_data["location"],
                popular_brands_content=brand_data["popular_brands_content"],
            )
            for brand_data in all_brands_data
        ]

        """ # Create a Paginator instance
        paginator = Paginator(all_brands, per_page)

        # Ensure that the requested page is within the valid range
        if page < 1 or page > paginator.num_pages:
            return JsonResponse({"error": "Page not found"}, status=404)

        # Get the specified page
        current_page = paginator.page()  # Use the 'page' variable here """


        # Serialize the data into JSON format
        serialized_brands = [
            brand.to_dict()
            for brand in all_brands
        ]

        # Create a JSON response
        response_data = {
            "brands": serialized_brands,
            "total_pages": 1,
            "current_page": page,
        }

        """ print('response_data', response_data) """
        return JsonResponse(response_data)
    except Exception as e:
        # Handle any other unexpected errors
        return JsonResponse({"error": str(e)}, status=500)
