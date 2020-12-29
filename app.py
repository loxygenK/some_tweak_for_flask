from config.application import app
from utils.endpoint_loader import load_endpoints

if __name__ == '__main__':
    load_endpoints()
    app.run()
