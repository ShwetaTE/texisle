To build docker in local and push it:
docker build -t texisle-django:<version> -f Dockerfile.dev .
docker save texisle-django:<version> > texisle-docker.tar.gz
scp texisle-docker.tar.gz root@<IP Address>:/home/docker-file


On server pull and run the docker:
docker pull thirdeyedata.jfrog.io/texisle-local/texisle-django:1.0.0
docker run -d -p 8000:8000 --name texisle-python thirdeyedata.jfrog.io/texisle-local/texisle-django:1.0.1

setup ODBC driver
https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15#download-for-windows
https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15