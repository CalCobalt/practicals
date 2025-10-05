TARIFFS = {
    "11": 0.244618,
    "31": 0.136928,
    "22": 0.190500,
    "45": 0.300100,
    "99": 0.175000
}

def main():
    print("Electricity Bill Estimator 2.0")
    print("Available tariffs:", ", ".join(TARIFFS.keys()))

    tariff = input("Which tariff? (e.g. 11 or 31): ").strip()
    while tariff not in TARIFFS:
        print("Invalid tariff code. Please try again.")
        tariff = input("Which tariff? (e.g. 11 or 31): ").strip()

    daily_use = float(input("Enter daily use in kWh: "))
    billing_days = int(input("Enter number of billing days: "))
    cost_per_kwh = TARIFFS[tariff]
    total_bill = daily_use * billing_days * cost_per_kwh

    print(f"Estimated bill: ${total_bill:.2f}")

main()
