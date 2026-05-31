# class OrderSerializer(serializer.modelSerializer):
#     class Meta:
#         model = Order
#         fields = "__all__"

# class AuditLog(models.Model):
#     actiontypes = (order_created
# driver_assigned
# accepted
# picked_up
# in_transit
# delivered
# cancelled)
#     User = models.Foreignkey(User,on_delete = Cascade,)
#     order = models.Foreignkey(Order, on_delete = cascade)
#     Actiontype =models.characterfield(max_lenght = 50,choices = actiontypes)
#     description = models.textfield(max_lenght = 500)
#     created_at = models.datetimefield(auto_now_add = True)

#     def __str__(self):
#         return "Logged"

# class Iscustomer(basepermission):
#     message = "only customers can perfrom this action"

#     def has_permission(self,request,view):
#         if not request.user or not request.user.is_aunthenticated:
#             return False
#         profile = getattr(request.user, 'userprofile',None)
#         return profile if not None and profile.role = customer

# class AssignDriverAPIView(APIView):
#     permission_classes = [IsAdmin]

#     def post(self, request):
#         serializer = AssignDriverSerializer(data=request.data)

#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#         data = serializer.validated_data

#         try:
#             assignment = assign_driver(
#                 order_id=data["order_id"],
#                 driver_id=data["driver_id"],
#                 admin_user=request.user
#             )
#             return Response({
#                 "message": "Driver assigned successfully",
#                 "assignment_id": assignment.id,
#                 "order_id": assignment.order.id,
#                 "driver": assignment.driver.name
#             }, status=status.HTTP_201_CREATED)

#         except ValueError as e:
#             return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)      
# 
# def update_delivery_status(order_id, new_status, driver_user):

#     with transaction.atomic():

#         order = Order.objects.select_for_update().get(id=order_id)

#         try:
#             driver = Driver.objects.get(user=driver_user)
#         except Driver.DoesNotExist:
#             raise ValueError("No driver profile is linked to your account")

#         active_assignment = order.assignments.filter(driver=driver).exclude(status="completed").first()
#         if not active_assignment:
#             raise ValueError("You are not assigned to this order")

#         expected_next = VALID_TRANSITIONS.get(order.status)
#         if expected_next != new_status:
#             raise ValueError(
#                 f"Invalid transition: '{order.status}' → '{new_status}'. "
#                 f"Expected next status: '{expected_next}'"
#             )

#         old_status = order.status
#         order.status = new_status
#         order.save()

#         if new_status == "delivered":
#             active_assignment.status = "completed"
#             active_assignment.save()
#             driver.status = "available"
#             driver.save()

#         TrackingEvent.objects.create(
#             order=order,
#             event_type=new_status,
#             metadata={"previous_status": old_status, "driver_id": driver.id}
#         )

#         Notification.objects.create(
#             user=order.customer,
#             order=order,
#             message=f"Your order status has been updated to: {new_status}",
#             notification_type=new_status
#         )

#         AuditLog.objects.create(
#             user=driver_user,
#             action="status_changed",
#             entity_type="Order",
#             entity_id=order.id,
#             details={"from": old_status, "to": new_status, "driver_id": driver.id}
#         )

#     return order  

# def update_delivery_status(order_id, new_status, driver_user):

#     with transaction.atomic():

#         order = Order.objects.select_for_update().get(id=order_id)

#         try:
#             driver = Driver.objects.get(user=driver_user)
#         except Driver.DoesNotExist:
#             raise ValueError("No driver profile is linked to your account")

#         active_assignment = order.assignments.filter(driver=driver).exclude(status="completed").first()
#         if not active_assignment:
#             raise ValueError("You are not assigned to this order")

#         expected_next = VALID_TRANSITIONS.get(order.status)
#         if expected_next != new_status:
#             raise ValueError(
#                 f"Invalid transition: '{order.status}' → '{new_status}'. "
#                 f"Expected next status: '{expected_next}'"
#             )

#         old_status = order.status
#         order.status = new_status
#         order.save()

#         if new_status == "delivered":
#             active_assignment.status = "completed"
#             active_assignment.save()
#             driver.status = "available"
#             driver.save()

#         TrackingEvent.objects.create(
#             order=order,
#             event_type=new_status,
#             metadata={"previous_status": old_status, "driver_id": driver.id}
#         )

#         Notification.objects.create(
#             user=order.customer,
#             order=order,
#             message=f"Your order status has been updated to: {new_status}",
#             notification_type=new_status
#         )

#         AuditLog.objects.create(
#             user=driver_user,
#             action="status_changed",
#             entity_type="Order",
#             entity_id=order.id,
#             details={"from": old_status, "to": new_status, "driver_id": driver.id}
#         )

#     return order
