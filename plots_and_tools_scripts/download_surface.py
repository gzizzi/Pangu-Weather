# how to download surface files with meaningful names
import cdsapi

c = cdsapi.Client()

dict={  'product_type': 'reanalysis',
        'variable': [
            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature',
            'mean_sea_level_pressure',
        ],
        'year': '2020',
        'month': '09',
        'day': '15',
        'time': '12:00',
        'format': 'grib',
     }

hour=dict['time'].split(':')[0]

download="input_surface_"+dict['day']+"_"+dict['month']+"_"+dict['year']+"_"+hour+"."+dict['format']

c.retrieve(
     'reanalysis-era5-single-levels', 
     dict,
     download)

