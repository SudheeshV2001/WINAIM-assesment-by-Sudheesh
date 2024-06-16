import sqlite3
from datetime import datetime

DATABASE = 'crm.db'

def connect_db():
    return sqlite3.connect(DATABASE)

# Function to add a new customer
def add_customer(first_name, last_name, email, phone, company_name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO customers (first_name, last_name, email, phone, company_name) 
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, email, phone, company_name))
    conn.commit()
    conn.close()

# Function to edit an existing customer
def edit_customer(customer_id, first_name, last_name, email, phone, company_name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        UPDATE customers
        SET first_name = ?, last_name = ?, email = ?, phone = ?, company_name = ?, updated_at = ?
        WHERE customer_id = ?
    ''', (first_name, last_name, email, phone, company_name, datetime.now(), customer_id))
    conn.commit()
    conn.close()

# Function to delete a customer
def delete_customer(customer_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM customers WHERE customer_id = ?', (customer_id,))
    conn.commit()
    conn.close()

# Function to view all customers
def view_customers():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM customers')
    customers = c.fetchall()
    conn.close()
    return customers

# Function to log an interaction
def log_interaction(customer_id, interaction_type, interaction_date, notes):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO interactions (customer_id, interaction_type, interaction_date, notes) 
        VALUES (?, ?, ?, ?)
    ''', (customer_id, interaction_type, interaction_date, notes))
    conn.commit()
    conn.close()

# Function to add a new opportunity
def add_opportunity(customer_id, title, description, stage, amount):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        INSERT INTO opportunities (customer_id, title, description, stage, amount) 
        VALUES (?, ?, ?, ?, ?)
    ''', (customer_id, title, description, stage, amount))
    conn.commit()
    conn.close()

# Function to update an opportunity
def update_opportunity(opportunity_id, customer_id, title, description, stage, amount):
    conn = connect_db()
    c = conn.cursor()
    c.execute('''
        UPDATE opportunities
        SET customer_id = ?, title = ?, description = ?, stage = ?, amount = ?, updated_at = ?
        WHERE opportunity_id = ?
    ''', (customer_id, title, description, stage, amount, datetime.now(), opportunity_id))
    conn.commit()
    conn.close()

# Function to view all opportunities
def view_opportunities():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM opportunities')
    opportunities = c.fetchall()
    conn.close()
    return opportunities