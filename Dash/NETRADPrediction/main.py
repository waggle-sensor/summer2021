  
from waggle import plugin

import pandas as pd
import numpy as np

plugin.init()
image_array = []
met_data = []

model = tf.keras.models.load_model(https://github.com/waggle-sensor/summer2021/blob/main/Dash/LCLPressureplugin/thursdaythetwentyninthmodel1.h5)
ans  =model.predict([np.array(met_data),np.array(image_array)])
plugin.publish(ans, "Net Solar Irradiance")
