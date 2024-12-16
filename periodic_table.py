# Dizionario con tutti gli elementi chimici della tavola periodica
periodic_table = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "atomic_mass": 1.008},
    "He": {"name": "Helium", "atomic_number": 2, "atomic_mass": 4.0026},
    "Li": {"name": "Lithium", "atomic_number": 3, "atomic_mass": 6.94},
    "Be": {"name": "Beryllium", "atomic_number": 4, "atomic_mass": 9.0122},
    "B": {"name": "Boron", "atomic_number": 5, "atomic_mass": 10.81},
    "C": {"name": "Carbon", "atomic_number": 6, "atomic_mass": 12.011},
    "N": {"name": "Nitrogen", "atomic_number": 7, "atomic_mass": 14.007},
    "O": {"name": "Oxygen", "atomic_number": 8, "atomic_mass": 15.999},
    "F": {"name": "Fluorine", "atomic_number": 9, "atomic_mass": 18.998},
    "Ne": {"name": "Neon", "atomic_number": 10, "atomic_mass": 20.180},
    "Na": {"name": "Sodium", "atomic_number": 11, "atomic_mass": 22.990},
    "Mg": {"name": "Magnesium", "atomic_number": 12, "atomic_mass": 24.305},
    "Al": {"name": "Aluminum", "atomic_number": 13, "atomic_mass": 26.982},
    "Si": {"name": "Silicon", "atomic_number": 14, "atomic_mass": 28.085},
    "P": {"name": "Phosphorus", "atomic_number": 15, "atomic_mass": 30.974},
    "S": {"name": "Sulfur", "atomic_number": 16, "atomic_mass": 32.06},
    "Cl": {"name": "Chlorine", "atomic_number": 17, "atomic_mass": 35.45},
    "Ar": {"name": "Argon", "atomic_number": 18, "atomic_mass": 39.948},
    "K": {"name": "Potassium", "atomic_number": 19, "atomic_mass": 39.098},
    "Ca": {"name": "Calcium", "atomic_number": 20, "atomic_mass": 40.078},
    "Sc": {"name": "Scandium", "atomic_number": 21, "atomic_mass": 44.956},
    "Ti": {"name": "Titanium", "atomic_number": 22, "atomic_mass": 47.867},
    "V": {"name": "Vanadium", "atomic_number": 23, "atomic_mass": 50.942},
    "Cr": {"name": "Chromium", "atomic_number": 24, "atomic_mass": 51.996},
    "Mn": {"name": "Manganese", "atomic_number": 25, "atomic_mass": 54.938},
    "Fe": {"name": "Iron", "atomic_number": 26, "atomic_mass": 55.845},
    "Co": {"name": "Cobalt", "atomic_number": 27, "atomic_mass": 58.933},
    "Ni": {"name": "Nickel", "atomic_number": 28, "atomic_mass": 58.693},
    "Cu": {"name": "Copper", "atomic_number": 29, "atomic_mass": 63.546},
    "Zn": {"name": "Zinc", "atomic_number": 30, "atomic_mass": 65.38},
    "Ga": {"name": "Gallium", "atomic_number": 31, "atomic_mass": 69.723},
    "Ge": {"name": "Germanium", "atomic_number": 32, "atomic_mass": 72.63},
    "As": {"name": "Arsenic", "atomic_number": 33, "atomic_mass": 74.922},
    "Se": {"name": "Selenium", "atomic_number": 34, "atomic_mass": 78.971},
    "Br": {"name": "Bromine", "atomic_number": 35, "atomic_mass": 79.904},
    "Kr": {"name": "Krypton", "atomic_number": 36, "atomic_mass": 83.798},
    "Rb": {"name": "Rubidium", "atomic_number": 37, "atomic_mass": 85.468},
    "Sr": {"name": "Strontium", "atomic_number": 38, "atomic_mass": 87.62},
    "Y": {"name": "Yttrium", "atomic_number": 39, "atomic_mass": 88.906},
    "Zr": {"name": "Zirconium", "atomic_number": 40, "atomic_mass": 91.224},
    "Nb": {"name": "Niobium", "atomic_number": 41, "atomic_mass": 92.906},
    "Mo": {"name": "Molybdenum", "atomic_number": 42, "atomic_mass": 95.95},
    "Tc": {"name": "Technetium", "atomic_number": 43, "atomic_mass": 98},
    "Ru": {"name": "Ruthenium", "atomic_number": 44, "atomic_mass": 101.07},
    "Rh": {"name": "Rhodium", "atomic_number": 45, "atomic_mass": 102.91},
    "Pd": {"name": "Palladium", "atomic_number": 46, "atomic_mass": 106.42},
    "Ag": {"name": "Silver", "atomic_number": 47, "atomic_mass": 107.87},
    "Cd": {"name": "Cadmium", "atomic_number": 48, "atomic_mass": 112.41},
    "In": {"name": "Indium", "atomic_number": 49, "atomic_mass": 114.82},
    "Sn": {"name": "Tin", "atomic_number": 50, "atomic_mass": 118.71},
    "Sb": {"name": "Antimony", "atomic_number": 51, "atomic_mass": 121.76},
    "Te": {"name": "Tellurium", "atomic_number": 52, "atomic_mass": 127.6},
    "I": {"name": "Iodine", "atomic_number": 53, "atomic_mass": 126.90},
    "Xe": {"name": "Xenon", "atomic_number": 54, "atomic_mass": 131.29},
    "Cs": {"name": "Cesium", "atomic_number": 55, "atomic_mass": 132.91},
    "Ba": {"name": "Barium", "atomic_number": 56, "atomic_mass": 137.33},
    "La": {"name": "Lanthanum", "atomic_number": 57, "atomic_mass": 138.91},
    "Ce": {"name": "Cerium", "atomic_number": 58, "atomic_mass": 140.12},
    "Pr": {"name": "Praseodymium", "atomic_number": 59, "atomic_mass": 140.91},
    "Nd": {"name": "Neodymium", "atomic_number": 60, "atomic_mass": 144.24},
    "Pm": {"name": "Promethium", "atomic_number": 61, "atomic_mass": 145},
    "Sm": {"name": "Samarium", "atomic_number": 62, "atomic_mass": 150.36},
    "Eu": {"name": "Europium", "atomic_number": 63, "atomic_mass": 151.96},
    "Gd": {"name": "Gadolinium", "atomic_number": 64, "atomic_mass": 157.25},
    "Tb": {"name": "Terbium", "atomic_number": 65, "atomic_mass": 158.93},
    "Dy": {"name": "Dysprosium", "atomic_number": 66, "atomic_mass": 162.50},
    "Ho": {"name": "Holmium", "atomic_number": 67, "atomic_mass": 164.93},
    "Er": {"name": "Erbium", "atomic_number": 68, "atomic_mass": 167.26},
    "Tm": {"name": "Thulium", "atomic_number": 69, "atomic_mass": 168.93},
    "Yb": {"name": "Ytterbium", "atomic_number": 70, "atomic_mass": 173.05},
    "Lu": {"name": "Lutetium", "atomic_number": 71, "atomic_mass": 174.97},
    "Hf": {"name": "Hafnium", "atomic_number": 72, "atomic_mass": 178.49},
    "Ta": {"name": "Tantalum", "atomic_number": 73, "atomic_mass": 180.95},
    "W": {"name": "Tungsten", "atomic_number": 74, "atomic_mass": 183.84},
    "Re": {"name": "Rhenium", "atomic_number": 75, "atomic_mass": 186.21},
    "Os": {"name": "Osmium", "atomic_number": 76, "atomic_mass": 190.23},
    "Ir": {"name": "Iridium", "atomic_number": 77, "atomic_mass": 192.22},
    "Pt": {"name": "Platinum", "atomic_number": 78, "atomic_mass": 195.08},
    "Au": {"name": "Gold", "atomic_number": 79, "atomic_mass": 196.97},
    "Hg": {"name": "Mercury", "atomic_number": 80, "atomic_mass": 200.59},
    "Tl": {"name": "Thallium", "atomic_number": 81, "atomic_mass": 204.38},
    "Pb": {"name": "Lead", "atomic_number": 82, "atomic_mass": 207.2},
    "Bi": {"name": "Bismuth", "atomic_number": 83, "atomic_mass": 208.98},
    "Po": {"name": "Polonium", "atomic_number": 84, "atomic_mass": 209},
    "At": {"name": "Astatine", "atomic_number": 85, "atomic_mass": 210},
    "Rn": {"name": "Radon", "atomic_number": 86, "atomic_mass": 222},
    "Fr": {"name": "Francium", "atomic_number": 87, "atomic_mass": 223},
    "Ra": {"name": "Radium", "atomic_number": 88, "atomic_mass": 226},
    "Ac": {"name": "Actinium", "atomic_number": 89, "atomic_mass": 227},
    "Th": {"name": "Thorium", "atomic_number": 90, "atomic_mass": 232.04},
    "Pa": {"name": "Protactinium", "atomic_number": 91, "atomic_mass": 231.04},
    "U": {"name": "Uranium", "atomic_number": 92, "atomic_mass": 238.03},
    "Np": {"name": "Neptunium", "atomic_number": 93, "atomic_mass": 237},
    "Pu": {"name": "Plutonium", "atomic_number": 94, "atomic_mass": 244},
    "Am": {"name": "Americium", "atomic_number": 95, "atomic_mass": 243},
    "Cm": {"name": "Curium", "atomic_number": 96, "atomic_mass": 247},
    "Bk": {"name": "Berkelium", "atomic_number": 97, "atomic_mass": 247},
    "Cf": {"name": "Californium", "atomic_number": 98, "atomic_mass": 251},
    "Es": {"name": "Einsteinium", "atomic_number": 99, "atomic_mass": 252},
    "Fm": {"name": "Fermium", "atomic_number": 100, "atomic_mass": 257},
    "Md": {"name": "Mendelevium", "atomic_number": 101, "atomic_mass": 258},
    "No": {"name": "Nobelium", "atomic_number": 102, "atomic_mass": 259},
    "Lr": {"name": "Lawrencium", "atomic_number": 103, "atomic_mass": 266},
    "Rf": {"name": "Rutherfordium", "atomic_number": 104, "atomic_mass": 267},
    "Db": {"name": "Dubnium", "atomic_number": 105, "atomic_mass": 270},
    "Sg": {"name": "Seaborgium", "atomic_number": 106, "atomic_mass": 271},
    "Bh": {"name": "Bohrium", "atomic_number": 107, "atomic_mass": 274},
    "Hs": {"name": "Hassium", "atomic_number": 108, "atomic_mass": 277},
    "Mt": {"name": "Meitnerium", "atomic_number": 109, "atomic_mass": 278},
    "Ds": {"name": "Darmstadtium", "atomic_number": 110, "atomic_mass": 281},
    "Rg": {"name": "Roentgenium", "atomic_number": 111, "atomic_mass": 282},
    "Cn": {"name": "Copernicium", "atomic_number": 112, "atomic_mass": 285},
    "Nh": {"name": "Nihonium", "atomic_number": 113, "atomic_mass": 286},
    "Fl": {"name": "Flerovium", "atomic_number": 114, "atomic_mass": 289},
    "Mc": {"name": "Moscovium", "atomic_number": 115, "atomic_mass": 290},
    "Lv": {"name": "Livermorium", "atomic_number": 116, "atomic_mass": 293},
    "Ts": {"name": "Tennessine", "atomic_number": 117, "atomic_mass": 294},
    "Og": {"name": "Oganesson", "atomic_number": 118, "atomic_mass": 294}
}

