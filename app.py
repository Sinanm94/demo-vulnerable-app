import sqlite3

# Hardcoded secret - violates no_hardcoded_secrets rule
api_key = "sk-prod-abc123secretkey789"

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    # Raw SQL - violates no_raw_sql rule  
    conn.execute("SELECT * FROM users WHERE id = " + user_id)
    # Print instead of logger - violates no_print_statements rule
    print("Fetching user: " + str(user_id))
    return conn.fetchone()

def process_request(request):
    # No input sanitization - violates sanitize_inputs rule
    data = request.args.get('user_id')
    return get_user(data)
    #IBM bob
# BobGuard Demo Trigger
