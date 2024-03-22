from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wifi_details')
def wifi_details():
    from wifi import get_wifi_details   
    wifi_details = get_wifi_details()
    return render_template('wifi_details.html', wifi_details=wifi_details)

@app.route('/network_speed')
def network_speed():
    from wifi import get_network_speed
    speed_details = get_network_speed()
    return render_template('network_speed.html', speed_details=speed_details)

@app.route('/network_info')
def network_info():
    from wifi import get_network_info
    network_info = get_network_info()
    return render_template('network_info.html', network_info=network_info)

if __name__ == '__main__':
    app.run(debug=True)

