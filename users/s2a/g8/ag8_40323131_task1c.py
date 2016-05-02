
# 各組分別在各自的 .py 程式中建立應用程式 (第1步/總共3步)
from flask import Blueprint, render_template

# 利用 Blueprint建立 ag1, 並且 url 前綴為 /ag1, 並設定 template 存放目錄
ag8_40323131c = Blueprint('ag8_40323131c', __name__, url_prefix='/ag8_40323131c', template_folder='templates')

# scrum1_task1 為完整可以單獨執行的繪圖程式
@ag8_40323131c.route('/task1c')
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

cgo.setWorldCoords(-350, -250, 500, 500) 

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
    basic1 = cmbr.dup()
    # basic1 轉 120 度
    basic1.rotate(180)
    basic2 = cmbr.dup()
    basic2.rotate(30)
    basic2.translate(0, -20)
    
    basic3 = basic2.dup()
    basic3.rotate(120)
    basic3.translate(-17.5,10)
    
    basic4 = cmbr.dup()
    basic4.rotate(70)
    basic4.translate(11.5*math.cos(30*deg), -25*math.sin(30*deg)-25)
    
    basic5 = cmbr.dup()
    basic5.rotate(90)
    basic5.translate(1.7*20*math.cos(30*deg), -44.5)
    
    basic6 = basic3.dup()
    basic6.rotate(-30)
    basic6.translate(0,20)
    
    basic7 = cmbr.dup()
    basic7.rotate(90)
    basic7.translate(27.5,47.5)
    
    cmbr.appendPath(basic1)
    cmbr.appendPath(basic2)
    cmbr.appendPath(basic3)
    cmbr.appendPath(basic4)
    cmbr.appendPath(basic5)
    cmbr.appendPath(basic6)
    cmbr.appendPath(basic7)
    
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
    

    
    
