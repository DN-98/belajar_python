
# ? membuat objek/class Temperature Contverter
class TempContverter :
    def celciusToKelvin(self, celcius):
        '''
            Celcius to Kelvin Converter
                Parameters:
                    celcius(float) : A celcius value 
                Returns:
                    kelvin(float) : result of celcius to kelvin converter
        '''
        print(f"Converting {celcius} celcius to Kelvin . . . \n")
        kelvin = celcius + 273.15
        return kelvin

    def celciusToFahrenheit(self, celcius):
        '''
            Celcius to Fahrenheit Converter
                Parameters:
                    celcius(float) : A celcius value 
                Returns:
                    fahrenheit(float) : result of celcius to fahrenheit converter
        '''
        print(f"Converting {celcius} celcius to Fahrenheit . . . \n")
        fahrenheit = celcius * 9/5 + 32
        return fahrenheit

    def kelvinToCelcius(self, kelvin):
        '''
            Kelvin to Celcius Converter
                Parameters:
                    kelvin(float) : A kelvin value 
                Returns:
                    celcius(float) : result of kelvin to celcius converter
        '''
        print(f"Converting {kelvin} kelvin to Celcius . . . \n")
        celcius = kelvin - 273.15
        return celcius

    def kelvinToFahrenheit(self, kelvin):
        '''
            Kelvin to Fahrenheit Converter
                Parameters:
                    kelvin(float) : A kelvin value 
                Returns:
                    fahrenheit(float) : result of kelvin to fahrenheit converter
        '''
        print(f"Converting {kelvin} kelvin to Fahrenheit . . . \n")
        fahrenheit = kelvin  * 9/5 - 459.67
        return fahrenheit

    def fahrenheitToCelcius(self, fahrenheit):
        '''
            Fahrenheit to Celcius Converter
                Parameters:
                    fahrenheit(float) : A fahrenheit value 
                Returns:
                    celcius(float) : result of fahrenheit to celcius converter
        '''
        print(f"Converting {fahrenheit} fahrenheit to Celcius . . . \n")
        celcius = (fahrenheit - 32) * 5/9
        return celcius

    def fahrenheitToKelvin(self, fahrenheit):
        '''
            Fahrenheit to Kelvin Converter
                Parameters:
                    fahrenheit(float) : A fahrenheit value 
                Returns:
                    kelvin(float) : result of fahrenheit to kelvin converter
        '''
        print(f"Converting {fahrenheit} fahrenheit to Kelvin . . . \n")
        kelvin = (fahrenheit + 459.67) * 5/9
        return kelvin
    
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
                case 1 : return tempConv.celciusToFahrenheit(val)
                case 2 : return tempConv.celciusToKelvin(val)
                case default:
                    return  "Invalid Reqest"
        case 2:
            # ? melakukan matching sesuai dengan jenis converter (n) untuk input suhu fahrenheit
            match n:
                case 1 : return  tempConv.fahrenheitToCelcius(val)
                case 2 : return  tempConv.fahrenheitToKelvin(val)
                case default:
                    return  "Invalid Reqest"
        case 3:
            # ? melakukan matching sesuai dengan jenis converter (n) untuk input suhu kelvin
            match n:
                case 1 : return  tempConv.kelvinToCelcius(val)
                case 2 : return  tempConv.kelvinToFahrenheit(val)
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
    m = int(input("\nMasukan pilihan: "))
    # ? melakukan pengecekan kesesuaian input pertama (jenis input suhu)
    while((m <= 0 or m > 4)):
        print("Invalid Input")
        print("Berikut tipe suhu yang dapat dipilih:")
        for i in range(0, len(ket)):
            print(f"{i+1}. {ket[i][0]}")
            m = int(input("\nMasukan pilihan: "))
    # ? melakukan pengecekan pilihan exit
    if(m == 4):
        break

    while True:
        # ? generate menu kedua (konverter)
        print("Berikut converter yang dapat dipilih:")
        for i in range(0, len(ket[m-1])):
            print(f"{i+1}. {ket[m-1][1][i]}")
        print("3. exit")
        # ? input untuk jenis konverter
        n = int(input("\nMasukan pilihan: "))

        # ? melakukan pengecekan kesesuaian input kedua (jenis konverter)
        while((n <= 0 or n > 3)):
            print("Invalid Input")
            print("Berikut converter yang dapat dipilih:")
            for i in range(0, len(ket[m-1])):
                print(f"{i+1}. {ket[m-1][1][i]}")
            print("3. exit")
            n = int(input("\nMasukan pilihan: "))
        if(n == 3):
            break
        
        # ? input untuk value
        val = int(input(f"\nMasukan nilai suhu {ket[m-1][0]}: "))
        print(menu(m, n, val))

        input("\nPress enter to continue . .")

