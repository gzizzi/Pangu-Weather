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
model_6 = onnx.load('pangu_weather_6.onnx')

# Set the behavier of onnxruntime
options = ort.SessionOptions()
options.enable_cpu_mem_arena=False
options.enable_mem_pattern = False
options.enable_mem_reuse = False
# Increase the number for faster inference and more memory consumption
options.intra_op_num_threads = 1

# Set the behavier of cuda provider
# The CUDA Execution Provider enables hardware accelerated computation on Nvidia CUDA-enabled GPUs
#
cuda_provider_options = {'arena_extend_strategy':'kSameAsRequested',}

# Initialize onnxruntime session for Pangu-Weather Models
ort_session_24 = ort.InferenceSession('pangu_weather_24.onnx', sess_options=options, providers=[('CUDAExecutionProvider', cuda_provider_options)])
ort_session_6 = ort.InferenceSession('pangu_weather_6.onnx', sess_options=options, providers=[('CUDAExecutionProvider', cuda_provider_options)])

# Load the upper-air numpy arrays
input = np.load(os.path.join(input_data_dir, f'input_upper_{i_Time}.npy')).astype(np.float32)
# Load the surface numpy arrays
input_surface = np.load(os.path.join(input_data_dir, f'input_surface_{i_Time}.npy')).astype(np.float32)

# Run the inference session
input_24, input_surface_24 = input, input_surface
for i in range(28):
  if (i+1) % 4 == 0:
    output, output_surface = ort_session_24.run(None, {'input':input_24, 'input_surface':input_surface_24})
    input_24, input_surface_24 = output, output_surface
  else:
    output, output_surface = ort_session_6.run(None, {'input':input, 'input_surface':input_surface})
  input, input_surface = output, output_surface
  # Your can save the results here
  np.save(os.path.join(output_data_dir, f'output_upper_{i_Time}_step_{i}.npy'), output)
  np.save(os.path.join(output_data_dir, f'output_surface_{i_Time}_step_{i}.npy'), output_surface)

print("--- %s minutes ---" % ((time.time() - start_time)/60))
