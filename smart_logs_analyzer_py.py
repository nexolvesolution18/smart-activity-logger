# -*- coding: utf-8 -*-


from math import log
from datetime import datetime
import json

now = datetime.now()
file_path = ''
def load_logs() :
  try:
        with open(file_path, 'r') as f :
          return json.load(f)
  except :
    return []
logs= load_logs()
def save_logs():
    with open(file_path, 'w') as f:
        json.dump(logs, f)

def add_log():
  activity = input('enter log : ')
  now = datetime.now().strftime("%d/%m/%Y ")
  log = { "Message" : activity,
          "time" : now
  }
  logs.append(log)
  save_logs()
  print('log added')

  return menu()

def view_log():
  if not logs :
    print('no logs yet')
  else :
    for log in logs:
        print(f"{log['Message']} → {log['time']}\n")
  return menu()
def log_filter() :
  search = input('search...')
  results = [log for log in logs if search.lower() in log['Message'].lower()]
  for log in results :
    print(f"{log['Message']} was created on {log['time']}")
  return menu()
def count_logs() :
  count_log = len(logs)
  print(count_log)
  return menu()
def menu() :
  while True :
     print("\n1. Add logs")
     print("2. View Logs")
     print("3. Search Logs")
     print("4. Count Logs")
     print("5. Exit")
     choice = input(' enter choice')
     if choice == "1" :
      return add_log()
     elif choice == '2' :
      return view_log()
     elif choice == '3' :
      return log_filter()
     elif choice == '4' :
      return count_logs()
     elif choice == '5' :
      return('exiting')
     else :
      return('invalid choice')
load_logs()
menu()

