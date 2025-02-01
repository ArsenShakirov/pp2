def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

# Example usage
grams = float(input("grams: "))
print(f"{grams} grams is equal  {grams_to_ounces(grams)} ounces")

fahrenheit = float(input("Fara: "))
print(f"{fahrenheit} F is equal  {fahrenheit_to_celsius(fahrenheit)} C")
