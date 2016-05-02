# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template, make_response

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag8 = Blueprint('ag8', __name__, url_prefix='/ag8', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@ag8.route('/task1All')
def task1():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>

</head>
<body>

<script>
window.onload=function(){
brython(1);
}
</script>

<canvas id="plotarea" width="700" height="800"></canvas>

<script type="text/python">
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-250, -250, 500, 500) 

# 決定要不要畫座標軸線
cgo.drawAxes(0, 400, 0, 400, {
    "strokeColor":"#aaaaaa",
    "fillColor": "#aaaaaa",
    "xTickInterval": 20,
    "xLabelInterval": 20,
    "yTickInterval": 20,
    "yLabelInterval": 20})
        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 0, 0, 0, 0, 0, 6.8397, -1.4894 \
                     A 0, 0, 0, 0, 0, 6.8397, -18.511 \
                     A 0, 0, 0, 0, 0, -6.8397, -18.511 \
                     A 0, 0, 0, 0, 0, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })


    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 5, rot)

O(0, 0, 0, 0, 0,"lightyellow",True, 4)
</script>
'''
    return outstring



@ag8.route('/task1All_2')
def task1All_2():
    return "</body></html>"

@ag8.route('/task1All_3')
def task1All_3():
    outstring = task1All()
    outstring += "<script type='text/python' src='http://0426-2014w11.rhcloud.com/ag8_40323131/task1'></script>"
    outstring += "<script type='text/python' src='http://0426-2014w11.rhcloud.com/ag8_40323137/task1'></script>"
    outstring += "<script type='text/python' src='http://0428-40323143.rhcloud.com/ag8_40323143/task1'></script>"
    outstring += "<script type='text/python' src='http://0426-2014w11.rhcloud.com/ag8_40323145/task1'></script>"
    outstring += "<script type='text/python' src='http://042854-eerjthki.rhcloud.com/ag8_40323154/task1'></script>"
    outstring += "<script type='text/python' src='http://0426-2014w11.rhcloud.com/ag8_40323123/task1'></script>"
    outstring += task1All_2()
    return outstring
    

    
    
