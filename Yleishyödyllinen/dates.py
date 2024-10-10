from datetime import date

def todaysdate():

    today = date.today()
    date1 = today.strftime('%d/%m/%Y')
    print(f"Tänään: {date1}")
todaysdate()

