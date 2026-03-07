# اجرای Conduit با Docker

docker pull ghcr.io/ssmirr/conduit/conduit:latest

# اجرای کانتینر

docker run -d \
--name conduit \
-v conduit-data:/home/conduit/data \
--restart unless-stopped \
ghcr.io/ssmirr/conduit/conduit:latest \
start -m 500 -b 40



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
