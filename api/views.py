from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from . import extentsions
class API(ViewSet):
    def retrieve(self,request,WordLanguage='eng',word='',MeaningLanguage='eng'):
        meaning=extentsions.meaning(word,WordLanguage,MeaningLanguage)

        return Response(meaning,status=status.HTTP_200_OK
                         ) 
    def create(self,request,WordLanguage='',word='',MeaningLanguage=''):
        return Response({"status":501 , 
                         "response": "under counstruction"},
                         status=status.HTTP_501_NOT_IMPLEMENTED
                         )
    def update(self,request,WordLanguage='',word='',MeaningLanguage=''):
        return Response({"status":501 , 
                         "response": "under counstruction"},
                         status=status.HTTP_501_NOT_IMPLEMENTED
                         )
    def partial_update(self,request,WordLanguage='',word='',MeaningLanguage=''):
        return Response({"status":501 , 
                         "response": "under counstruction"},
                         status=status.HTTP_501_NOT_IMPLEMENTED
                         )
