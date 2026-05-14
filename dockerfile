FROM ubuntu:22.04

# Evita blocchi interattivi durante l'installazione dei pacchetti
ENV DEBIAN_FRONTEND=noninteractive

# Aggiorna il sistema e installa SSH e sudo
RUN apt-get update && apt-get install -y \
    openssh-server \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Crea le cartelle necessarie per il funzionamento di SSH
RUN mkdir /var/run/sshd

# Configura le variabili per il nuovo utente (puoi cambiarle qui)
ARG USERNAME=utentesftp
ARG PASSWORD=PasswordSicura123!

# Crea l'utente, imposta la password e aggiungilo al gruppo sudo
RUN useradd -m -s /bin/bash $USERNAME && \
    echo "$USERNAME:$PASSWORD" | chpasswd && \
    usermod -aG sudo $USERNAME

# Configurazione di sicurezza minima per SSH
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Espone la porta 22 per le connessioni SFTP
EXPOSE 22

# Avvia il server SSH in primo piano per mantenere attivo il container
CMD ["/usr/sbin/sshd", "-D"]
