def length_converter():
    units = {
        'm': {'name': 'Meters', 'factor': 1},
        'cm': {'name': 'Centimeters', 'factor': 0.01},
        'km': {'name': 'Kilometers', 'factor': 1000},
        'in': {'name': 'Inches', 'factor': 0.0254},
        'ft': {'name': 'Feet', 'factor': 0.3048}
    }
    
    print("\nLength Units:")
    for key, val in units.items():
        print(f"{key}: {val['name']}")
    
    from_unit = input("Convert from (unit): ").lower()
    to_unit = input("Convert to (unit): ").lower()
    
    if from_unit not in units or to_unit not in units:
        print("Invalid unit!")
        return
    
    value = float(input("Enter value: "))
    
    # Conversion logic
    meters = value * units[from_unit]['factor']
    result = meters / units[to_unit]['factor']
    print(f"\nResult: {value} {units[from_unit]['name']} = {result:.2f} {units[to_unit]['name']}")

def temperature_converter():
    units = {
        'c': 'Celsius',
        'f': 'Fahrenheit',
        'k': 'Kelvin'
    }
    
    print("\nTemperature Units:")
    for key, val in units.items():
        print(f"{key}: {val}")
    
    from_unit = input("Convert from (unit): ").lower()
    to_unit = input("Convert to (unit): ").lower()
    
    temp = float(input("Enter temperature: "))
    
    if from_unit == 'c':
        if to_unit == 'f':
            result = (temp * 9/5) + 32
        elif to_unit == 'k':
            result = temp + 273.15
        else:
            result = temp
    elif from_unit == 'f':
        if to_unit == 'c':
            result = (temp - 32) * 5/9
        elif to_unit == 'k':
            result = (temp - 32) * 5/9 + 273.15
        else:
            result = temp
    elif from_unit == 'k':
        if to_unit == 'c':
            result = temp - 273.15
        elif to_unit == 'f':
            result = (temp - 273.15) * 9/5 + 32
        else:
            result = temp
    else:
        print("Invalid unit!")
        return
    
    print(f"\nResult: {temp} {units[from_unit]} = {result:.2f} {units[to_unit]}")

def weight_converter():
    units = {
        'kg': {'name': 'Kilograms', 'factor': 1},
        'g': {'name': 'Grams', 'factor': 0.001},
        'lb': {'name': 'Pounds', 'factor': 0.453592},
        'oz': {'name': 'Ounces', 'factor': 0.0283495}
    }
    
    print("\nWeight Units:")
    for key, val in units.items():
        print(f"{key}: {val['name']}")
    
    from_unit = input("Convert from (unit): ").lower()
    to_unit = input("Convert to (unit): ").lower()
    
    if from_unit not in units or to_unit not in units:
        print("Invalid unit!")
        return
    
    value = float(input("Enter value: "))
    
    # Conversion logic
    kg = value * units[from_unit]['factor']
    result = kg / units[to_unit]['factor']
    print(f"\nResult: {value} {units[from_unit]['name']} = {result:.2f} {units[to_unit]['name']}")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Length Converter")
        print("2. Temperature Converter")
        print("3. Weight Converter")
        print("4. Exit")
        choice = input("Choose option (1-4): ")
        
        if choice == '1':
            length_converter()
        elif choice == '2':
            temperature_converter()
        elif choice == '3':
            weight_converter()
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

if _name_ == "_main_":
    main_menu()
