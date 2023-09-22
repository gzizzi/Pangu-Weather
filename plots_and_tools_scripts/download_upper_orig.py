import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-pressure-levels',
    {
        'product_type': 'reanalysis',
        'format': 'grib',
        'pressure_level': [
            '50', '100', '150',
            '200', '250', '300',
            '400', '500', '600',
            '700', '850', '925',
            '1000',
        ],
        'year': '2018',
        'month': '09',
        'day': '27',
        'time': '12:00',
        'variable': [
            'geopotential', 'specific_humidity', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
        ],
    },
    'download.grib')

