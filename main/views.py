from django.views import View
from django.shortcuts import render


class IndexView(View):
    def get(self, request):
        context = {"user": request.user}
        return render(request, "main/index.html", context)
