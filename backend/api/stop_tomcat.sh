#!/bin/bash

catalina.sh stop

#!/bin/bash

echo "🧟 Kill any zombie processes lingering in the system."

PIDS=$(ps aux | grep vscode-remote-containers-server | grep -v grep | awk '{print $2}')

if [ -z "$PIDS" ]; then
  echo "Zombie processes not exist."
else
  echo "kill process: $PIDS"
  for PID in $PIDS; do
    kill -9 "$PID" && echo "Killed $PID" || echo "Failed to kill PID $PID"
  done
fi
