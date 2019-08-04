from application.Hello import HelloWorld
from application.App import service

if __name__ == '__main__':
    service.run(host='0.0.0.0', port=5000, use_reloader=True)