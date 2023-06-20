from ratings.api.serializers import *
from rest_framework import generics, permissions, status, views
from ratings.models import Rating
from rest_framework.response import Response


class ListRatingsAPIView(generics.ListAPIView):
    """
       Endpoint to list ratings
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Rating.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = RatingSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CreateRatingAPIView(generics.CreateAPIView):
    """
        Endpoint to create ratings
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = RatingCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.save()
        return Response({"Data": "OK", "id": subject.id})


class UpdateRatingAPIView(views.APIView):
    """
        Endpoint to update ratings
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RatingCreateSerializer

    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return Rating.objects.none()

    def patch(self, request, pk):
        rating = self.get_object(pk)
        if rating:
            serializer = RatingCreateSerializer(rating, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Data": "OK", "id": pk})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No existe una calificacion con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)


class DeleteRatingAPIView(views.APIView):
    """
        Endpoint to delete ratings
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Rating.objects.get(pk=pk)
        except Rating.DoesNotExist:
            return Rating.objects.none()

    def delete(self, request, pk):
        rating = self.get_object(pk)
        if rating:
            rating.delete()
            return Response({"Data": "OK"})
        else:
            return Response({"error": "No existe una calificacion registrada con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)
