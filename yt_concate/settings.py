# 讓環境變數可以存在檔案裡
from dotenv import load_dotenv
import os

load_dotenv()
# 都大寫_表static variable 永不變的變數
API_KEY = os.getenv('API_KEY')
