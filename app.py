from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="Discount: ",display2="Loan Payment: ", pageTitle='Loan Calculator')


@app.route('/loan', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
      form = request.form
      try:
          LoanAmount  = int(form['A'])
          Number_of_periodic_payments = int(form['N'])
          Periodic_interest_rate = float(form['I'])
          Discount =   round(((( 1 + Periodic_interest_rate ) **Number_of_periodic_payments ) - 1 ) / ( Periodic_interest_rate* ( 1+ Periodic_interest_rate) **Number_of_periodic_payments),2)
          Loan_Payment = round(LoanAmount/Discount,2)
          return render_template('index.html', display=(f'Discount: {Discount}'),display2=(f'Loan Payment: ${Loan_Payment}'), pageTitle='Loan Calculator')


      except ValueError:
          return render_template('index.html', display="Please enter numbers.", pageTitle='Loan Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
