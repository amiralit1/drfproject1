from rest_framework.generics import ListCreateAPIView
from .models import Message
from .serializers import MessageSerializer

# Create your views here.

class MessageListCreateView(ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer