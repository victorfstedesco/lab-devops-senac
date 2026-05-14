from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    # HTML com CSS embutido para um visual moderno
    return """
    <html>
    <head>
        <title>Lab DevOps Senac</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }

            .card {
                background: white;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                text-align: center;
            }

            h1 {
                color: #003366;
            }

            p {
                color: #666;
                font-size: 1.2rem;
            }

            .status {
                color: white;
                background: #28a745;
                padding: 5px 15px;
                border-radius: 20px;
                font-size: 0.9rem;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="card">
            <h1>SISTEMA ONLINE V1.0</h1>
            <p>Laboratório DevOps - Senac</p>
            <span class="status">
                DEPLOY AUTOMÁTICO VIA GITHUB ACTIONS
            </span>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)