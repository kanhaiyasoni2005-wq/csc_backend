# # 1. Cashfree se payment status check karo
# response = cashfree.PGOrderFetchPayments(
#     "2023-08-01",
#     order.cashfree_order_id
# )

# payments = response.data

# # 2. Dekho payment SUCCESS hua ya nahi
# for payment in payments:
#     if payment.payment_status == "SUCCESS":

#         # 3. Database update karo
#         order.payment_status = "paid"
#         order.status = "confirmed"

#         db.commit()

#         print("Payment successful!")
#         break