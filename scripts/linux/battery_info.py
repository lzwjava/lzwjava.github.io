import psutil
import os
import time

def get_battery_info():
    try:
        # Get battery information using psutil
        battery = psutil.sensors_battery()
        
        if battery is None:
            print("No battery detected.")
            return

        # Battery percentage
        percent = battery.percent
        print(f"Battery Percentage: {percent}%")

        # Check if battery is charging
        is_charging = battery.power_plugged
        status = "Charging" if is_charging else "Discharging"
        print(f"Status: {status}")

        # Estimate remaining time (only when discharging)
        if not is_charging and battery.secsleft != psutil.POWER_TIME_UNLIMITED:
            remaining_secs = battery.secsleft
            hours = remaining_secs // 3600
            minutes = (remaining_secs % 3600) // 60
            print(f"Estimated Time Remaining: {hours} hours, {minutes} minutes")
        elif is_charging:
            # Try to estimate time to full charge using sysfs
            try:
                # Read battery info from sysfs
                with open('/sys/class/power_supply/BAT0/charge_now', 'r') as f:
                    charge_now = int(f.read().strip())
                with open('/sys/class/power_supply/BAT0/charge_full', 'r') as f:
                    charge_full = int(f.read().strip())
                with open('/sys/class/power_supply/BAT0/current_now', 'r') as f:
                    current_now = int(f.read().strip())

                if current_now > 0:
                    charge_remaining = charge_full - charge_now
                    seconds_to_full = (charge_remaining / current_now) * 3600
                    hours = int(seconds_to_full // 3600)
                    minutes = int((seconds_to_full % 3600) // 60)
                    print(f"Estimated Time to Full Charge: {hours} hours, {minutes} minutes")
                else:
                    print("Cannot estimate time to full charge (current_now is 0).")
            except FileNotFoundError:
                print("Cannot estimate time to full charge (sysfs files not found).")
            except Exception as e:
                print(f"Error estimating time to full charge: {e}")
        else:
            print("No remaining time estimate available.")

    except Exception as e:
        print(f"Error retrieving battery information: {e}")

if __name__ == "__main__":
    get_battery_info()