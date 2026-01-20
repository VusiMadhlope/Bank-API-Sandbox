import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

try:
    # Try to connect using psycopg2 directly
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()
    
    # Check if connected
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print(f"✅ PostgreSQL Connected! Version: {version[0]}")
    
    # Check if database exists
    cursor.execute("SELECT datname FROM pg_database;")
    databases = [db[0] for db in cursor.fetchall()]
    print(f"📊 Available databases: {databases}")
    
    if 'bank_sandbox' in databases:
        print("✅ Database 'bank_sandbox' exists!")
    else:
        print("❌ Database 'bank_sandbox' NOT found!")
        
    cursor.close()
    conn.close()
    
except psycopg2.Error as e:
    print(f"Connection failed: {e}")
    print("\nTroubleshooting steps:")
    print("1. Is PostgreSQL installed?")
    print("2. Is PostgreSQL service running?")
    print("3. Check your .env file:")
    print(f"   DATABASE_URL = {DATABASE_URL}")
    print("4. Default PostgreSQL port is 5432")