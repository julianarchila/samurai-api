from flask import json, request, Flask
import mysql.connector
import os
from dotenv import load_dotenv
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_database = os.getenv('DB_NAME')
db_port = int(os.getenv('PORT_DB') or 3306)

def get_db_connection():
    conn = mysql.connector.connect(
        host=db_host,
        user=db_user,
        passwd=db_pass,
        port=db_port,
        database=db_database
    )
    return conn

PREFIX = "/api/bakugan"

@app.route(PREFIX + '/')
def getHolaMundo():
    return json.dumps({"message": 'Hola Mundo Python, un Saludo desde el Microservicio que conecta con la Bakugan-DB!'}), 200


@app.route(PREFIX + '/get-all-bakugan')
def get_all_bakugans():
    con = get_db_connection()

    cursor = con.cursor()
    cursor.execute("SELECT * FROM bakugan")
    rows = cursor.fetchall()
    column_names = [desc[0] for desc in cursor.description or []]
    cursor.close()
    res = json.dumps([dict(zip(column_names, row)) for row in rows])

    return res


@app.route(PREFIX + '/insert-bakugan', methods=['POST'])
def insertbakugan():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud
    name = data.get('name')
    type_primary = data.get('type_primary')
    type_secondary = data.get('type_secondary')

    if not name or not type_primary:
        return json.dumps({"error": "Faltan campos requeridos"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''INSERT INTO bakugan (name, type_primary, type_secondary)
                          VALUES (%s, %s, %s)''', (name, type_primary, type_secondary))
        conn.commit()
        conn.close()
        return json.dumps({"message": "Bakugan insertado con éxito"}), 201
    except mysql.connector.Error as e:
        conn.close()
        return json.dumps({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


@app.route(PREFIX + '/delete-bakugan/<int:id>', methods=['DELETE'])
def deletebakugan(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('DELETE FROM bakugan WHERE id = ?', (id,))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return json.dumps({"error": "Bakugan no encontrado"}), 404

        conn.close()
        return json.dumps({"message": "Bakugan eliminado con éxito"}), 200
    except mysql.connector.Error as e:
        conn.close()
        return json.dumps({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()
