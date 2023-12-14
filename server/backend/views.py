
from django.http import JsonResponse
from backend.models.Colors import Colors
from backend.models.Brand import Brand
from django.views.decorators.csrf import csrf_protect
import json
from django.views.decorators.http import require_http_methods
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


authentication_classes = [];

# [GET] /api/brand-search
def brand_search(request):
    print (f"request: {request}")
    data = {"message": "This is the brand search API"}
    return JsonResponse(data)


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

            
            print('chatbot_response', chat_completion['choices'][0] )
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