from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Instrument
from .serializers import InstrumentSerializer
# PopulatedTeacherSerialiser
from rest_framework.exceptions import NotFound



class InstrumentListView(APIView):

    def get(self, _request):
        instruments = Instrument.objects.all()
        serlialized_instruments = InstrumentSerializer(instruments,many=True)
        return Response(serlialized_instruments.data, status=status.HTTP_200_OK)

class InstrumentDetailView(APIView):

    def get(self, _request,pk):
        try:
            instrument = Instrument.objects.get(pk=pk)
            serlialized_instrument = InstrumentSerializer(instrument)
            return Response(serlialized_instrument.data, status=status.HTTP_200_OK)
        except Instrument.DoesNotExist:
            raise NotFound()
