name = 'Zed A. Shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm = 2.54  # 1 inch is approximately equal to 2.54 cm
kg = 0.4535924  # 1 pound is equal to 0.4535924 kg

print(f"Let's talk about {name}")
print(f"He's {height * cm} inches tall.")
print(f"He's {weight * kg} pounds heavy.")
print(f"Actually, that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are actually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + (height * cm) + (weight * kg)
print(f"If I had {age}, {height}, and {weight}")