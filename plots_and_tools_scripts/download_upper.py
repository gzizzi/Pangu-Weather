# how to download "plev" files with meaningful names
import cdsapi

c = cdsapi.Client()

dict= {
        'product_type': 'reanalysis',
        'format': 'grib',
        'pressure_level': [
            '50', '100', '150',
            '200', '250', '300',
            '400', '500', '600',
            '700', '850', '925',
            '1000',
        ],
        'year': '2020',
        'month': '09',
        'day': '15',
        'time': '12:00',
        'variable': [
            'geopotential', 'specific_humidity', 'temperature',
            'u_component_of_wind', 'v_component_of_wind',
        ],
    }
    
hour=dict['time'].split(':')[0]    
download="input_upper_"+dict['day']+"_"+dict['month']+"_"+dict['year']+"_"+hour+"."+dict['format']
print(download)

c.retrieve(
    'reanalysis-era5-pressure-levels',
    dict,
    download)


