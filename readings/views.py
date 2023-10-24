from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from spd.models import DataParameter, Parameter, Station


@csrf_exempt
@require_POST
def new_reading(request):
    # http_response = ""
    try:
        stationOBJ = Station.objects.get(id=request.POST.get("id"))
        print(stationOBJ.access_token)
    except Exception as e:
        print("FALHA GERAL [posivel estacao não existente]\n" + e)
        return HttpResponse("FALHA GERAL [posivel estacao inexistente]\n")

    if request.POST.get("token") == stationOBJ.access_token:
        print(request.POST.get("values"))
        valores = request.POST.get("values").split(";")
        for variaveis in valores:
            print(variaveis + "\n")
            valor_variavel = variaveis.split("=")
            print("Variavel = " + valor_variavel[0])
            print("Valor = " + valor_variavel[1])
            parametro = Parameter.objects.get(name=valor_variavel[0])
            # parametro.id
            dataPrameterOBJ = DataParameter(
                value=valor_variavel[1],
                parameter_id_id=parametro.id,
                station_id_id=request.POST.get("id"),
            )
            dataPrameterOBJ.save()
        """
                        dataPrameterOBJ = DataParameter(value=request.POST.get("values"), parameter_id_id=1, station_id_id=request.POST.get('id'))
                        dataPrameterOBJ.save()
                        """
        http_response = HttpResponse("save\n")
    else:
        http_response = HttpResponse("Authenticate error\n")

    return http_response
