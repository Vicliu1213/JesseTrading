#!/bin/bash

echo "Starting Redis server in background..."
redis-server --port 6379 --bind 0.0.0.0 --save "" --appendonly no > /tmp/redis-output.log 2>&1 &
REDIS_PID=$!

sleep 3

echo "Checking Redis connection..."
MAX_RETRIES=10
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    if redis-cli ping > /dev/null 2>&1; then
        echo "✓ Redis is running successfully (PID: $REDIS_PID)!"
        break
    fi
    RETRY_COUNT=$((RETRY_COUNT+1))
    echo "Waiting for Redis to start... ($RETRY_COUNT/$MAX_RETRIES)"
    sleep 1
done

if [ $RETRY_COUNT -eq $MAX_RETRIES ]; then
    echo "ERROR: Redis failed to start after $MAX_RETRIES attempts"
    cat /tmp/redis-output.log
    exit 1
fi

echo "Checking if port 5000 is available..."
if lsof -ti:5000 > /dev/null; then
    echo "Port 5000 is in use, killing existing processes..."
    lsof -ti:5000 | xargs kill -9 2>/dev/null || true
    sleep 2
fi

echo "Starting Jesse Trading Framework..."
echo "Dashboard will be available at: http://localhost:5000"

# 启动 Jesse 并绑定到所有接口
jesse run --host 0.0.0.0 --port 5000un
