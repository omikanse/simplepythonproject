from tkinter import *
import pandas as pd
import requests
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import ttk


# Load the Excel file
df = pd.read_excel('car_data.xlsx')
root = Tk()
root.title("CarProject")
root.config(bg="#00FFFF")
root.geometry("1500x700")

Label(root, text="Mercedes ShowRoom", bg="black", fg="white",font=50).place(x=50, y=100)


def display_image(url):
    response = requests.get(url)
    image_data = response.content
    image = Image.open(BytesIO(image_data))
    image = image.resize((250, 200))  # Adjust the size as per your requirement
    photo = ImageTk.PhotoImage(image)
    result_label2.config(image=photo)
    result_label2.image = photo
    
    
def car():
    # Specify the column names
    column_name = 'Seating Capacity'
    column_name2 = 'Budget'
    seating_capacity = int(name.get())  # Get the entered seating capacity from the Entry widget
    budget = int(account.get())  # Get the entered budget from the Entry widget
    
    for value in df[column_name]:
        if 4== seating_capacity:
            if 6==budget:
                result_label.config(text='Tata Punch')
                url = 'https://imgd.aeplcdn.com/664x374/n/cw/ec/39015/punch-exterior-right-front-three-quarter-2.jpeg?isig=0&q=75'  # Replace with your desired image URL
                display_image(url)
                row_index = 1  # Specify the row index from which you want to display the value
                column_name = 'Details'  # Replace with the desired column name
                value = df.at[row_index, column_name]
                result_label3.config(text=value)
                continue
            if 7==budget:
                result_label.config(text='Tata Altroz')
                url = 'https://imgd.aeplcdn.com/272x153/n/cw/ec/32597/altroz-exterior-right-front-three-quarter-79.jpeg?isig=0&q=75'  # Replace with your desired image URL
                display_image(url)
                row_index = 2  # Specify the row index from which you want to display the value
                column_name = 'Details'  # Replace with the desired column name
                value = df.at[row_index, column_name]
                result_label3.config(text=value)
                break
            if 8==budget:
                result_label.config(text='Tata Nexon')
                url = 'https://imgd.aeplcdn.com/272x153/n/cw/ec/41645/tata-nexon-right-front-three-quarter3.jpeg?q=75'  # Replace with your desired image URL
                display_image(url)
                row_index = 0  # Specify the row index from which you want to display the value
                column_name = 'Details'  # Replace with the desired column name
                value = df.at[row_index, column_name]
                result_label3.config(text=value)
                break
            if 10==budget:
                result_label.config(text='Mahindra Thar')
                url = 'https://imgd.aeplcdn.com/272x153/n/cw/ec/40087/thar-exterior-right-front-three-quarter-11.jpeg?q=75'  # Replace with your desired image URL
                display_image(url)
                row_index = 7  # Specify the row index from which you want to display the value
                column_name = 'Details'  # Replace with the desired column name
                value = df.at[row_index, column_name]
                result_label3.config(text=value)
                break
            if 13==budget:
                result_label.config(text='Mahindra Scorpio N')
                url = 'https://imgd.aeplcdn.com/272x153/n/cw/ec/40432/scorpio-n-exterior-right-front-three-quarter-15.jpeg?isig=0&q=75'  # Replace with your desired image URL
                display_image(url)
                row_index = 6  # Specify the row index from which you want to display the value
                column_name = 'Details'  # Replace with the desired column name
                value = df.at[row_index, column_name]
                result_label3.config(text=value)
                break
            if 15==budget:
                result_label.config(text='Tata Harrier')
                url = 'https://imgd.aeplcdn.com/272x153/n/cw/ec/142739/harrier-exterior-right-front-three-quarter-2.jpeg?isig=0&q=75'  # Replace with your desired image URL
                display_image(url)
                row_index = 3  # Specify the row index from which you want to display the value
                column_name = 'Details'  # Replace with the desired column name
                value = df.at[row_index, column_name]
                result_label3.config(text=value)
                break
        if 5== seating_capacity:
                if 11==budget:
                    result_label.config(text='Mahindra XUV300 TurboSport')
                    url = 'https://imgd.aeplcdn.com/272x153/n/cw/ec/131907/xuv300-turbosport-exterior-right-front-three-quarter-8.jpeg?isig=0&q=75'  # Replace with your desired image URL
                    display_image(url)
                    row_index = 5  # Specify the row index from which you want to display the value
                    column_name = 'Details'  # Replace with the desired column name
                    value = df.at[row_index, column_name]
                    result_label3.config(text=value)
                    break
        if 6== seating_capacity:
                if 13==budget:
                    result_label.config(text='Mahindra Scorpio')
                    url = 'https://imgd.aeplcdn.com/272x153/n/cw/ec/128413/scorpio-exterior-right-front-three-quarter-46.jpeg?isig=0&q=75'  # Replace with your desired image URL
                    display_image(url)
                    row_index = 4  # Specify the row index from which you want to display the value
                    column_name = 'Details'  # Replace with the desired column name
                    value = df.at[row_index, column_name]
                    result_label3.config(text=value)
                    break
        else:
            result_label.config(text='No condition matched.')

Label(root, text="Add Seating capacity 4,5,6:", fg="white", bg="#000000", font=15).place(x=50, y=170)
name = Entry(root, width=13, font="arial 15")
name.place(x=50, y=200)


Label(root, text="Add Budget 6,7,8,10,11,13,15 Lakh:", fg="white", bg="#000000", font=15).place(x=50, y=260)
account = Entry(root, width=13, font="arial 15")
account.place(x=50, y=290)

result_label = Label(root, text="", fg="black", bg="#FFFFFF",font=15)
result_label.place(x=850, y=100)

result_label2 = Label(root, text="", fg="black",bg="#FFFFFF", font=15)
result_label2.place(x=850, y=140)

result_label3 = Label(root, text="", fg="black", bg="#FFFFFF",font=15)
result_label3.place(x=850, y=350)

Button(root, text="Show", width=30, height=2, bg="black", fg="white", command=car).place(x=50, y=360)

root.mainloop()





