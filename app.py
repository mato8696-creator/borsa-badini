# 7. وەرگرتنا بها و گونجاندن دگەل بازارێ دهۆک (نوو)
try:
    resp = requests.get("https://api.exchangerate-api.com/v4/latest/USD").json()
    # ل ڤێرە مە زێدەتر لێکر دا بگونجیت دگەل بازارێ دهۆک
    one_usd = resp['rates']['IQD'] + 2.5  
    iqd_100 = one_usd * 100
except:
    one_usd, iqd_100 = 1472.5, 147250 # نرخێ دەستپێکێ ئەگەر ئینتەرنێت نەبوو
