from django.shortcuts import render, redirect
from .models import BitcoinPrediction, LitecoinPrediction, StellarPrediction
from APP.models import BitcoinPrediction, LitecoinPrediction, StellarPrediction
from . forms import  UserRegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
import numpy as np
import joblib
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from django.utils import timezone
from IPython.display import display, Image


def Landing_1(request):
    return render(request, '1_Landing.html')

def Register_2(request):
    form = UserRegisterForm()
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            print('data passed')
            user = form.cleaned_data.get('username')
            print(user)
            messages.success(request, 'Account was successfully created. ' + user)
            return redirect('Login_3')

    context = {'form':form}
    return render(request, '2_Register.html', context)


def Login_3(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print(user)

        if user is not None:
            login(request, user)
            return redirect('Home_4')
        else:
            messages.info(request, 'Username OR Password incorrect')

    context = {}
    return render(request,'3_Login.html', context)

def Home_4(request):
    return render(request, '4_Home.html')

def Teamates_5(request):
    return render(request,'5_Teamates.html')

def Domain_Result_6(request):
    return render(request,'6_Domain_Result.html')

Model1 = joblib.load('APP/BITCOIN1.pkl')
def Deploy_7(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]  # Skip the first value which might be CSRF token or similar

        a = []
        for i in int_features:
            try:
                a.append(int(i))
            except ValueError:
                # Handle the error or skip the value
                print(f"ValueError: Cannot convert {i} to int")
                return render(request, 'Deploy_7.html', {"prediction_text": f"Invalid input: {i} is not a number"})

        final_features = [np.array(a, dtype=object)]
        print(final_features)
        prediction = Model1.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        a.append(output)
        print(a)

        # Save the prediction to the database
        BitcoinPrediction.objects.create(
            open_price=a[0],
            high_price=a[1],
            low_price=a[2],
            volume=a[3],
            closing_price=output
        )

        categories = ['Open', 'High', 'Low', 'Volume', 'close']
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=categories, y=a, marker='o', color='red')

        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title(f"['Open', 'High', 'Low', 'Volume', 'close'] : {a}")

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        context = {'plot_base64': plot_base64}

        return render(request, 'bitcoin.html', {"prediction_text": f'THE BITCOIN STOCK CLOSING PRICE IS {output}', 'plot_base64': plot_base64})

    else:
        return render(request, '7_Deploy.html')
    

    


    
    
Model2 = joblib.load('APP/LITECOIN1.pkl')  
  
def Deploy_9(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]  # Skip the first value which might be CSRF token or similar

        a = []
        for i in int_features:
            try:
                a.append(int(i))
            except ValueError:
                # Handle the error or skip the value
                print(f"ValueError: Cannot convert {i} to int")
                return render(request, 'Deploy_9.html', {"prediction_text": f"Invalid input: {i} is not a number"})

        final_features = [np.array(a, dtype=object)]
        print(final_features)
        prediction = Model2.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        a.append(output)
        print(a)

        # Save the prediction to the database
        LitecoinPrediction.objects.create(
            open_price=a[0],
            high_price=a[1],
            low_price=a[2],
            volume=a[3],
            closing_price=output
        )

        categories = ['Open', 'High', 'Low', 'Volume', 'close']
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=categories, y=a, marker='o', color='red')

        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title(f"['Open', 'High', 'Low', 'Volume', 'close'] : {a}")

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        context = {'plot_base64': plot_base64}

        return render(request, 'Litecoin.html', {"prediction_text": f'THE LITECOIN STOCK CLOSING PRICE IS {output}', 'plot_base64': plot_base64})

    else:
        return render(request, '9_Deploy.html')
    
    
    
Model3 = joblib.load('APP/STELLAR1.pkl')

def Deploy_10(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]  # Skip the first value which might be CSRF token or similar

        a = []
        for i in int_features:
            try:
                a.append(int(i))
            except ValueError:
                # Handle the error or skip the value
                print(f"ValueError: Cannot convert {i} to int")
                return render(request, 'Deploy_9.html', {"prediction_text": f"Invalid input: {i} is not a number"})

        final_features = [np.array(a, dtype=object)]
        print(final_features)
        prediction = Model3.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(output)
        a.append(output)
        print(a)

        # Save the prediction to the database
        StellarPrediction.objects.create(
            open_price=a[0],
            high_price=a[1],
            low_price=a[2],
            volume=a[3],
            closing_price=output
        )

        categories = ['Open', 'High', 'Low', 'Volume', 'close']
        plt.figure(figsize=(8, 6))
        sns.lineplot(x=categories, y=a, marker='o', color='red')

        plt.xlabel('Categories')
        plt.ylabel('Values')
        plt.title(f"['Open', 'High', 'Low', 'Volume', 'close'] : {a}")

        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)

        plot_base64 = base64.b64encode(buffer.read()).decode('utf-8')

        context = {'plot_base64': plot_base64}

        return render(request, 'stellar.html', {"prediction_text": f'THE STELLAR STOCK CLOSING PRICE IS {output}', 'plot_base64': plot_base64})

    else:
        return render(request, '10_Deploy.html')

def bit_db(request):
    predictions = BitcoinPrediction.objects.all()
    return render(request, 'bit_db.html', {'predictions': predictions})




def lite_db(request):
    predictions = LitecoinPrediction.objects.all()
    return render(request, 'lite_db.html', {'predictions': predictions})

def ste_db(request):
    predictions = StellarPrediction.objects.all()
    return render(request, 'ste_db.html', {'predictions': predictions})


def Logout(request):
    
    logout(request)
    return redirect('Landing_1')
def domain(request):
    return render(request,'domain.html')


def bitcoin_report(request):
    return render(request,'bitcoin_report.html')

def litecoin_report(request):
    return render(request,'litecoin_report.html')

def stellar_report(request):
    return render(request,'stellar_report.html')