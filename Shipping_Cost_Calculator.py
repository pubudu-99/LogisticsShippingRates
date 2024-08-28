# Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
shipping_cost = weight * rate

## Display the result
print("Shipping Cost: {shipping_cost} USD")

print("Hooray You have successfully created a Shipping Cost Calculator in Python.")