
import json
from alright import WhatsApp
from flask import Flask, request, jsonify

messenger = WhatsApp()
app = Flask(__name__)

@app.route('/send',methods=['POST'])
def send():
    notif = ''
    no_hp = request.form['no_hp']
    if no_hp:
        messenger.find_user(no_hp)
        messenger.send_message("coba bot2")
        notif = 'message sent'
        return notif
    else :
        notif = 'failed get number'
        return notif


@app.route('/sendall',methods=['POST'])
def sendall():
    dataJson = request.json
    # dataJson = ['6289656123491','6282185474782','6287877354076']
    if dataJson :
        for no_hp in dataJson:
            messenger.find_user(no_hp)
            messenger.send_message("tes whatsapp bot coy(last)")
    return 'ok'
if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=5000)
   

    