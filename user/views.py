from django.shortcuts import render
from django.views import View
            
class UserDashbord(View):            
    def get(self, request):
        return render(request, "user/pages/dashbord.html")
        
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
