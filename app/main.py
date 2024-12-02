import signal
import sys
from threading import Thread
from server import run_server
from bot import run_bot


def signal_handler(sig, frame):
    print("プログラムを終了します。")
    sys.exit(0)


# SIGINTシグナルをキャッチ
signal.signal(signal.SIGINT, signal_handler)

# サーバーを別スレッドで実行
server_thread = Thread(target=run_server, kwargs={"debug": True})
server_thread.start()

# Discord botを起動
run_bot()
