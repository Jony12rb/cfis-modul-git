import csv

def main():
    # Open the CSV file
    with open('data.csv', mode='r') as file:
        # Create a CSV reader object
        csv_reader = csv.reader(file)
        
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Print each row
            print(rows)
            
if __name__ == "__main__":
    main()