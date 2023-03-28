from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

import pandas as pd

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']

        # Read the existing data from the Excel file
        try:
            df = pd.read_excel('data.xlsx')
        except:
            df = pd.DataFrame(columns=['Name', 'Email', 'Age'])

        # Append the new data to the existing data
        new_data = {'Name': name, 'Email': email, 'Age': age}
        df = df.append(new_data, ignore_index=True)

        # Save the data to the Excel file
        df.to_excel('data.xlsx', index=False)

        return 'Thank you for submitting the form!'
    else:
        # Render the form template
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
