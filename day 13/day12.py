# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  

#     def get_balance(self):
#         return self.__balance

# class WalletService:
#     def __init__(self):
#         self.wallets = [] 

#     def create_wallet(self, wallet):
#         self.wallets.append(wallet)

# def deposit(balance, amount):
#     if amount <= 0:
#         return "Invalid amount"
#     balance += amount
#     return balance

# history = []
# history.append("Deposited 100")
# history.append("Withdrew 50")

# for h in history:
#     print(h)

# def cli():
#     while True:
#         print("\n1. Create\n2. Deposit\n3. Exit")
#         choice = input("Choose: ")

#         if choice == "3":
#             break

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount <= 0:
#             return "Invalid deposit"
#         self.__balance += amount
#         return self.__balance

# class WalletService:
#     def __init__(self):
#         self.wallets = {}  # key = owner name

#     def create_wallet(self, owner, balance):
#         if owner in self.wallets:
#             return "Wallet already exists"
#         self.wallets[owner] = Wallet(owner, balance)
#         return "Wallet created"

# class Wallet:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance
#         self.history = []

#     def deposit(self, amount):
#         if amount <= 0:
#             return "Invalid amount"
#         self.__balance += amount
#         self.history.append(f"Deposited {amount}")
#         return self.__balance

#     def withdraw(self, amount):
#         if amount > self.__balance:
#             return "Insufficient funds"
#         self.__balance -= amount
#         self.history.append(f"Withdrew {amount}")
#         return self.__balancefrom wallet_app.services.wallet_service import WalletService



# class WalletListCreateAPI(generics.ListCreateAPIView):
#     serializer_class = WalletSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Wallet.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


# class TransactionListAPI(generics.ListAPIView):
#     serializer_class = TransactionSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Transaction.objects.filter(wallet__user=self.request.user)


# class DepositAPI(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         amount = request.data.get("amount")

#         if not amount:
#             return Response({"error": "Amount required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             amount = Decimal(amount)
#         except:
#             return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

#         if amount <= 0:
#             return Response({"error": "Amount must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)

#         wallet, created = Wallet.objects.get_or_create(user=user)

#         with transaction.atomic():
#             wallet.balance += amount
#             wallet.save()

#             Transaction.objects.create(
#                 wallet=wallet,
#                 transaction_type="deposit",
#                 amount=amount
#             )

#         return Response({
#             "message": "Deposit successful",
#             "new_balance": wallet.balance
#         }, status=status.HTTP_200_OK)


# class WithdrawAPI(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         user = request.user
#         amount = request.data.get("amount")

#         if not amount:
#             return Response({"error": "Amount required"}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             amount = Decimal(amount)
#         except:
#             return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

#         if amount <= 0:
#             return Response({"error": "Amount must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)

#         wallet, created = Wallet.objects.get_or_create(user=user)

#         if wallet.balance < amount:
#             return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

#         with transaction.atomic():
#             wallet.balance -= amount
#             wallet.save()

#             Transaction.objects.create(
#                 wallet=wallet,
#                 transaction_type="withdraw",
#                 amount=amount
#             )

#         return Response({
#             "message": "Withdraw successful",
#             "new_balance": wallet.balance
#         }, status=status.HTTP_200_OK)