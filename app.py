@app.route('/sonlar/toq')
def toq_sonlar():
    sonlar = [14, 8, 33, 5, 71, 22, 9, 46]

    toqlar = []
    for son in sonlar:
        if son % 2 != 0:
            toqlar.append(son)

    yigindi = sum(toqlar)

    return render_template("toq.html",
                           toqlar=toqlar,
                           yigindi=yigindi)
