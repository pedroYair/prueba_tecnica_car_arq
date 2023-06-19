from teachers.api.serializers import *
from rest_framework import generics, permissions, status, views
from teachers.models import Teacher
from rest_framework.response import Response


class ListTeachersAPIView(generics.ListAPIView):
    """
       Endpoint to list teachers
    """

    permission_classes = [permissions.IsAuthenticated]
    queryset = Teacher.objects.all().order_by("last_name")

    def get(self, request, *args, **kwargs):
        serializer = TeacherSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class CreateTeacherAPIView(generics.CreateAPIView):
    """
    Endpoint to create a teacher
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TeacherSerializer

    def post(self, request, *args, **kwargs):
        serializer = TeacherSerializer(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        teacher = serializer.save()
        return Response({"Data": "OK", "id": teacher.id})


class UpdateTeacherAPIView(views.APIView):
    """
    Endpoint to update a teacher
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TeacherSerializer

    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Teacher.objects.none()

    def patch(self, request, pk):
        teacher = self.get_object(pk)
        if teacher:
            serializer = TeacherSerializer(teacher, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"Data": "OK", "id": pk})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "No existe un profesor registrado con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)


class DeleteTeacherAPIView(views.APIView):
    """
    Endpoint to delete a teacher
    """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return Teacher.objects.none()

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        if teacher:
            teacher.delete()
            return Response({"Data": "OK"})
        else:
            return Response({"error": "No existe un profesor registrado con este id", "id": pk},
                            status=status.HTTP_400_BAD_REQUEST)


