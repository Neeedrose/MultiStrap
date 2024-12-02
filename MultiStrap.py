import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import ctypes
from ctypes import wintypes
import os
import time
from subprocess import Popen
import requests
import psutil
import json
import logging
import win32api
import win32process
import win32con
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

message_loop_running = False
message_loop_thread = None

# Default cookies file
DEFAULT_COOKIES_FILE = "roblox_cookies.txt"

if not os.path.exists(DEFAULT_COOKIES_FILE):
    with open(DEFAULT_COOKIES_FILE, "w", encoding="utf-8") as file:
        pass

def messageLoop():
    global message_loop_running

    mutex = ctypes.windll.kernel32.CreateMutexW(None, 1, "ROBLOX_singletonEvent")
    msg = wintypes.MSG()

    print("Mutex On")
    while message_loop_running:
        if ctypes.windll.user32.GetMessageW(ctypes.byref(msg), 0, 0, 0):
            ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
            ctypes.windll.user32.DispatchMessageW(ctypes.byref(msg))
    print("Message loop stopped.")

def startGame(placeID, gameID, security_cookie):
    try:
        print("Checking latest version of ROBLOX...")
        path = os.getenv("LOCALAPPDATA") + "\\Bloxstrap"
        if not os.path.exists(path):
            print("Error: Please install Bloxstrap.")
            return

        print("Fetching CSRF token...")
        req = requests.post(
            "https://auth.roblox.com/v1/authentication-ticket",
            headers={"Cookie": ".ROBLOSECURITY=" + security_cookie}
        )
        csrf = req.headers.get('x-csrf-token')
        print("CSRF token obtained.")

        print("Fetching authentication ticket...")
        req = requests.post(
            "https://auth.roblox.com/v1/authentication-ticket",
            headers={
                "Cookie": ".ROBLOSECURITY=" + security_cookie,
                "Origin": "https://www.roblox.com",
                "Referer": "https://www.roblox.com/",
                "X-CSRF-TOKEN": csrf,
                "Content-Type": "application/json"
            }
        )
        if len(req.content) > 2:
            print("Error: Could not fetch authentication ticket. Check your cookie.")
            return

        ticket = req.headers['rbx-authentication-ticket']
        print("Authentication ticket obtained.")

        location = path + "\\Bloxstrap.exe"
        args = (
            f"roblox-player:1+launchmode:play+gameinfo:{ticket}"
            f"+launchtime:{round(time.time() * 1000)}"
            f"+placelauncherurl:https%3A%2F%2Fassetgame.roblox.com%2Fgame%2F"
            f"PlaceLauncher.ashx%3Frequest%3DRequestGame%26placeId%3D{placeID}"
        )
        if gameID:
            args += f"%26gameID%3D{gameID}"

        print(f"Launching: {location}")
        if not os.path.exists(location):
            print(f"Error: Executable not found at {location}")
            return

        Popen([location, args])
        print("ROBLOX launched successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def stop_all_roblox_processes():
    print("Stopping all ROBLOX processes using win32...")
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] and 'roblox' in proc.info['name'].lower():
                pid = proc.info['pid']
                print(f"Attempting to terminate: {proc.info['name']} (PID: {pid})")
                handle = win32api.OpenProcess(win32con.PROCESS_TERMINATE, 0, pid)
                win32api.TerminateProcess(handle, 0)
                win32api.CloseHandle(handle)
                print(f"Successfully terminated: {proc.info['name']} (PID: {pid})")
        except Exception as e:
            print(f"Failed to terminate process (PID: {proc.info['pid']}): {e}")
    print("All ROBLOX processes stopped.")

