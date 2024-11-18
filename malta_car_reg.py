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
    """
    print(banner)


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


def get_euro_standard():
    """Prompt the user to select a Euro Standard."""
    euro_standard_map = {
        6: "Euro 6",
        5: "Euro 5",
        4: "Euro 4",
        3: "Euro 3",
        2: "Euro 2",
        1: "Euro 1",
    }

    print("Select the Euro Standard:")
    for number, description in euro_standard_map.items():
        print(f"{number}: {description}")

    while True:
        try:
            euro_standard_number = int(input("Enter the corresponding number (1-6): "))
            if euro_standard_number in euro_standard_map:
                return euro_standard_number
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


class VehicleTaxCalculator:
    def __init__(self, co2_emissions, rv, length, euro_standard, vehicle_type):
        self.co2_emissions = co2_emissions
        self.rv = rv
        self.length = length
        self.euro_standard = euro_standard
        self.vehicle_type = vehicle_type
        self.length_tax_rate = self.get_length_tax_rate()
        self.co2_tax_rate = self.get_co2_tax_rate(vehicle_type)

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

    def get_co2_tax_rate(self, vehicle_type):
        """Determine the CO2 tax rate based on the vehicle's CO2 emissions and numeric Euro Standard."""
        co2_rate_table = {
            "petrol": {
                (0, 100): [0.07, 0.15, 0.20, 0.23],
                (101, 130): [0.09, 0.17, 0.23, 0.26],
                (131, 140): [0.10, 0.19, 0.26, 0.30],
                (141, 150): [0.11, 0.22, 0.29, 0.33],
                (151, 180): [0.16, 0.24, 0.32, 0.37],
                (181, 220): [0.18, 0.26, 0.35, 0.40],
                (221, 250): [0.21, 0.29, 0.38, 0.44],
                (251, float("inf")): [0.23, 0.31, 0.41, 0.47],
            },
            "diesel": {
                (0, 100): [0.07, 0.15, 0.20, 0.23],
                (101, 130): [0.09, 0.17, 0.23, 0.26],
                (131, 140): [0.10, 0.19, 0.26, 0.30],
                (141, 150): [0.11, 0.22, 0.29, 0.33],
                (151, 180): [0.16, 0.24, 0.32, 0.37],
                (181, 220): [0.18, 0.26, 0.35, 0.40],
                (221, 250): [0.21, 0.29, 0.38, 0.44],
                (251, float("inf")): [0.23, 0.31, 0.41, 0.47],
            },
        }

        # Determine the Euro Standard index
        euro_index = max(0, min(6 - self.euro_standard, 3))  # Clamp index to range 0–3

        # Match CO2 range to rates
        for co2_range, rates in co2_rate_table[vehicle_type].items():
            if co2_range[0] <= self.co2_emissions <= co2_range[1]:
                return rates[euro_index] / 100  # Convert percentage to decimal

        raise ValueError("CO2 emissions are out of range.")


    def calculate_length_tax(self):
        """Calculate the length tax based on the vehicle's length and registration value."""
        length_tax = self.length * self.rv * self.length_tax_rate / 100
        print(f"Length Tax Calculation: {self.length} * {self.rv} * {self.length_tax_rate} / 100 = {length_tax:.2f}")
        return length_tax

    def calculate_co2_tax(self):
        """Calculate the CO2 tax based on the vehicle's CO2 emissions and registration value."""
        rounded_tax_rate = round(self.co2_tax_rate, 4)
        co2_tax = self.co2_emissions * self.rv * rounded_tax_rate
        print(f"CO2 Tax Calculation: {self.co2_emissions} * {self.rv} * {rounded_tax_rate} = {round(co2_tax, 2):.2f}")
        return co2_tax

    def calculate_total_tax(self):
        """Calculate the total tax by summing length tax and CO2 tax."""
        length_tax = self.calculate_length_tax()
        co2_tax = self.calculate_co2_tax()
        total_tax = length_tax + co2_tax
        print(f"Total Tax Calculation: {length_tax:.2f} + {co2_tax:.2f} = {total_tax:.2f}")
        return total_tax


def main():
    """Main function to run the vehicle tax calculator."""
    show_banner()
    print("1. Petrol Vehicle")
    print("2. Diesel Vehicle")
    print("3. Exit")

    choice = int(input("Enter your choice (1/2/3): "))
    if choice == 3:
        print("Exiting...")
        return

    vehicle_type = "petrol" if choice == 1 else "diesel"

    co2_emissions = float(input("Enter CO2 emissions (g/km): "))
    rv = float(input("Enter Registration Value (RV): "))
    length = float(input("Enter Vehicle Length (mm): "))
    euro_standard = get_euro_standard()

    print_summary(co2_emissions, rv, length, f"Euro {euro_standard}")

    try:
        calculator = VehicleTaxCalculator(co2_emissions, rv, length, euro_standard, vehicle_type)

        total_tax = calculator.calculate_total_tax()

        print("\n+------------------+-------------------------------+")
        print(f"| {'Vehicle Type':<16} | {'Total Registration Tax (€)':<29} |")
        print("+------------------+-------------------------------+")
        print(f"| {vehicle_type.capitalize():<16} | {total_tax:<29.2f} |")
        print("+------------------+-------------------------------+")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
