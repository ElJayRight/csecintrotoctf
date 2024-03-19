# Use an official Ubuntu image as the base image
FROM ubuntu:20.04

# Install Apache2, PHP, and required PHP modules
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 php libapache2-mod-php php-mysql php-cgi php-curl php-json && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Enable Apache2 modules
RUN a2enmod rewrite

# Set the working directory to /var/www/html
WORKDIR /var/www/html

# Create the four directories for flag files in the root directory
RUN mkdir -p /flag00 \
             /flag01 \
             /flag02 \
             /flag03

# Copy your web app files into the container's web root directory
COPY ./src .

# Copy the flag.txt file from the working directory to /Flagishere/ and then remove it
RUN cp flag.txt /flag02/ && rm flag.txt

# Start Apache2 in the foreground
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

