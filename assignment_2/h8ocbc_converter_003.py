
# ? membuat objek/class Temperature Contverter
class TempContverter :
    def celcius_kelvin(self, temp_type, val):
        '''
            Celcius to Kelvin Converter
                Parameters:
                    temp_type(str)  : string value temperature input type
                    val(float)      : A celcius or kelvin value 
                Returns:
                    result(float) : result of celcius-kelvin or kelvin-celcius converter
        '''
        match (temp_type):
            case "c":
                print(f"Converting {val} celcius to Kelvin . . . \n")
                result = val + 273.15
            case "k":
                print(f"Converting {val} kelvin to Celcius . . . \n")
                result = val - 273.15
        return result
    
    def toFahrenherit(self, temp_type, val):
        '''
            Temperature to Fahrenheit Converter
                Parameters:
                    temp_type(str)  : string value temperature input type
                    val(float)      : A celcius or kelvin value 
                Returns:
                    result(float) : result of celcius-fahrenheit or kelvin-fahrenheit converter
        '''
        match (temp_type):
            case "c":
                print(f"Converting {val} celcius to Fahrenheit . . . \n")
                result = val * 9/5 + 32
            case "k":
                print(f"Converting {val} kelvin to Fahrenheit . . . \n")
                result = val  * 9/5 - 459.67
        return result
    
    def fromFahrenherit(self, temp_type, val):
        '''
            Fahrenheit to Temperature Converter
                Parameters:
                    temp_type(str)  : string value temperature target type
                    val(float)      : A fahrenheit value
                Returns:
                    result(float) : result of fahrenheit-temperature converter
        '''
        match (temp_type):
            case "c":
                print(f"Converting {val} Fahrenheit to celcius. . . \n")
                result = (val - 32) * 5/9
            case "k":
                print(f"Converting {val} Fahrenheit to kelvin . . . \n")
                result = (val + 459.67) * 5/9
        return result
    
# ? menerapkan object TempConverter ke dalam variable tempConv
tempConv = TempContverter()

# ? fungsi menu sebagai pengarah ke fungsi converter yang dipilih user
def menu(m, n, val):
    '''
        fungsi menu untuk selector input dan converter
            Parameters:
                m(int) : value[1-3] to select Temperature Input type
                n(int) : value[1-2] to select Temperature Converter type
                val(float) : value of convertion target Input Temperature 
            Returns:
                tempConv : returning the return value of selected function of tempConv (TempConverter)
                or
                "invalid Request" : when m and n value invalid
    '''
    # ? melakukan matching sesuai dengan jenis input suhu (m) yang dipilih user
    match (m):
        case 1:
            # ? melakukan matching sesuai dengan jenis converter (n) untuk input suhu celcius
            match n:
                case 1 : return tempConv.toFahrenherit("c",val)
                case 2 : return tempConv.celcius_kelvin("c",val)
                case default:
                    return  "Invalid Reqest"
        case 2:
            # ? melakukan matching sesuai dengan jenis converter (n) untuk input suhu fahrenheit
            match n:
                case 1 : return  tempConv.fromFahrenherit("c", val)
                case 2 : return  tempConv.fromFahrenherit("k", val)
                case default:
                    return  "Invalid Reqest"
        case 3:
            # ? melakukan matching sesuai dengan jenis converter (n) untuk input suhu kelvin
            match n:
                case 1 : return  tempConv.celcius_kelvin("k", val)
                case 2 : return  tempConv.toFahrenherit("k", val)
                case default:
                    return  "Invalid Reqest"
        case default:
            return  "Invalid Reqest"

while True:
    print("\n-----Temperatur Converter -----\n")

    # ? list string untuk pilihan menu
    ket = [
        ['Celcius', ['Celcius to Farenheit', 'Celcius to Kelvin']],
        ['Farenheit', ['Farenheit to Celcius', 'Farenheit to Kelvin']],
        ['Kelvin', ['Kelvin to Celcius','Kelvin to Farenheit']],
        ['exit']
    ]

    # ? generate menu pertama (input suhu)
    print("Berikut tipe suhu yang dapat dipilih:")
    for i in range(0, len(ket)):
        print(f"{i+1}. {ket[i][0]}")

    # ? input untuk jenis input suhu
    m = int(input("\nMasukan angka pilihan[1-4]: "))
    # ? melakukan pengecekan kesesuaian input pertama (jenis input suhu)
    while((m <= 0 or m > 4)):
        print("\nInvalid Input\n")
        print("Berikut tipe suhu yang dapat dipilih:")
        for i in range(0, len(ket)):
            print(f"{i+1}. {ket[i][0]}")
        m = int(input("\nMasukan angka pilihan[1-4]: "))

    # ? melakukan pengecekan pilihan exit
    if(m == 4):
        break

    while True:
        # ? generate menu kedua (konverter)
        print("Berikut converter yang dapat dipilih:")
        for i in range(0, len(ket[m-1])):
            print(f"{i+1}. {ket[m-1][1][i]}")
        print("3. back to main")
        # ? input untuk jenis konverter
        n = int(input("\nMasukan angka pilihan[1-3]: "))

        # ? melakukan pengecekan kesesuaian input kedua (jenis konverter)
        while((n <= 0 or n > 3)):
            print("\nInvalid Input\n")
            print("Berikut converter yang dapat dipilih:")
            for i in range(0, len(ket[m-1])):
                print(f"{i+1}. {ket[m-1][1][i]}")
            print("3. back to main")
            n = int(input("\nMasukan angka pilihan [1-3]: "))
        if(n == 3):
            break
        
        # ? input untuk value
        val = int(input(f"\nMasukan nilai suhu {ket[m-1][0]}: "))
        print(menu(m, n, val))

        input("\nPress enter to continue . .")

