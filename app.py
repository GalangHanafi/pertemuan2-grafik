import streamlit as st
import pandas as pd
import numpy as np

# Data sederhana
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [200, 300, 400, 350, 500]
})

#
# 1 AREA CHART
#
st.title('Area Chart')
st.area_chart(data.set_index('Month'))
st.markdown('---')

#
# 2 BAR CHART
#
st.title('Bar Chart')
st.bar_chart(data.set_index('Month'))
st.markdown('---')

#
# 3 LINE CHART
#
st.title('Line Chart')
st.line_chart(data.set_index('Month'))
st.markdown('---')

#
# 4 SCATTER CHART
#
st.title('Scatter Chart')
# Dataset untuk scatter plot
scatter_data = pd.DataFrame({
    'X': np.random.rand(100),
    'Y': np.random.rand(100)
})
# Menampilkan scatter chart
st.scatter_chart(scatter_data)
st.markdown('---')

#
# 5 MAP CHART
#
st.title('Map Chart')
# Menghasilkan 100 data acak di sekitar Yogyakarta
np.random.seed(42)  # Untuk reproducibility
latitudes = -7.8 + np.random.rand(100) * 0.1  # Sekitar Yogyakarta
longitudes = 110.36 + np.random.rand(100) * 0.1  # Sekitar Yogyakarta

# Membuat DataFrame dengan lat dan lon
map_data = pd.DataFrame({
    'lat': latitudes,
    'lon': longitudes
})

# Menampilkan peta
st.map(map_data)