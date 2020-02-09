from django.http import HttpResponse
class ExcutionFlowMiddleware(object):
    def __init__(self,get_respone):
        self.get_responce = get_respone
    def __call__(self,request):
        # print("Befor pre-proccesing request")
        # respone = self.get_responce(request)
        # print("After post_proceing request")
        # return respone
       #return HttpResponse("('<h1>Currently Application under maintenance...plz try a fter 2 days!!!")
       return self.get_responce(request)
    def procceing_exception(self,request,exception):
        return HttpResponse("<h1>>Currently we are facing some technical problems pl z try after some time!!!<h1>")

