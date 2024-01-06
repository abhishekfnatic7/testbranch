from django.shortcuts import render
from .models import Second
from django.shortcuts import render
from django.http import HttpResponse
from telegram import Bot
# Create your views here.

def home(request):
    # s=Second.objects.only('fname')
    ss=Second.objects.only('fname')
    # print(s
    print(ss)
  
    return render(request,'a.html') 

# views.py
from rest_framework import generics
from .models import Third
from .serializers import YourModelSerializer
from django.http import HttpResponse
from django_pandas.io import read_frame
from django.db.models import F, DateTimeField
from datetime import datetime, timedelta
from django.db.models.functions import Trunc
from django.db.models import Count, F,Q
from django.db import models
start_date = datetime(2023, 12, 23)
end_date = start_date + timedelta(days=1)
from django.utils import timezone
from django.db.models.functions import Extract
from django.db.models.functions import TruncHour
class FilteredDataDownloadView(generics.ListAPIView):
    serializer_class = YourModelSerializer

    def get_queryset(self):
        a=Third.objects.filter(recordated_at__date__range=['2023-12-23','2023-12-23'])
        result = a.annotate(hour=Extract('recordated_at', 'hour'))
        for x in result:
            print(x['hour'])
        
            

    def get(self, request, *args, **kwargs):
        # Get the filtered queryset
        queryset = self.get_queryset()

        # Serialize the queryset to a DataFrame
        # df = read_frame(queryset, fieldnames=['facility', 'people_in'])  # Specify the fields you want in the DataFrame
        # df.rename(columns={'facility':'Facility Name'},inplace=True)

        # # Convert DataFrame to CSV (or any other format you prefer)
        # csv_data = df.to_csv(index=False)

        # # Create the HTTP response with the CSV data
        # response = HttpResponse(csv_data, content_type='text/csv')
        # response['Content-Disposition'] = 'attachment; filename="filtered_data.csv"'

        return queryset


from django.shortcuts import render
from django.http import HttpResponse
from telegram import Bot

def send_telegram_message(request):
    try:
        # Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
        bot_token = '6927554400:AAG_LONergnsb1y_UyZiqeS3UwvVM4fC1Jk'
        bot = Bot(token=bot_token)
        
        # Replace 'YOUR_CHAT_ID' with the actual chat ID of your Telegram group
        group_name = 'YOUR_GROUP_NAME'

        # Message to be sent to the group
        message = "Hello from your Django web application!"
        updates = bot.get_updates()

        for update in updates:
            chat = update.message.chat
            if chat.type == 'group' and chat.title == group_name:
                chat_id = chat.id
                print(f"Chat ID for {group_name}: {chat_id}")
                break
        # Send the message
        sent_message = bot.send_message(chat_id=chat_id, text=message)

        if sent_message:
            return HttpResponse("Telegram message sent successfully!")
        else:
            return HttpResponse("Failed to send Telegram message.")

    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")

