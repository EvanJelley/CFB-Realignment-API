import csv

def csv_to_object_list(csv_file_path):
    objects = []
    id_counter = 1000  # Start IDs from 1000

    with open(csv_file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)
        
        for row in csvreader:
            # Create a dictionary for each city
            city_object = {
                "id": id_counter,
                "city": row[0],
                "state": row[1],
                "latitude": float(row[2]),
                "longitude": float(row[3])
            }
            objects.append(city_object)
            id_counter += 1  # Increment the ID counter for each city

    return objects

csv_file_path = 'DatabaseCreation/DistanceCalculator/majorCities.csv'  # Path to your CSV file
city_objects = csv_to_object_list(csv_file_path)

print(city_objects)  # Print the list of city objects
