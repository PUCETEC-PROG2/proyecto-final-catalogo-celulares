def total_compra(request):
    total = 0
    if request.user.is_authenticated:
        if "compra" in request.session.keys():
            for key, value in request.session["compra"].items():
                total += int(value.get("acumulado", 0))
    return {"total_compra": total}