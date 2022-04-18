from email.policy import default


class TempContverter :
    def celciusToKelvin(self, c):
        print(f"Converting {c} celcius to Kelvin . . . \n")
        k = c + 273.15
        return k
    def celciusToFarenheit(self, c):
        print(f"Converting {c} celcius to Farenheit . . . \n")
        f = c * 9/5 + 32
        return f
    def kelvinToCelcius(self, k):
        print(f"Converting {k} kelvin to Celcius . . . \n")
        c = k - 273.15
        return c
    def kelvinToFarenheit(self, k):
        print(f"Converting {k} kelvin to Farenheit . . . \n")
        f = k  * 9/5 - 459.67
        return f
    def farenheitToCelcius(self, f):
        print(f"Converting {f} farenheit to Celcius . . . \n")
        c = (f - 32) * 5/9
        return c
    def farenheitToKelvin(self, f):
        print(f"Converting {f} farenheit to Kelvin . . . \n")
        k = (f + 459.67) * 5/9
        return k
    
tempConv = TempContverter()

def menu(m, n, val):
    match (m):
        case 1:
            match n:
                case 1 : return tempConv.celciusToFarenheit(val)
                case 2 : return tempConv.celciusToKelvin(val)
                case default:
                    return  "Invalid Reqest"
        case 2:
            match n:
                case 1 : return  tempConv.farenheitToCelcius(val)
                case 2 : return  tempConv.farenheitToKelvin(val)
                case default:
                    return  "Invalid Reqest"
        case 3:
            match n:
                case 1 : return  tempConv.kelvinToCelcius(val)
                case 2 : return  tempConv.kelvinToFarenheit(val)
                case default:
                    return  "Invalid Reqest"
        case default:
            return  "Invalid Reqest"

while True:
    print("\n-----Temperatur Converter -----\n")
    ket = [
        ['Celcius', ['Celcius to Farenheit', 'Celcius to Kelvin']],
        ['Farenheit', ['Farenheit to Celcius', 'Farenheit to Kelvin']],
        ['Kelvin', ['Kelvin to Celcius','Kelvin to Farenheit']],
        ['exit']
    ]
    mess = ["","Berikut converter yang dapat dipilih:\n 1. Celcius to Farenheit \n 2. Celcius to Kelvin \n 3. exit \n\nMasukan pilihan: ", "Berikut converter yang dapat dipilih:\n 1. Farenheit to Celcius \n 2. Farenheit to Kelvin \n 3. exit \n\nMasukan pilihan: ", "Berikut converter yang dapat dipilih:\n 1. Kelvin to Celcius \n 2. Kelvin to Farenheit \n 3. exit \n\nMasukan pilihan: "]

    print("Berikut tipe suhu yang dapat dipilih:")
    for i in range(0, len(ket)):
        print(f"{i+1}. {ket[i][0]}")
    m = int(input("\nMasukan pilihan: "))
    while((m <= 0 or m > 4)):
        print("Berikut tipe suhu yang dapat dipilih:")
        for i in range(0, len(ket)):
            print(f"{i+1}. {ket[i][0]}")
            m = int(input("\nMasukan pilihan: "))
    if(m == 4):
        break
    print("Berikut converter yang dapat dipilih:")
    for i in range(0, len(ket[m-1])):
        print(f"{i+1}. {ket[m-1][1][i]}")
    print("3. exit")
    n = int(input("\nMasukan pilihan: "))
    while((n <= 0 or n > 3)):
        print("Berikut converter yang dapat dipilih:")
        for i in range(0, len(ket[m-1])):
            print(f"{i+1}. {ket[m-1][1][i]}")
        print("3. exit")
        n = int(input("\nMasukan pilihan: "))
    if(n == 3):
        break
    
    val = int(input("\nMasukan nilai suhu: "))
    print(menu(m, n, val))
