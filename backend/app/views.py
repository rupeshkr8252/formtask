from rest_framework import viewsets
from rest_framework.response import Response
from .models import Form
from .serializers import FormSerializer
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
class FormModelViewset(viewsets.ModelViewSet):
    queryset = Form.objects.all()
    serializer_class = FormSerializer


@api_view(["GET"])
def user_status(request, UserId):

    try:
        get_user = Form.objects.get(id=UserId)
    except Form.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = {
        "name": get_user.name,
        "sex": get_user.sex,
        "mobile": get_user.mobile,
        'address': get_user.address,
        'id_num': get_user.id_num,
        'guardian_name': get_user.guardian_name,
        'nationality': get_user.nationality

    }
    return Response(data)
