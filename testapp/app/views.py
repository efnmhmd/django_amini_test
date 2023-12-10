from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse,JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.views.generic import TemplateView  # import the TemplateView parent class
from .models import Phone,Person
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework_simplejwt import authentication  as jwt_authentication
from .serializers import *
from rest_framework import generics,permissions,authentication


# Create your views here.
def test(request):
    print(request.method)
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

@csrf_exempt
def test2(request):
    print(request.method)
    if (request.method == "GET"):
        html =''' 
            <!DOCTYPE html>
            <html>
            <body>

            <h2>HTML Forms</h2>

            <form action="/app/test2/" method="POST">
                <label for="fname">First name:</label><br>
                <input type="text" id="fname" name="fname" value="John"><br>
                <label for="lname">Last name:</label><br>
                <input type="text" id="lname" name="lname" value="Doe"><br><br>
                <input type="submit" value="Submit">
            </form> 

            <p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

            </body>
            </html>
        '''
        return HttpResponse(html)
    elif(request.method =="POST"):
        fname = request.POST["fname"] +" " + request.POST["lname"]
        return HttpResponse("<h1>hello " +fname +"</h1>")

@csrf_exempt
def test3(request,adad):
    print(request.method)
    print(request.GET.get("x",None))
    print("addad " ,adad)
    if (request.method == "GET"):
        context = {}
        context["name"] ="erfan"
        return render(request,"app/base.html",context=context)
    
    elif(request.method =="POST"):
        fname = request.POST["fname"] +" " + request.POST["lname"]
        context = {"fname":fname,"xxx":2,"jj":range(5)}
        return render(request,"app/resp.html",context=context)


class Test4 (View):

    def get(self,request):
        context = {}
        context["name"] ="erfan"
        return render(request,"app/base.html",context=context)
    
    def post(self,request):
        fname = request.POST["fname"]
        lname =  request.POST["lname"]
        phone = request.POST["phone"]
        context= {}
        #ravesh aval
        # p = Phone()
        # p.lname = lname
        # p.fname = fname
        # p.phone = phone 
        # p.save()
        p = Phone(lname=lname , fname=fname , phone=phone)
        p.save()
        ff = Phone.objects.all()
        # context = {"phone_list":ff}
        context["phone_list"] = ff
        return render(request,"app/resp.html",context=context)               
    
class Test5(TemplateView):
    template_name= "app/base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "radmehr"
        return context

class Test6(View):
    def get(self,request):
        search = request.GET.get('search')
        
        list_of_numbers = Person.objects.filter(lname=search)
        person_list = []
        for p in list_of_numbers:
            phones = p.phones.all()
            phone_list = []
            for pp in phones :
                phone_list.append(pp.phone)
            person_list.append(
            {
               "lname" :p.lname,
               "fname":p.fname,
               "phone_list":phone_list
            } )
        print(list_of_numbers)
        context = {"list_of_numbers":person_list}
        return JsonResponse(context)
    


class Test7(View):
    def get(self,request):
        search = request.GET.get('search')
        list_of_numbers = Person.objects.filter(Q(lname=search) | Q(fname=search) ,active=True)
        person_list = []
        for p in list_of_numbers:
            phones = p.phones.all()
            phones = Phone.objects.filter(person=p)
            phone_list = []
            for pp in phones :
                phone_list.append(pp.phone)
            person_list.append(
            {
               "lname" :p.lname,
               "fname":p.fname,
               "phone_list":phone_list
            } )
        print(list_of_numbers)
        context = {"list_of_numbers":person_list}
        return JsonResponse(context)
    
class Test8(View):
    def get(self,request):
        lname = request.GET.get('search')
        
        list_of_numbers = Phone.objects.filter(person__lname=lname )
        print(list_of_numbers.query)
        person_list = []
        for p in list_of_numbers:
            person_list.append(
            {
               "phone_number" :p.phone,
               "lname":p.person.lname,
               "fname":p.person.fname
            } )
        print(list_of_numbers)
        context = {"list_of_numbers":person_list}
        return JsonResponse(context)
    
class APITest1(APIView):
    def get(self,request):
        return Response({'status':"ok"})
    
class APITest2(APIView):
    def get(self,request):
        lname = request.GET.get('search')
        
        list_of_numbers = Phone.objects.filter(person__lname=lname )
        print(list_of_numbers.query)
        person_list = []
        for p in list_of_numbers:
            person_list.append(
            {
               "phone_number" :p.phone,
               "lname":p.person.lname,
               "fname":p.person.fname
            } )
        print(list_of_numbers)
        context = {"list_of_numbers":person_list}
        return Response(context)
    
class APITest3(APIView):
    def get(self,request):
        lname = request.GET.get('search')
        
        persons = Person.objects.filter(lname=lname )
        sr = PersonSerializer(persons,many=True)       
        return Response(sr.data)
    def post(self,request):
        data = request.data
        print(data)
        sr = PersonSerializer(data=data)  
        sr.is_valid(raise_exception=True)
        print(sr.data)
        p = Person(**sr.validated_data)
        p.save()
        return Response(sr.data)
    

class APITest4(APIView):
    def get(self,request):
        lname = request.GET.get('search')
        persons = Person.objects.filter(lname=lname )
        sr = PersonModelSerializer(persons,many=True)       
        return Response(sr.data)
    def post(self,request):
        data = request.data
        sr = PersonModelSerializer(data=data)  
        sr.is_valid(raise_exception=True)
        sr.save()
        return Response(sr.data)

class APITest5(APIView):
    def post(self,request,pk):
        data = request.data
        p= Person.objects.get(id=pk)
        sr = PersonModelSerializer(p,data=data)  
        sr.is_valid(raise_exception=True)
        sr.save()
        return Response(sr.data) 
    

class APITest6(generics.ListCreateAPIView):
    queryset = Person.objects.filter(active=True)
    serializer_class = PersonModelSerializer
    # def get_queryset(self):
    #     return Person.objects.filter(fname="mohamadi")
    #     # return super().get_queryset()
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    # permission_classes = [Is]

class APITest7(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [jwt_authentication.JWTAuthentication]
    # permission_classes = [permissions.AllowAny]

    queryset = Person.objects.all()
    serializer_class = PersonModelSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)