from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/phones/create/')
def phone_create():
    name = request.args['name']
    phone = request.args['phone']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        INSERT INTO phones
        VALUES ('{name}', '{phone}');
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phones Create'


@app.route('/phones/read/')
def phone_read():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones;
        '''
        cur.execute(sql)
        phones = cur.fetchall()

    finally:
        conn.close()

    return str(phones)


@app.route('/phones/delete/')
def phone_delete():
    phone = request.args['phone']
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        DELETE FROM phones WHERE ContactName == '{phone}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phones Delete'


@app.route('/phones/update/')
def phone_update():
    phone = request.args['phone']
    name = request.args['name']

    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        UPDATE phones
        SET ContactName = '{name}'
        WHERE Phone == '{phone}';
        '''
        cur.execute(sql)
        conn.commit()
    finally:
        conn.close()

    return 'Phones Update'


@app.route('/phones/kyivstar/')
def phone_kyivstar():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones WHERE Phone LIKE '38097%' OR Phone LIKE '38098%' OR Phone LIKE '38068%';
        '''
        cur.execute(sql)
        phones = cur.fetchmany(300)

    finally:
        conn.close()

    return str(phones)


@app.route('/phones/life/')
def phone_life():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones WHERE Phone LIKE'38093%' OR Phone LIKE'38063%';
        '''
        cur.execute(sql)
        phones = cur.fetchmany(300)

    finally:
        conn.close()

    return str(phones)


@app.route('/phones/sort/')
def phone_sort():
    try:
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        sql = f'''
        SELECT * FROM phones ORDER BY ContactName;
        '''
        cur.execute(sql)
        phones = cur.fetchall()

    finally:
        conn.close()

    return str(phones)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)