def save_cookies():
    try:
        service = Service()
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.roblox.com/login")

        print("Please log in manually in the browser window...")
        WebDriverWait(driver, 99999).until(
            EC.url_to_be("https://www.roblox.com/home")
        )

        print("Login detected. Saving cookies...")

        cookies = driver.get_cookies()
        roblosecurity_cookie = None
        for cookie in cookies:
            if cookie['name'] == '.ROBLOSECURITY':
                roblosecurity_cookie = cookie['value']
                break

        if roblosecurity_cookie:
            with open(DEFAULT_COOKIES_FILE, "a", encoding="utf-8") as file:
                stripped_cookie = roblosecurity_cookie.strip()
                file.write(f"{stripped_cookie}\n")
                print("Added cookie")
        else:
            print(".ROBLOSECURITY cookie not found.")
    except Exception as e:
        print(f"Error during login: {str(e)}")
    finally:
        driver.quit()

def run_app():
    global message_loop_running, message_loop_thread

    def start_process():
        global message_loop_running, message_loop_thread

        if message_loop_running:
            print("The process is already running.")
            return

        place_id = place_id_entry.get().strip()
        game_id = game_id_entry.get().strip()
        num_accounts = num_accounts_entry.get().strip()

        if not place_id:
            messagebox.showerror("Input Error", "Place ID is required.")
            return

        try:
            num_accounts = int(num_accounts)
            if num_accounts <= 0:
                raise ValueError("Number of accounts must be greater than zero.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number of accounts.")
            return

        try:
            with open(DEFAULT_COOKIES_FILE, "r") as file:
                cookies = file.read().splitlines()
                cookies = cookies[:num_accounts]

            print("Starting process and message loop...")
            message_loop_running = True
            message_loop_thread = threading.Thread(target=messageLoop, daemon=True)
            message_loop_thread.start()

            threading.Thread(
                target=launch_accounts, args=(place_id, game_id, cookies), daemon=True
            ).start()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to start: {str(e)}")

    def launch_accounts(place_id, game_id, cookies):
        for cookie in cookies:
            if not message_loop_running:
                print("Process stopped before all accounts were launched.")
                break
            startGame(place_id, game_id, cookie.strip())
            print("Waiting for 10 seconds before launching the next account...")
            time.sleep(10)

    def stop_process():
        global message_loop_running, message_loop_thread

        if not message_loop_running:
            print("The process is not running.")
            return

        print("Stopping message loop...")
        # Stop the message loop safely
        message_loop_running = False

        # Wait for the message loop thread to exit
        if message_loop_thread and message_loop_thread.is_alive():
            message_loop_thread.join(timeout=5)
            print("Message loop thread has stopped.")

        # Stop Roblox processes in a separate thread to avoid GUI blocking
        threading.Thread(target=stop_all_roblox_processes, daemon=True).start()
        print("Process stopped.")

    def login():
        threading.Thread(target=save_cookies, daemon=True).start()

    # Main Window
    root = tk.Tk()
    root.title("MultiStrap")
    root.resizable(False, False)

    # Place ID
    tk.Label(root, text="Place ID:").grid(row=0, column=0, padx=10, pady=5)
    place_id_entry = tk.Entry(root)
    place_id_entry.grid(row=0, column=1, padx=10, pady=5)

    # Game/Job ID
    tk.Label(root, text="Game/Job ID:").grid(row=1, column=0, padx=10, pady=5)
    game_id_entry = tk.Entry(root)
    game_id_entry.grid(row=1, column=1, padx=10, pady=5)

    # Number of accounts
    tk.Label(root, text="Number of Accounts:").grid(row=2, column=0, padx=10, pady=5)
    num_accounts_entry = tk.Entry(root)
    num_accounts_entry.grid(row=2, column=1, padx=10, pady=5)

    # Start/Stop Buttons
    tk.Button(root, text="Start", command=start_process, bg="green", fg="white", width=15).grid(row=3, column=0, padx=10, pady=5)
    tk.Button(root, text="Stop", command=stop_process, bg="red", fg="white", width=15).grid(row=3, column=1, padx=10, pady=5)
    tk.Button(root, text="Login", command=login, bg="blue", fg="white", width=15).grid(row=4, column=0, padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    run_app()