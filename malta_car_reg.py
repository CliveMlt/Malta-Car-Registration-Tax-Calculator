def show_banner():
    """Display a banner when the script starts."""
    banner = """
███╗   ███╗ █████╗ ██╗  ████████╗ █████╗      ██████╗ █████╗ ██████╗                                                     
████╗ ████║██╔══██╗██║  ╚══██╔══╝██╔══██╗    ██╔════╝██╔══██╗██╔══██╗                                                    
██╔████╔██║███████║██║     ██║   ███████║    ██║     ███████║██████╔╝                                                    
██║╚██╔╝██║██╔══██║██║     ██║   ██╔══██║    ██║     ██╔══██║██╔══██╗                                                    
██║ ╚═╝ ██║██║  ██║███████╗██║   ██║  ██║    ╚██████╗██║  ██║██║  ██║                                                    
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝                                                    
                                                                                                                         
██████╗ ███████╗ ██████╗ ██╗███████╗████████╗██████╗  █████╗ ████████╗██╗ ██████╗ ███╗   ██╗    ████████╗ █████╗ ██╗  ██╗
██╔══██╗██╔════╝██╔════╝ ██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗████╗  ██║    ╚══██╔══╝██╔══██╗╚██╗██╔╝
██████╔╝█████╗  ██║  ███╗██║███████╗   ██║   ██████╔╝███████║   ██║   ██║██║   ██║██╔██╗ ██║       ██║   ███████║ ╚███╔╝ 
██╔══██╗██╔══╝  ██║   ██║██║╚════██║   ██║   ██╔══██╗██╔══██║   ██║   ██║██║   ██║██║╚██╗██║       ██║   ██╔══██║ ██╔██╗ 
██║  ██║███████╗╚██████╔╝██║███████║   ██║   ██║  ██║██║  ██║   ██║   ██║╚██████╔╝██║ ╚████║       ██║   ██║  ██║██╔╝ ██╗
╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ ╚═╝  ╚═══╝       ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                                         
 ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗                                       
██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗                                      
██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝                                      
██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗                                      
╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║                                      
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝                                                                      
    """
    print(banner)

#_______________________________________________________________________________________________________________

class VehicleTaxCalculator:
    def __init__(self, co2_emissions, rv, length, euro_standard):
        self.co2_emissions = co2_emissions
        self.rv = rv
        self.length = length
        self.euro_standard = euro_standard
        self.length_tax_rate = self.get_length_tax_rate()
        self.co2_tax_rate = self.get_co2_tax_rate()

#_______________________________________________________________________________________________________________

    def get_length_tax_rate(self):
        """Determine the length tax rate based on vehicle length."""
        if self.length <= 3450:
            return 0.0020
        elif self.length <= 3640:
            return 0.0022
        elif self.length <= 3770:
            return 0.0024
        elif self.length <= 4030:
            return 0.0026
        elif self.length <= 4370:
            return 0.0028
        elif self.length <= 4570:
            return 0.0030
        elif self.length <= 4770:
            return 0.0032
        else:
            return 0.0034

#_______________________________________________________________________________________________________________

    def get_co2_tax_rate(self):
        """Determine the CO2 tax rate based on Euro Standard."""
        if self.euro_standard == '3':
            return 0.47
        elif self.euro_standard == '4':
            return 0.44
        elif self.euro_standard in ['5', '6']:
            return 0.41
        else:
            raise ValueError("Invalid Euro Standard")

#_______________________________________________________________________________________________________________

    def calculate_length_tax(self):
        """Calculate the length tax based on the vehicle's length and registration value."""
        length_tax = self.length * self.rv * self.length_tax_rate / 100
        print(f"Length Tax Calculation: {self.length} * {self.rv} * {self.length_tax_rate} / 100 = {length_tax:.2f}")
        return length_tax

#_______________________________________________________________________________________________________________

    def calculate_co2_tax(self):
        """Calculate the CO2 tax based on the vehicle's CO2 emissions and registration value."""
        co2_tax = self.co2_emissions * self.rv * self.co2_tax_rate / 100
        print(f"CO2 Tax Calculation: {self.co2_emissions} * {self.rv} * {self.co2_tax_rate} / 100 = {co2_tax:.2f}")
        return co2_tax

#_______________________________________________________________________________________________________________

    def calculate_total_tax(self):
        """Calculate the total tax by summing length tax and CO2 tax."""
        length_tax = self.calculate_length_tax()
        co2_tax = self.calculate_co2_tax()
        total_tax = length_tax + co2_tax
        print(f"Total Tax Calculation: {length_tax:.2f} + {co2_tax:.2f} = {total_tax:.2f}")
        return total_tax

#_______________________________________________________________________________________________________________

def get_float_input(prompt):
    """Get a float input from the user with validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#_______________________________________________________________________________________________________________

def get_non_empty_string(prompt):
    """Get a non-empty string input from the user with validation."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please enter a valid value.")

#_______________________________________________________________________________________________________________

def get_numeric_string(prompt, valid_values):
    """Get a numeric string input from the user with validation."""
    while True:
        value = input(prompt).strip()
        if value in valid_values:
            return value
        else:
            print(f"Invalid input. Please enter one of the following values: {', '.join(valid_values)}.")

#_______________________________________________________________________________________________________________

def print_summary(co2_emissions, rv, length, euro_standard):
    """Print a summary of the entered values."""
    print("+-----------------------------+-------------------------------+")
    print(f"| {'Value':<24}   | {'Entered Value':<30} |")
    print("+-----------------------------+-------------------------------+")
    print(f"| CO2 Emissions              | {co2_emissions:<30.2f} |")
    print(f"| Registration Value (RV)    | {rv:<30.2f} |")
    print(f"| Vehicle Length (mm)        | {length:<30.2f} |")
    print(f"| Euro Standard              | {euro_standard:<30} |")
    print("+-----------------------------+-------------------------------+")
    print()

#_______________________________________________________________________________________________________________

def main():
    """Main function to run the vehicle tax calculator."""
    show_banner()
    print("1. Petrol Vehicle")
    print("2. Diesel Vehicle")
    print("3. Exit")

    choice = get_float_input("Enter your choice (1/2/3): ")
    if choice not in [1, 2]:
        print("Exiting...")
        return

    co2_emissions = get_float_input("Enter CO2 emissions (g/km): ")
    rv = get_float_input("Enter Registration Value (RV): ")
    length = get_float_input("Enter Vehicle Length (mm): ")
    euro_standard = get_numeric_string("Enter Euro Standard (3, 4, 5, 6): ", ['3', '4', '5', '6'])

    try:
        calculator = VehicleTaxCalculator(co2_emissions, rv, length, euro_standard)

        # Print the summary of entered values
        print_summary(co2_emissions, rv, length, euro_standard)

        # Calculate and print the total tax
        total_tax = calculator.calculate_total_tax()
        print()
        print(f"+----------------+------------------------------+")
        print(f"|  Vehicle Type  |  Total Registration Tax (€)  |")
        print(f"+----------------+------------------------------+")
        vehicle_type = "Petrol Vehicle" if choice == 1 else "Diesel Vehicle"
        print(f"|{vehicle_type:^16}|{total_tax:^30.2f}|")
        print(f"+----------------+------------------------------+")

    except ValueError as e:
        print(f"Error: {e}")

#_______________________________________________________________________________________________________________

if __name__ == "__main__":
    main()
