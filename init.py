import db

def create_key_table():
    db.cur.execute("""
        CREATE TABLE IF NOT EXISTS keys (
            id TEXT,
            x TEXT,
            y TEXT,
            PRIMARY KEY (id, x)        
        );
    """)

    db.conn.commit()

if __name__ == '__main__':
    db.cur.execute('DROP TABLE IF EXISTS keys')
    create_key_table()

    print('Table created successfully!')
    db.cur.close()
    db.conn.close()