def get_element_info(symbol):
    """Restituisce le informazioni di un elemento chimico dato il simbolo."""
    element = periodic_table.get(symbol)
    if element:
        return f"{symbol}: {element['name']} (Atomic Number: {element['atomic_number']}, Atomic Mass: {element['atomic_mass']} g/mol)"
    else:
        return f"Elemento {symbol} non trovato nella tavola periodica."

def calculate_molecular_mass(compound):
    """Calcola la massa molecolare di un composto dato."""
    import re
    pattern = r"([A-Z][a-z]?)(\d*)"
    matches = re.findall(pattern, compound)
    total_mass = 0.0

    for (symbol, count) in matches:
        count = int(count) if count else 1
        element = periodic_table.get(symbol)
        if element:
            total_mass += element["atomic_mass"] * count
        else:
            return f"Errore: Elemento {symbol} non trovato."
    return f"La massa molecolare di {compound} è: {total_mass} g/mol"

if __name__ == "__main__":
    print("Tavola Periodica Interattiva")
    print("1. Cerca un elemento")
    print("2. Calcola la massa molecolare di un composto")
    choice = input("Scegli un'opzione (1 o 2): ")

    if choice == "1":
        symbol = input("Inserisci il simbolo dell'elemento (es. H, O): ")
        print(get_element_info(symbol))
    elif choice == "2":
        compound = input("Inserisci il composto (es. H2O, CO2): ")
        print(calculate_molecular_mass(compound))
    else:
        print("Scelta non valida.")
