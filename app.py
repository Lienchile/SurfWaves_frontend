
import streamlit as st
from datetime import date
from datetime import datetime
import pandas as pd

### --------------SURF WAVES STREAMLIT CODE -------------------------###

# ------------------------Header Section-----------------------------#

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide",page_title='SurfWaves Project',page_icon=':surfer:')
st.image('The-great-wave.jpg',use_column_width='always')
st.title("""SurfWaves Project :surfer:""")

# ------------------------SideBar Section-----------------------------#
st.sidebar.header(':round_pushpin: Choose your specific feature:')

#Add a select box to choose the location
api_input = st.sidebar.selectbox(
    ' Where would you like to surf?',
    ('DePanne', 'Oostend', 'Knokke')
)
if api_input == 'DePanne':
    st.sidebar.write(f'You choose {api_input}')
    st.sidebar.write('''It is situated close to the border
                     with France in the south-west of Belgian coast.
                     Known for its elongated dunes, the Panne is the place of birth of beach sailing.''')
    st.sidebar.image('de-panne.jpg',use_column_width='always')
elif api_input == 'Oostend':
    st.sidebar.write(f'You choose {api_input}')
    st.sidebar.write('''As Belgium’s largest coastal outpost, Ostend offers a rare taste of Flemish beach culture.
                     Inland visitors flock to sandy beaches and the seaside promenade, while
                     reminders of the city’s military and maritime history run deep in the old harbor town.''')
    st.sidebar.image('oostend.jpg',use_column_width='always')
else:
    st.sidebar.write(f'You choose {api_input}')
    st.sidebar.write('''Knokke is the most north-eastern seaside resort on the Belgian coast.
                     It lies adjacent to the Dutch border;
                     separated from the Dutch territory by the Zwin nature reserve.''')
    st.sidebar.image('knokke.jpg',use_column_width='always')



col1, col2 = st.columns(2)



# --------------------- Left Column Section/Column1------------------#

#Add a time stamp selection
now = datetime.now()
timestamp =pd.to_datetime(now)
# Print the current date only
today = date.today()

#Dummy answer

api = {"rating": 2,
       'wind_speed': 10.5,
       'wind_direction':58,
        'tide': 'low',
        'wave_height': 150}

if st.sidebar.button('Click to see the result'):
    # print is visible in the server output, not in the page
    print('button clicked it will show the rating!')
    if api['rating']==2 or api['rating']==3:
        expander = col1.expander("Optional informations")
        with expander:
            col1.metric(label="The wind speed in m/s", value=api['wind_speed'])
            col1.metric(label="The wave height in cm", value=api['wave_height'])
            col1.metric(label="The tide is", value=api['tide'])
            col2.image("surfeur.jpg")
        st.success('It is the ideal time to surf!')
        st.write(f'''Date: {today} - Time: {now.hour}:{now.minute} ''')
    else:
        expander = col1.expander("Optional informations")
        with expander:
            col1.metric(label="The wind speed in m/s", value=api['wind_speed'])
            col1.metric(label="The wave height in m", value=api['wave_height'])
            col1.metric(label="The tide is", value=api['tide'])
            col1.write('')
            col2.image("home.jpg")
        st.error('Mmmh.. maybe you should stay home')
        st.write(f'''Date: {today} - Time: {now.hour}:{now.minute} ''')

else:
    st.write('👈 Choose your location and click on the button on the sidebar to see if it is a good day to go surfing')
