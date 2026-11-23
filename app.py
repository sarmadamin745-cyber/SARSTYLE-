from flask import Flask, jsonify 

app = Flask (__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome To SARSTYLE</h1>
    <p>My first deployed Flask Website </p>
    <a href="/products">Watch Our Products</a>
    """
    
@app.route("/products")
def products():
    return """
    <h1>SARSTYLE Products</h1>
    <p>watch - Rs. 5000</p>
    <p>Wallet - Rs. 2500</p>"""
    
if __name__=="__main__":
    app.run
    