from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import UserSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer

# Get the User model (default or custom)
User = get_user_model()

# ---------------- User Registration ----------------
class UserRegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

# ---------------- Patients ----------------
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()  # Required by DRF router
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return patients created by logged-in user only
        return Patient.objects.filter(created_by=self.request.user)

    def perform_create(self, serializer):
        # Set created_by field to logged-in user
        serializer.save(created_by=self.request.user)

# ---------------- Doctors ----------------
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()  # Required by DRF router
    serializer_class = DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]

# ---------------- Patient-Doctor Mappings ----------------
class MappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()  # Required by DRF router
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def patient_doctors(self, request, pk=None):
        mappings = self.queryset.filter(patient_id=pk)
        serializer = self.get_serializer(mappings, many=True)
        return Response(serializer.data)
