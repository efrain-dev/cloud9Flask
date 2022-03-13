"""
Your module description
comentarios múltiples
"""

#comentario de una línea

from flask import Flask, render_template,request ,url_for
import calculos

umg = Flask(__name__)




@umg.route("/",methods=['POST','GET'])
def home():
    print( calculos.result())
    return render_template('home.html',resultado= calculos.result())

    
if __name__ == '__main__':
    umg.run(host='0.0.0.0', port=5000, debug=True)


