from flask import Flask
import chalk

app = Flask(__name__)

if __name__ == '__main__':
    print(chalk.yellow("Server on port 5000"))
    app.run(debug=True, port=3000)
