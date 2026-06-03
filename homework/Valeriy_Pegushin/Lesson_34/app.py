import datetime
import time
import os


def main():
    print("🐳 Docker контейнер запущен!")
    print(f"📅 Текущее время: {datetime.datetime.now()}")
    print(f"🐍 Версия Python: {os.sys.version}")
    print("-" * 50)

    counter = 0
    try:
        while True:
            counter += 1
            print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Счётчик: {counter}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("\n👋 Программа остановлена")


main()
