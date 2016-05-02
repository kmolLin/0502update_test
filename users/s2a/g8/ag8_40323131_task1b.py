
# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag8_40323131b = Blueprint('ag8_40323131b', __name__, url_prefix='/ag8_40323131b', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@ag8_40323131b.route('/task1b')
def task1():
    outstring = '''
from javascript import JSConstructor
from browser import window
import math

cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")

cgo.setWorldCoords(-300
, -250, 500, 500) 

# 決定要不要畫座標軸線

        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })

deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M -6.8397, -1.4894 \
                     A 7, 7, 0, 1, 0, 6.8397, -1.4894 \
                     A 40, 40, 0, 0, 1, 6.8397, -18.511 \
                     A 7, 7, 0, 1, 0, -6.8397, -18.511 \
                     A 40, 40, 0, 0, 1, -6.8397, -1.4894 z"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })

    # 複製 cmbr, 然後命名為 basic1
    basic1 =  cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(120)
    basic1.translate(21, 20)
    
    basic2 = cmbr.dup()
    basic2.rotate(90)
    basic2.translate(0, -20)
    
    basic3 = basic2.dup()
    basic3.rotate(90)
    basic3.translate(-20, 0)
    
    basic4 = cmbr.dup()
    basic4.rotate(120)
    basic4.translate(24*math.cos(30*deg), -13.25*math.sin(30*deg)-13.25)
    
    basic5 = cmbr.dup()
    basic5.translate(2.20*20*math.cos(30*deg), 10)
    
    basic6 = basic3.dup()
    basic6.rotate(0)
    basic6.translate(0, 20)
    
    basic7 = basic6.dup()
    basic7.rotate(90)
    basic7.translate(40,20)
    
    basic8 = basic7.dup()
    basic8.rotate(-30)
    basic8.translate(11,2.5)
    
    basic9 = cmbr.dup()
    basic9.rotate(0)
    basic9.translate(0,60)
    
    basic10 = cmbr.dup()
    basic10.rotate(90)
    basic10.translate(0,60)
    
    basic11 = basic10.dup()
    basic11.rotate(-30)
    basic11.translate(-10,8)
    
    basic12 = cmbr.dup()
    basic12.rotate(2.5)
    basic12.translate(37.5,50)
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    cmbr.appendPath(basic8)
    cmbr.appendPath(basic9)
    cmbr.appendPath(basic10)
    cmbr.appendPath(basic11)
    cmbr.appendPath(basic12)
    
    # hole 為原點位置
    hole = cobj(shapedefs.circle(4), "PATH")
    cmbr.appendPath(hole)

    # 表示放大 3 倍
    #cgo.render(cmbr, x, y, 3, rot)
    # 放大 5 倍
    cgo.render(cmbr, x, y, 0.5, rot)

O(0, 0, 0, 0, 0, "lightyellow", True, 4)
'''
    return outstring
    

    
    
