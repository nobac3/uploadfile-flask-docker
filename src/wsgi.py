from s3_uploader.views import app as application

if __name__ == '__main__':
    application.run(debug=True, host='0.0.0.0', port="8030")
