from docker_watchdog.Watchdog import Watchdog

# Customize these as needed
SLEEP_SECONDS = 10
IDLE_TIMEOUT = 60
BILLING_GRANULARITY = 0
PERCENTAGE_THRESHOLD = 0.5

watchdog = Watchdog(SLEEP_SECONDS, IDLE_TIMEOUT, BILLING_GRANULARITY, PERCENTAGE_THRESHOLD)
watchdog.start()
