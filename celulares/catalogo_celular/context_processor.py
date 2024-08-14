def total_compra(request):
    total = 0
    if request.user.is_authenticated:
        if request.session["compra"]:
            for key, value in request.session["compra"].items():
                total += int(value["acumulado"])
    return {"total_compra": total}