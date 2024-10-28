# Dockerfile
FROM python:3.9-slim

# Install necessary packages
RUN apt-get update && apt-get install -y bash supervisor && pip install psutil \
    && useradd -ms /bin/bash victim

# Copy application files
COPY ./src/*.py /root/
COPY ./src/flag.txt /home/victim/

# Make Other Directories and Files
RUN mkdir -p /tmp /usr/bnc 

RUN touch /tmp/abyss /tmp/singularity /tmp/orphans\
    /home/council /tmp/.loab /tmp/loab /tmp/.boom \
    /usr/bnc/.yummyarbs /home/victim/.consortium && \
    chmod 755 /tmp/ /usr/bnc/ /home/victim/

# Set correct permissions for Python scripts
RUN chmod 700 /root/*.py  # Only root can read, write, and execute these scripts

# Give root user access to modify files in /tmp/ and /home/victim/
RUN chown -R root:root /tmp/ /home/victim/

# Give victim user access to read files everywhere *but* in /root/
RUN chown -R victim:victim /home/victim/ /usr/bnc/

# Expose port
EXPOSE 9999

# Set up supervisord configuration
RUN echo "[supervisord]" > /etc/supervisor/conf.d/supervisord.conf && \
    echo "nodaemon=true" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "[program:welcome]" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "command=python3 /root/welcome.py" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "user=root" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "autostart=true" >> /etc/supervisor/conf.d/supervisord.conf && \
    echo "autorestart=true" >> /etc/supervisor/conf.d/supervisord.conf

WORKDIR /root/

# Start supervisord
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]