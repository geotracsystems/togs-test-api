oauth = {
    'test': {
        'url': 'https://auth.geotracdemo.com/connect/token',
        'client_id': 'D1A72CBD-F605-4C89-9A0E-8D50D282B423',
        'client_secret': 'eFleetSuite',
        'username': 'efsdealer',
        'password': 'efs',
        'scope': 'openid profile email webapiroles'
    },
    'prod': {
        'url': 'https://auth.assetcontrolcenter.com/connect/token',
        'client_id': 'D1A72CBD-F605-4C89-9A0E-8D50D282B423',
        'client_secret': 'eFleetSuite',
        'username': 'androidBifrost',
        'password': 'Ijustateabunchofpeanutbuttersandwiches!',
        'scope': 'openid profile email webapiroles'
    }
}

bifrost = {
    'test': {
        'swagger': 'https://bifrost.geotracdemo.com/togs-api-docs/v1/swagger.json',
        'endpoint': 'https://bifrost.geotracdemo.com'
    },
    'prod': {
        'swagger': 'https://bifrost.gogeotrac.com/togs-api-docs/v1/swagger.json',
        'endpoint': 'https://bifrost.gogeotrac.com'
    }
}
