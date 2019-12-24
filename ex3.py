import time


def start_water_heating_system(water_level, input_temp):
	# initialize variables
	temp = 0
	boiler = 0
	
	print ("Water Level:", water_level)
	print ("Current temperature:", temp)
	print ("Input temperature:", input_temp)

	if (water_level > 100):
		# turn on boiler
		boiler = 1
		
		while (temp < input_temp):
			#print ("Current Temp:", temp)
			# Heat the water
			temp = temp + 1
			time.sleep(1)
	
	return temp
			




############# TESTS #####################

def test_start_water_heating():
	temp = start_water_heating_system(200, 10)
	assert temp == 10, "Current temp should be 10"

def test_low_water_level():
	temp = start_water_heating_system(0, 100)
	assert temp == 0, "Boiler should not be turned on to increase the temperature"

	
if __name__ == "__main__":

	test_low_water_level()
	test_start_water_heating()
	
	print("Tests completed")
