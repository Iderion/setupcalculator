def calculate_aero_adjustments(current_setup, top_speed, understeer, oversteer, target):
    adjustments = {}
    reasons = []
    
    # Logik für Frontflügel
    if understeer and not oversteer:
        if target == "more_grip":
            adjustments["front_wing"] = current_setup.get("front_wing", 0) + 2
            reasons.append("Frontflügel erhöht (+2) wegen Untersteuern und Ziel 'Mehr Grip'")
        else:
            adjustments["front_wing"] = current_setup.get("front_wing", 0) + 1
            reasons.append("Frontflügel erhöht (+1) wegen Untersteuern")
    
    # Logik für Heckflügel bei Topspeed-Problemen
    if top_speed < 320 and target == "top_speed":
        if current_setup.get("rear_wing", 0) > 40:
            adjustments["rear_wing"] = current_setup.get("rear_wing", 0) - 3
            reasons.append("Heckflügel reduziert (-3) für höhere Topspeed")
        else:
            adjustments["rear_wing"] = current_setup.get("rear_wing", 0) - 1
            reasons.append("Heckflügel leicht reduziert (-1) für bessere Topspeed")
    
    return {"adjustments": adjustments, "reasons": reasons}