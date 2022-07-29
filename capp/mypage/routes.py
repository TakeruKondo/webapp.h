from flask import Blueprint,render_template

mypage= Blueprint('mypage',__name__,template_folder="templates", static_folder="static")

@mypage.route('/mypageTop')
def usertop():
    return render_template('top_mypage.html')
