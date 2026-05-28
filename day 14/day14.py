
# class TransferMoneyAPI(APIView):

#     permission_classes = [IsAuthenticated]

#     def post(self, request):

#         try:

#             sender_wallet = Wallet.objects.get(
#                 id=request.data.get("sender_wallet"),
#                 owner=request.user
#             )

#             receiver_wallet = Wallet.objects.get(
#                 id=request.data.get("receiver_wallet")
#             )

#             amount = float(request.data.get("amount"))

#             WalletService.transfer_money(
#                 sender_wallet,
#                 receiver_wallet,
#                 amount
#             )

#             return Response({
#                 "message": "Transfer successful"
#             }, status=status.HTTP_200_OK)

#         except Wallet.DoesNotExist:

#             return Response({
#                 "error": "Wallet not found"
#             }, status=status.HTTP_404_NOT_FOUND)

#         except Exception as e:

#             return Response({
#                 "error": str(e)
#             }, status=status.HTTP_400_BAD_REQUEST)


# from django.urls import path

# urlpatterns = [

#     # JWT AUTH
#     path(
#         "api/token/",
#         TokenObtainPairView.as_view(),
#         name="token_obtain_pair"
#     ),

#     path(
#         "api/token/refresh/",
#         TokenRefreshView.as_view(),
#         name="token_refresh"
#     ),

#     # WALLETS
#     path(
#         "wallets/",
#         WalletListCreateAPI.as_view(),
#         name="wallet-list"
#     ),

#     path(
#         "wallets/<int:pk>/",
#         WalletDetailAPI.as_view(),
#         name="wallet-detail"
#     ),

#     # TRANSFER
#     path(
#         "transfer/",
#         TransferMoneyAPI.as_view(),
#         name="transfer"
#     ),

#     # PUBLIC
#     path(
#         "public/",
#         PublicAPI.as_view(),
#         name="public"
#     )
# ]


#   def get_queryset(self):

#         return Wallet.objects.select_related(
#             "owner"
#         ).prefetch_related(
#             "transactions"
#         ).filter(owner=self.request.user)

#     def perform_create(self, serializer):

#         serializer.save(owner=self.request.user)


# class WalletDetailAPI(generics.RetrieveUpdateDestroyAPIView):

#     serializer_class = WalletSerializer

#     permission_classes = [IsAuthenticated, IsOwner]

#     queryset = Wallet.objects.all()

# class Transaction(models.Model):

#     TRANSACTION_TYPES = [
#         ("deposit", "Deposit"),
#         ("withdraw", "Withdraw"),
#         ("transfer", "Transfer")
#     ]

#     wallet = models.ForeignKey(
#         Wallet,
#         on_delete=models.CASCADE,
#         related_name="transactions"
#     )

#     amount = models.DecimalField(max_digits=12, decimal_places=2)

#     transaction_type = models.CharField(
#         max_length=20,
#         choices=TRANSACTION_TYPES
#     )

#     description = models.TextField(blank=True)

#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.wallet.name} - {self.transaction_type}"


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):

#     if created:
#         Profile.objects.create(
#             user=instance,
#             country="Unknown"
#         )