from flask import Flask, jsonify, request, abort
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data 
customers = []
interactions = []
opportunities = []

# Routes for customers
@app.route('/api/customers', methods=['GET'])
def get_customers():
    return jsonify(customers)

@app.route('/api/customers', methods=['POST'])
def add_customer():
    customer = request.json
    customers.append(customer)
    return jsonify(customer), 201

@app.route('/api/customers/<string:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        abort(404)
    customer.update(request.json)
    return jsonify(customer)

@app.route('/api/customers/<string:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    customer = next((c for c in customers if c['id'] == customer_id), None)
    if not customer:
        abort(404)
    customers.remove(customer)
    return '', 204

# Routes for interactions
@app.route('/api/interactions', methods=['POST'])
def log_interaction():
    interaction = request.json
    interactions.append(interaction)
    return jsonify(interaction), 201

# Routes for opportunities
@app.route('/api/opportunities', methods=['GET'])
def get_opportunities():
    return jsonify(opportunities)

@app.route('/api/opportunities', methods=['POST'])
def add_opportunity():
    opportunity = request.json
    opportunities.append(opportunity)
    return jsonify(opportunity), 201

@app.route('/api/opportunities/<string:opportunity_id>', methods=['PUT'])
def update_opportunity(opportunity_id):
    opportunity = next((o for o in opportunities if o['id'] == opportunity_id), None)
    if not opportunity:
        abort(404)
    opportunity.update(request.json)
    return jsonify(opportunity)

@app.route('/api/opportunities/<string:opportunity_id>', methods=['DELETE'])
def delete_opportunity(opportunity_id):
    opportunity = next((o for o in opportunities if o['id'] == opportunity_id), None)
    if not opportunity:
        abort(404)
    opportunities.remove(opportunity)
    return '', 204











app = Flask(__name__)


customers = []

@app.route('/')
def index():
    return render_template('index.html', customers=customers)

@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        
       
        new_id = len(customers) + 1
        
        
        customers.append({"id": new_id, "name": name, "email": email, "phone": phone})
        
        return redirect(url_for('index'))
    
    return render_template('add_customer.html')

if __name__ == '__main__':
    app.run(debug=True)