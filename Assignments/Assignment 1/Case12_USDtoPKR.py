#    Currency Converter (USD to PKR)
fixed_exchange_rate = 283.38   # fixed exchange rate as per latest report

USD = float(input("Enter amount in USD:  "))
PKR = USD * fixed_exchange_rate

print(f"{USD} USD = {PKR} PKR")

