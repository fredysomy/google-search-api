from flask import Flask, render_template, redirect, url_for, request, flash
from flask import jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import html5lib
app=Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/api')
def googleapi():
    s=request.args.get('search')
    pg=request.args.get('page',type=int)*10
    d=str(pg)
    dd={}
    l=[]
    url="https://www.google.com/search?q="+s+"&start="+d+"&sa=N&ved=2ahUKEwi7_fTxvcPrAhUy6XMBHahXAuc4ChDy0wN6BAgLEC8&biw=1600&bih=757"
    r=requests.get(url)
    soup=BeautifulSoup(r.content,'html5lib')
    f=soup.find('div',id="main")
    for i in range(1,len(f)-1):
        try:
            g=f.find_all(class_='ZINbbc xpd O9g5cc uUPGi')[i]
            desc=g.find(class_="BNeawe vvjwJb AP7Wnd").getText()
            desc2=g.find(class_="BNeawe s3v9rd AP7Wnd").getText()
            
            try:
                u=g.find('a')['href']
                x=u.split('&')[0].split('?q=')[1]
                gh={"url":x,"desc":desc,"desc2":desc2}
                l=l+[gh]
            except:
                u=g.find('a')['href']
                x=u.split('&')[0]
                gh={"url":x,"desc":desc,"desc2":desc2}
                l=l+[gh]
                
        except:
            print()
    return jsonify(l)
app.run()    