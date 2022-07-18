import sqlite3

conn = sqlite3.connect('users.db')
cur = conn.cursor()

cur.execute('''
CREATE TABLE phones
(ContactName varchar(255), Phone varchar(20) UNIQUE)
''')



# user_name, email

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()