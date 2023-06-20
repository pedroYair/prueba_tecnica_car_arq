from students.api.serializers import *
from rest_framework import generics, permissions, status, views
from students.models import Student
from rest_framework.response import Response


class ListStudentsAPIView(generics.ListAPIView):
    """
       Endpoint to list students
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Student.objects.all().order_by("last_name")

    def get(self, request, *args, **kwargs):
        serializer = StudentSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CreateStudentAPIView(generics.CreateAPIView):
    """
        Endpoint to create students
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentSerializer

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        student = serializer.save()
        return Response({"Data": "OK", "id": student.id})


class UpdateStudentAPIView(views.APIView):
    """
        Endpoint to update students
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StudentSerializer

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Student.objects.none()

    def patch(self, request, pk):
        student = self.get_object(pk)
        if student:
            serializer = StudentSerializer(student, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Data": "OK", "id": pk})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No existe un estudiante registrado con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)


class DeleteStudentAPIView(views.APIView):
    """
        Endpoint to delete students
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Student.objects.none()

    def delete(self, request, pk):
        student = self.get_object(pk)
        if student:
            student.delete()
            return Response({"Data": "OK"})
        else:
            return Response({"error": "No existe un estudiante registrado con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)
