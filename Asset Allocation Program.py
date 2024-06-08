# Asset Allocation Program

def allocate_assets(risk_tolerance):
    allocation = {}
    
    if risk_tolerance == 'conservative':
        allocation = {'Stocks': 20, 'Bonds': 50, 'Cash': 30}
    elif risk_tolerance == 'moderate':
        allocation = {'Stocks': 50, 'Bonds': 30, 'Cash': 20}
    elif risk_tolerance == 'aggressive':
        allocation = {'Stocks': 70, 'Bonds': 20, 'Cash': 10}
    else:
        print("Invalid risk tolerance. Please choose conservative, moderate, or aggressive.")
        return None
    
    return allocation

def main():
    print("Welcome to the Asset Allocation Program")
    risk_tolerance = input("Enter your risk tolerance (conservative, moderate, aggressive): ").strip().lower()
    
    allocation = allocate_assets(risk_tolerance)
    
    if allocation:
        print("\nAsset Allocation based on your risk tolerance:")
        for asset, percentage in allocation.items():
            print(f"{asset}: {percentage}%")
    
if __name__ == "__main__":
    main()
