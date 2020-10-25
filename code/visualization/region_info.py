import pandas as pd
import warnings
warnings.filterwarnings("ignore")

time_province = pd.read_csv('../../data/korea/covid/TimeProvince.csv')
movement = pd.read_csv('../../data/korea/covid/Movement_2019_2020_7.csv')
region = pd.read_csv('../../data/korea/covid/Region.csv')
patient = pd.read_csv('../../data/korea/covid/PatientInfo.csv')

loc_dict = {
    'Seoul': [37.5665, 126.9780],
    'Gyeonggi-do': [37.3138, 127.1183],
    'Incheon': [37.4563, 126.7052],
    'Daejeon': [36.3504, 127.3845],
    'Daegu': [35.8714, 128.6014],
    'Gwangju': [35.1595, 126.8526],
    'Gangwon-do': [37.8228, 128.1555],
    'Ulsan': [35.5384, 129.3114],
    'Sejong': [36.4870, 127.2822],
    'Chungcheongbuk-do': [36.8000, 127.7000],
    'Chungcheongnam-do': [36.6184, 126.8000],
    'Jeollabuk-do': [35.7175, 127.1530],
    'Jeollanam-do': [34.8679, 126.9910],
    'Gyeongsangbuk-do': [36.4919, 128.8889],
    'Gyeongsangnam-do': [35.4606, 128.2132],
    'Busan': [35.1796, 129.0756],
    'Jeju-do': [33.4890, 126.4983],
}

regional_patient = pd.merge(patient[['patient_id', 'confirmed_date', 'sex', 'age', 'province', 'city']],
                            region[['province', 'city', 'latitude', 'longitude']], how='left', on=['province', 'city'])

# drop missing values
regional_count = regional_patient[['latitude', 'longitude']].dropna()

