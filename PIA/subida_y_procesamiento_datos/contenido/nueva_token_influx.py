from influxdb_client import InfluxDBClient

# Configuración
influx_url = "http://influxdb:8086"
admin_token = "solo_para_cryptobros"  # reemplaza con el token válido
org = "Cryptobro_Together_Strong"

# Crear cliente
client = InfluxDBClient(
    url=influx_url,
    token=admin_token,
    org=org
)

# Llamada directa a la API sin auth_settings
response = client.api_client.call_api(
    '/api/v2/authorizations', 'GET',
    response_type='AuthorizationList'
)

# Imprimir tokens activos
for auth in response[0].authorizations:
    if auth.status == "active":
        print("✅ Token activo encontrado:")
        print(auth.token)