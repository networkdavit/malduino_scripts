from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        data = request.data.decode('utf-8') 
        print("Received Data: ", data)  

        with open("received_sysinfo.txt", "w") as f:
            f.write(data) 

        return "Data received successfully!", 200
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 
