from influxdb_client import InfluxDBClient, Permission, PermissionResource

# Configuración
INFLUXDB_URL    = "http://influxdb:8086"
ADMIN_TOKEN     = "solo_para_cryptobros"
ORG             = "Cryptobro_Together_Strong"
BUCKET_NAME     = "livemarket"

def crear_token_escritura():
    client = InfluxDBClient(
        url=INFLUXDB_URL,
        token=ADMIN_TOKEN,
        org=ORG
    )

    # Obtener el bucket
    bucket = client.buckets_api().find_bucket_by_name(BUCKET_NAME)
    if not bucket:
        print(f"❌ No se encontró el bucket '{BUCKET_NAME}'")
        return None

    # Obtener la organización por nombre
    orgs = client.organizations_api().find_organizations()
    org_obj = next((o for o in orgs if o.name == ORG), None)
    if not org_obj:
        print(f"❌ No se encontró la organización '{ORG}'")
        return None


    # Crear permiso de escritura
    write_perm = Permission(
        action="write",
        resource=PermissionResource(type="buckets", id=bucket.id)
    )

    # Buscar si ya existe un token con ese permiso
    existing_auths = client.authorizations_api().find_authorizations(org_id=org_obj.id)
    for auth in existing_auths:
        if write_perm in auth.permissions:
            print(f"🔁 Ya existe un token con permiso de escritura: {auth.token}")
            return auth.token

    # Si no existe, crear uno nuevo
    new_auth = client.authorizations_api().create_authorization(
        permissions=[write_perm],
        org_id=org_obj.id
    )

    print(f"✅ Token creado: {new_auth.token}")
    return new_auth.token

if __name__ == "__main__":
    crear_token_escritura()
