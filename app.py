from flask import Flask
from flask import render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', display="", pageTitle='Loan Calculator')


@app.route('/loan', methods=['GET', 'POST'])
def addition():
    if request.method == 'POST':
      form = request.form
      try:
          LoanAmount  = int(form['A'])
          Number_of_periodic_payments = int(form['N'])
          Periodic_interest_rate = float(form['I'])
          Discount =   ((( 1 + Periodic_interest_rate ) **Number_of_periodic_payments ) - 1 ) / ( Periodic_interest_rate* ( 1+ Periodic_interest_rate) **Number_of_periodic_payments)
          Loan_Payment = LoanAmount/Discount
          return render_template('index.html', display=(('Discount:',Discount),('Loan Payment:',Loan_Payment)), pageTitle='My Calculator')


      except ValueError:
          return render_template('index.html', display="Please enter two integers.", pageTitle='Loan Calculator')

    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)
