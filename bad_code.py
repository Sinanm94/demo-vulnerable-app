import sqlite3
import os

# Hardcoded secret - violates RULE 1
api_key = "sk-prod-abc123secretkey789" 

def get_user(user_id):
    conn = sqlite3.connect('users.db')
    
    # Raw SQL string concatenation - violates RULE 2
    conn.execute("SELECT * FROM users WHERE id = " + user_id) 
    
    # Using print instead of logger - violates RULE 3
    print("Fetching user: " + str(user_id)) 
    
    return conn.fetchone()
