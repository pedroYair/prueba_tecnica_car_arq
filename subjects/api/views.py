from subjects.api.serializers import *
from rest_framework import generics, permissions, status, views
from subjects.models import Subject
from rest_framework.response import Response


class ListSubjectsAPIView(generics.ListAPIView):
    """
       Endpoint to list subjects
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Subject.objects.all().order_by("code")

    def get(self, request, *args, **kwargs):
        serializer = SubjectSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CreateSubjectAPIView(generics.CreateAPIView):
    """
        Endpoint to create subjects
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubjectCreateSerializer

    def post(self, request, *args, **kwargs):
        serializer = SubjectCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.save()
        return Response({"Data": "OK", "id": subject.id})


class UpdateSubjectAPIView(views.APIView):
    """
        Endpoint to update subjects
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SubjectCreateSerializer

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Subject.objects.none()

    def patch(self, request, pk):
        subject = self.get_object(pk)
        if subject:
            serializer = SubjectCreateSerializer(subject, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Data": "OK", "id": pk})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No existe un curso registrado con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)


class DeleteSubjectAPIView(views.APIView):
    """
        Endpoint to delete subjects
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return Subject.objects.none()

    def delete(self, request, pk):
        subject = self.get_object(pk)
        if subject:
            subject.delete()
            return Response({"Data": "OK"})
        else:
            return Response({"error": "No existe un curso registrado con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)
