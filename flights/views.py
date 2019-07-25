from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer, RegisterSerializer, AdminSerializer, UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser


class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer
	permission_classes = [AllowAny]


class BookingsList(ListAPIView):
	# queryset = Booking.objects.filter(date__gte=datetime.today(), user=request.user)
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated]

	def get_queryset(self):
	 	self.serializer_class
	 	return Booking.objects.filter(date__gte=datetime.today(), user=self.request.user)

class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateBookingSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

	def Admin(RetrieveUpdateAPIView):
		serializer_class = AdminSerializer
		if self.request.user.is_staff:
			serializer_class = AdminSerializer
		else:
			serializer_class = UserSerializer
		return serializer_class


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'
	permission_classes = [IsAuthenticated, IsAdminUser]


class BookFlight(CreateAPIView):
	serializer_class = UpdateBookingSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, flight_id=self.kwargs['flight_id'])


class Register(CreateAPIView):
	serializer_class = RegisterSerializer


