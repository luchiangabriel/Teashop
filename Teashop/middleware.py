
from distributors.models import Logs_Distributors
from ingredients.models import Logs_Ingredients
from recipes.models import Logs_Recipes


class RefreshMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print(request.method)
            if request.method == 'GET':
                Logs_Distributors.objects.create(user_id=request.user.id, action='refresh', url=request.path) \
                    and Logs_Ingredients.objects.create(user_id=request.user.id, action='refresh', url=request.path) \
                    and Logs_Recipes.objects.create(user_id=request.user.id, action='refresh', url=request.path)
            elif request.method == 'POST':
                action = 'created'
                for item in str(request.path):
                    if item.isdigit():
                        action = 'updated'
                        break
                Logs_Distributors.objects.create(user_id=request.user.id, action=action, url=request.path) \
                    and Logs_Ingredients.objects.create(user_id=request.user.id, action=action, url=request.path) \
                    and Logs_Recipes.objects.create(user_id=request.user.id, action=action, url=request.path)
        response = self.get_response(request)
        return response
