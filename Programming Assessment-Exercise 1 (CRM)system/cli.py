def cli():
    while True:
        print("1. Add Customer")
        print("2. Edit Customer")
        print("3. Delete Customer")
        print("4. View Customers")
        print("5. Log Interaction")
        print("6. Add Opportunity")
        print("7. Update Opportunity")
        print("8. View Opportunities")
        print("9. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            company_name = input("Company Name: ")
            add_customer(first_name, last_name, email, phone, company_name)
        
        elif choice == '2':
            customer_id = int(input("Customer ID: "))
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            company_name = input("Company Name: ")
            edit_customer(customer_id, first_name, last_name, email, phone, company_name)
        
        elif choice == '3':
            customer_id = int(input("Customer ID: "))
            delete_customer(customer_id)
        
        elif choice == '4':
            customers = view_customers()
            for customer in customers:
                print(customer)
        
        elif choice == '5':
            customer_id = int(input("Customer ID: "))
            interaction_type = input("Interaction Type: ")
            interaction_date = input("Interaction Date (YYYY-MM-DD): ")
            notes = input("Notes: ")
            log_interaction(customer_id, interaction_type, interaction_date, notes)
        
        elif choice == '6':
            customer_id = int(input("Customer ID: "))
            title = input("Title: ")
            description = input("Description: ")
            stage = input("Stage: ")
            amount = float(input("Amount: "))
            add_opportunity(customer_id, title, description, stage, amount)
        
        elif choice == '7':
            opportunity_id = int(input("Opportunity ID: "))
            customer_id = int(input("Customer ID: "))
            title = input("Title: ")
            description = input("Description: ")
            stage = input("Stage: ")
            amount = float(input("Amount: "))
            update_opportunity(opportunity_id, customer_id, title, description, stage, amount)
        
        elif choice == '8':
            opportunities = view_opportunities()
            for opportunity in opportunities:
                print(opportunity)
        
        elif choice == '9':
            break
        
        else:
            print("Invalid choice. Please try again.")

if _name_ == '_main_':
    cli()