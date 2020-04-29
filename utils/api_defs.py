bifrost = {
    'test': {
        'swagger': 'https://bifrost.geotracdemo.com/togs-api-docs/v1/swagger.json',
        'endpoint': 'https://bifrost.geotracdemo.com',
        'oauth': {
            'url': 'https://auth.geotracdemo.com/connect/token',
            'client_id': 'D1A72CBD-F605-4C89-9A0E-8D50D282B423',
            'client_secret': 'eFleetSuite',
            'username': 'efsdealer',
            'password': 'efs',
            'scope': 'openid profile email webapiroles'
        }
    },
    'prod': {
        'swagger': 'https://bifrost.gogeotrac.com/togs-api-docs/v1/swagger.json',
        'endpoint': 'https://bifrost.gogeotrac.com',
        'oauth': {
            'url': 'https://auth.assetcontrolcenter.com/connect/token',
            'client_id': 'D1A72CBD-F605-4C89-9A0E-8D50D282B423',
            'client_secret': 'eFleetSuite',
            'username': 'androidBifrost',
            'password': 'Ijustateabunchofpeanutbuttersandwiches!',
            'scope': 'openid profile email webapiroles'
        }
    }
}

vehicle = {
    'test': {
        'swagger': 'http://testdockersrv.geotracdemo.com:4002/togs-api-docs/v1/swagger.json',
        'endpoint': 'http://testdockersrv.geotracdemo.com:4002'
    },
    'prod': {
        'swagger': 'http://proddockersrv.assetcontrolcenter.com:4002/togs-api-docs/v1/swagger.json',
        'endpoint': 'http://proddockersrv.assetcontrolcenter.com:4002'
    }
}


eld_dvir = {
    'test': {
        'swagger': 'https://togsapigateway.geotracdemo.com/api-specs/EldDVIRAPI.json',
        'endpoint': 'https://togsapigateway.geotracdemo.com/api/eld',
        'oauth': {
            'url': 'https://auth.geotracdemo.com/connect/token',
            'client_id': 'D1A72CBD-F605-4C89-9A0E-8D50D282B423',
            'client_secret': 'eFleetSuite',
            'username': 'eldWebapiTest',
            'password': 'Test1234',
            'scope': 'profile webapiroles'
        }
    },
    'prod': {
        'swagger': 'https://togsapigateway.gogeotrac.com/api-specs/EldDVIRAPI.json',
        'endpoint': 'https://togsapigateway.gogeotrac.com/api/eld',
        'oauth': {
            'url': 'https://auth.assetcontrolcenter.com/connect/token',
            'client_id': 'D1A72CBD-F605-4C89-9A0E-8D50D282B423',
            'client_secret': 'eFleetSuite',
            'username': '',
            'password': '',
            'scope': 'profile webapiroles'
        }
    }
}
