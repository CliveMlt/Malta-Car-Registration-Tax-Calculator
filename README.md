# Malta-Car-Registration-Tax-Calculator
 
Welcome to the Vehicle Registration Tax Calculator for Malta! This script calculates the registration tax based on various parameters including CO2 emissions, vehicle length, registration value, and Euro Standard.

## Features

- **Calculate Vehicle Registration Tax**: Supports both petrol and diesel vehicles.
- **Dynamic Calculation**: Uses specific rates for different Euro standards and vehicle lengths.
- **User-Friendly Input**: Prompts for necessary inputs and validates them.
- **Detailed Summary**: Provides a detailed summary of entered values and calculations.
- **Error Handling**: Includes error handling for invalid inputs.

## Prerequisites

- Python 3.x

## How to Use

1. Clone the repository or download the script file.
2. Run the script using Python:
   ```bash
   python malta_car_reg.py
   ```   
3. Follow the prompts to enter the required vehicle details:
- CO2 emissions (g/km)
- Registration Value (RV)
- Vehicle Length (mm)
- Euro Standard (3, 4, 5, 6)
4. Choose the vehicle type (Petrol or Diesel).
5. The script will calculate and display the total registration tax along with a summary of entered values.

## Calculations
- Length Tax Calculation:
Length Tax Rate is determined based on the vehicle length.
   ```bash
    Length Tax = Vehicle Length (mm) × Registration Value (RV) × Length Tax Rate / 100
   ```
   
- CO2 Tax Calculation:
CO2 Tax Rate is determined based on the Euro Standard.
   ```bash
    CO2 Tax = CO2 Emissions (g/km) × Registration Value (RV) × CO2 Tax Rate / 100
   ```

## Example Calculation
Let’s say we have the following vehicle details:
- CO2 Emissions: 298 g/km
- Registration Value (RV): €28,189
- Vehicle Length: 4,650 mm
- Euro Standard: 4

1. Length Tax Calculation:
For a vehicle length of 4,650 mm, the length tax rate is 0.0032%.
   ```bash
    Length Tax = 4650 × 28189 × 0.0032 100 = 4194.52
   ```
2. CO2 Tax Calculation:
For Euro Standard 4, the CO2 tax rate is 0.44%.
   ```bash
    CO2 Tax = 298 × 28189 × 0.44 100 = 36961.42
   ```
3. Total Registration Tax
   ```bash
    Total Tax = Length Tax + CO2 Tax = 4194.52 + 36961.42 = 41155.94
   ```
## Example Output
   ```bash
    
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
    
    1. Petrol Vehicle
    2. Diesel Vehicle
    3. Exit
    Enter your choice (1/2/3): 1
    Enter CO2 emissions (g/km): 298
    Enter Registration Value (RV): 28189
    Enter Vehicle Length (mm): 4650
    Enter Euro Standard (3, 4, 5, 6): 4
    +-----------------------------+-------------------------------+
    | Value                      | Entered Value                  |
    +-----------------------------+-------------------------------+
    | CO2 Emissions              | 298.00                         |
    | Registration Value (RV)    | 28189.00                       |
    | Vehicle Length (mm)        | 4650.00                        |
    | Euro Standard              | 4                              |
    +-----------------------------+-------------------------------+
    
    Length Tax Calculation: 4650.0 * 28189.0 * 0.0032 / 100 = 4194.52
    CO2 Tax Calculation: 298.0 * 28189.0 * 0.44 / 100 = 36961.42
    Total Tax Calculation: 4194.52 + 36961.42 = 41155.94
    
    +----------------+------------------------------+
    |  Vehicle Type  |  Total Registration Tax (€)  |
    +----------------+------------------------------+
    | Petrol Vehicle |           41155.94           |
    +----------------+------------------------------+   
   ```
    
## Document Reference
This script is based on the calculations and guidelines provided in the document using NEDC rates:
**Document:** SOPV 02 - Registering & Licensing of New & Used Motor Vehicles
**Source:** Transport Malta

## License
This project is licensed under the MIT License.