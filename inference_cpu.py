import os
import numpy as np
import onnx
import onnxruntime as ort

import time                   #in order to measure how much time is needed
start_time = time.time()      #


i_Time="16_09_2020_00"

# The directory of your input and output data
input_data_dir = 'input_data'
output_data_dir = 'output_data'
model_24 = onnx.load('pangu_weather_24.onnx')

# Set the behavier of onnxruntime
options = ort.SessionOptions()
options.enable_cpu_mem_arena=False
options.enable_mem_pattern = False
options.enable_mem_reuse = False
# Increase the number for faster inference and more memory consumption
options.intra_op_num_threads = 1

# Set the behavier of cuda provider
cuda_provider_options = {'arena_extend_strategy':'kSameAsRequested',}

# Initialize onnxruntime session for Pangu-Weather Models
ort_session_24 = ort.InferenceSession('pangu_weather_24.onnx', sess_options=options, providers=['CPUExecutionProvider'])

# Load the upper-air numpy arrays
#input = np.load(os.path.join(input_data_dir, 'input_upper.npy')).astype(np.float32)
input = np.load(os.path.join(input_data_dir, f'input_upper_{i_Time}.npy')).astype(np.float32)
# Load the surface numpy arrays
#input_surface = np.load(os.path.join(input_data_dir, 'input_surface.npy')).astype(np.float32)
input_surface = np.load(os.path.join(input_data_dir, f'input_surface_{i_Time}.npy')).astype(np.float32)

# Run the inference session
output, output_surface = ort_session_24.run(None, {'input':input, 'input_surface':input_surface})

# Save the results
np.save(os.path.join(output_data_dir, f'output_upper_{i_Time}'), output)
np.save(os.path.join(output_data_dir, f'output_surface_{i_Time}'), output_surface)

print("--- %s minutes ---" % ((time.time() - start_time)/60)) 



