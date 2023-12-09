from django.shortcuts import render
from openai import OpenAI
from django.http import JsonResponse

client = OpenAI(api_key='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')
# Create your views here.
def chatbot_view(request):
    return render(request, 'chat.html')

# def get_answer(request):
#     user_input = request.GET.get('msg')
#     response = client.chat.completions.create(
#     model="tuned_gpt",
#     messages=[
#     {"role": "system", "content": "You are a knowledgeable assistant specialized in e-commerce and social media marketing. Provide detailed and creative strategies."},
#     {"role": "user", "content": user_input}
#     ]
#     )
#     print(response.choices[0].message)
#     return render(request, 'chat.html', {'user_input': user_input})


def get_answer(request):
   
        if request.method == 'GET':
            user_input = request.GET.get('userInputField', '')
            print(user_input)

            # Use the OpenAI API to get a response based on the user input
            response = client.chat.completions.create(
                model="tuned_gpt",
                messages=[
                    # {"role": "system", "content": "You are a knowledgeable assistant experienced in e-commerce and social media marketing. Provide detailed and creative strategies. answers should not be less than 10 lines."},
                    {"role": "user", "content": user_input}
                ]
            )
            
            # Extract relevant data from the response object
            response_content = response.choices[0].message.content  # Adjust this based on the structure of the ChatCompletion object
            print(response_content)
            
            # Return the response as JSON
            return JsonResponse({'response': response_content})

    