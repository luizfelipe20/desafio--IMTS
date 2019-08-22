from app import create_app

HOST = '0.0.0.0'
PORT = 5000

app = create_app()

if __name__ == '__main__':    
    app.run(host=HOST, port=PORT)