from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


data = pd.read_csv('ml_app/UK_Accident.csv')

data = data.dropna()  

target = 'Accident_Severity' 
features = ['Location_Easting_OSGR', 'Location_Northing_OSGR']

X = data[features] 
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

def predict(request):
    if request.method == 'POST':
        location_easting = request.POST.get('location_easting')
        location_northing = request.POST.get('location_northing')

        if location_easting is not None and location_northing is not None:
            try:
                location_easting = float(location_easting)
                location_northing = float(location_northing)

                user_input = {
                    'Location_Easting_OSGR': location_easting,
                    'Location_Northing_OSGR': location_northing
                }

                user_input_df = pd.DataFrame([user_input])

               
                prediction = model.predict(user_input_df)

                
                return JsonResponse({'prediction': prediction[0]})
            
            except ValueError as e:
                return JsonResponse({'error': 'Invalid input. Please enter valid numbers.'})

    return render(request, 'prediction.html')
