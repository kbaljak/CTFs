FROM docker.io/nginx:alpine

# Copy our custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Create directory for our content
RUN mkdir -p /opt/files

# Copy sample content
COPY content/ /opt/files/

COPY flag.txt /opt

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"] 
