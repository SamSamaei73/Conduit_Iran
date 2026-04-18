# اجرای Conduit با Docker

docker pull ghcr.io/ssmirr/conduit/conduit:latest

# اجرای کانتینر


docker run -d \
  --name conduit \
  --restart unless-stopped \
  -v conduit-data:/home/conduit/data \
  ghcr.io/ssmirr/conduit/conduit:2fd31d4 \
  start \
  --data-dir /home/conduit/data \
  --max-clients 200 \
  --bandwidth 5


# چک کن که اجرا شده

docker logs -f conduit


# ===================================================================================


# توقف کانتینر

docker stop conduit


# حذف کانتینر

docker rm conduit

#  چک کن چیزی باقی نمانده

docker ps -a


# اگر هنوز conduit را دیدی


docker rm -f conduit
