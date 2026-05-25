from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db import transaction
from decimal import Decimal

from .models import Wallet, Transaction
from .serializers import WalletSerializer, TransactionSerializer


class WalletListCreateAPI(generics.ListCreateAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionListAPI(generics.ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(wallet__user=self.request.user)


class DepositAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        amount = request.data.get("amount")

        if not amount:
            return Response({"error": "Amount required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = Decimal(amount)
        except:
            return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

        if amount <= 0:
            return Response({"error": "Amount must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)

        wallet, created = Wallet.objects.get_or_create(user=user)

        with transaction.atomic():
            wallet.balance += amount
            wallet.save()

            Transaction.objects.create(
                wallet=wallet,
                transaction_type="deposit",
                amount=amount
            )

        return Response({
            "message": "Deposit successful",
            "new_balance": wallet.balance
        }, status=status.HTTP_200_OK)


class WithdrawAPI(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        amount = request.data.get("amount")

        if not amount:
            return Response({"error": "Amount required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            amount = Decimal(amount)
        except:
            return Response({"error": "Invalid amount"}, status=status.HTTP_400_BAD_REQUEST)

        if amount <= 0:
            return Response({"error": "Amount must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)

        wallet, created = Wallet.objects.get_or_create(user=user)

        if wallet.balance < amount:
            return Response({"error": "Insufficient balance"}, status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            wallet.balance -= amount
            wallet.save()

            Transaction.objects.create(
                wallet=wallet,
                transaction_type="withdraw",
                amount=amount
            )

        return Response({
            "message": "Withdraw successful",
            "new_balance": wallet.balance
        }, status=status.HTTP_200_OK)