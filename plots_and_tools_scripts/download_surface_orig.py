# how to download surface files
import cdsapi

c = cdsapi.Client()

c.retrieve(
    'reanalysis-era5-single-levels',
    {
        'product_type': 'reanalysis',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature',
            'mean_sea_level_pressure',
        ],
        'year': '2018',
        'month': '09',
        'day': '27',
        'time': '12:00',
        'format': 'grib',
    },
    'download.grib')
