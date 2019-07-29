sweaterPrice = 68
computerPrice = 75
bracletPrice = 43

sweaterCount = 3
computerCount = 1
bracletCount = 2

rebatePrice = 10
returnBracletCount = 1

totalPrice = ((sweaterPrice * sweaterCount) + (computerPrice +
                                               computerCount) + (bracletPrice * bracletCount))
disountedPrice = (rebatePrice + (returnBracletCount * bracletPrice))
finalPrice = totalPrice - disountedPrice

print(finalPrice)
