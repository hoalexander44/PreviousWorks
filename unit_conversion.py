#This is a unit converter

# intro text that introduces the user what this program does and how to use it
print('Welcome to the length conversion wizard')
print('This program can convert between any of the following lengths.')
print('inches\nfeet\nyards\nmiles\nleagues\ncentimeters\ndecimeters\nmeters\ndecameters\nhectometers\nkilometers')
print('Note: You must use the units exactly as spelled above.\n')

# inputs variables that the user will fill in

value = float(input('Please enter a value\n'))
unit = input('Please enter a unit\n')
new_unit = input('What would you like your new unit to be\n')

# dictionary that holds unit conversions with the base unit being a meter
unit_dictionary = {
    'centimeters': 0.0100,
    'decimeters': 0.1000,
    'meters': 1.0000,
    'decameters': 10.0000,
    'hectometers': 100.0000,
    'kilometers': 1000.0000,
    'inches': 0.0254,
    'feet': 0.3048,
    'yards': 0.9144,
    'miles': 1609.3440,
    'leagues': 4828.0320

}

# The algorithem that calculates the new unit
new_value = (value * unit_dictionary[str(unit)])/unit_dictionary[str(new_unit)]

# outputs the new unit to the user
print(value, unit, 'is', round(new_value, 4), new_unit)
