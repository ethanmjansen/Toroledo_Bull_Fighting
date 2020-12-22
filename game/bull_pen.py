from bull import Bull

def make_bulls():
    # Makes bulls and picks their status
    bulls = {
    'Mooses' : Bull('Mooses', 7, 6, 4, 8),
    'Buster': Bull('Buster', 5, 2, 9, 6),
    'T-Bone': Bull('T-Bone', 8, 5, 8, 7),
    'Wully': Bull('Wully', 3, 6, 5, 7),
    'Jake': Bull('Jake', 9, 9, 9, 9),
    'Havacow': Bull('Havacow', 6, 9, 7, 5), 
    'El Torro': Bull('El Torro', 8, 9, 5, 5), 
    'Countess': Bull('Countess', 9, 9, 9, 0), 
    'Evo': Bull('Evo', 9, 6, 7, 5), 
    'Rocky': Bull('Rocky', 4, 9, 6, 9), 
    'Nartcow': Bull('Nartcow', 6, 2, 8, 9),
    'Momur': Bull('Momur', 5, 8, 9, 3),
    'Bulloni': Bull('Bulloni', 8, 2, 9, 9),
    'Lao': Bull('Lao', 8, 9, 8, 9),
    'Kowking': Bull('Kowking', 9, 4, 8, 7),
    'Mooer': Bull('Mooer', 5, 7, 9, 9),
    'Cooky': Bull('Cooky', 9, 4, 8, 8), 
    'Bull Nye': Bull('Bull Nye', 7, 7, 7, 7), 
    'Bullty': Bull('Bullty', 6, 3, 9, 9), 
    'Chips': Bull('Chips', 1, 1, 1, 1)
    }

    for bull in bulls.values():
        bull.pick_status()
    
    return bulls

if __name__ == "__main__":
    """Proof of Concept"""
    bulls = make_bulls()
    for bull in bulls.values():
        print(f'{bull}\n')

