# how to download surface and files with meaningful names
#only grib files are downloaded with 
import cdsapi

def download_data(Iday,Imonth,Iyear,Itime,level):

	c = cdsapi.Client()

	if level =="surface":
		dict={  'product_type': 'reanalysis',
		        'variable': [
		            '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_temperature',
		            'mean_sea_level_pressure',
		        ],
		        'year': Iyear,
		        'month': Imonth,
		        'day': Iday,
		        'time': Itime,
		        'format': 'grib',
		     }
		
		hour=dict['time'].split(':')[0]
		download="input_surface_"+dict['day']+"_"+dict['month']+"_"+dict['year']+"_"+hour+"."+dict['format']
		category='reanalysis-era5-single-levels' 
		#print(Itime)
		#print(download)

	if level=="upper":
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
		        'year': Iyear,
		        'month': Imonth,
		        'day': Iday,
		        'time': Itime,
		        'variable': [
		            'geopotential', 'specific_humidity', 'temperature',
		            'u_component_of_wind', 'v_component_of_wind',
		        ],
		    }
		    
		hour=dict['time'].split(':')[0]    
		download="input_upper_"+dict['day']+"_"+dict['month']+"_"+dict['year']+"_"+hour+"."+dict['format']
		category='reanalysis-era5-pressure-levels'
                
	print(download)
	print(category)

	c.retrieve(category, dict, download)

#if __name__ == "__main__":
download_data("19","09","2018","12:00","upper")
