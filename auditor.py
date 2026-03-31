import db_manager

def run_audit():
    # Input simulation (In London, this will be an API call)
    item = "Industrial Sensors"
    value = 4500.00
    rate = 0.12 # 12% Duty
    
    # Logic
    if value > 1000 and rate < 0.15:
        status = "FLAG: Potential Under-valuation"
    else:
        status = "PASS"
        
    print(f"Auditing {item}... Result: {status}")
    
    # Persistence
    db_manager.init_db()
    db_manager.log_audit(item, value, rate, status)

if __name__ == "__main__":
    run_audit()

