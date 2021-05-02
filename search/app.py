import connexion
import os
import sys

sys.path.append("./api")

apiver = "v2.0"
base_path_prefix = "backend"
app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('openapi.yaml', arguments={'api_version': apiver, 'base_path_prefix': base_path_prefix})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6000)
